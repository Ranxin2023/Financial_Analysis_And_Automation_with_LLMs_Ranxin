import concurrent.futures
from modules.get_stock_info import get_stock_info
from modules.get_company_tickets import get_company_tickers
#import packages
from langchain.schema import Document
from langchain_pinecone import PineconeVectorStore
from langchain_community.embeddings import HuggingFaceEmbeddings
hf_embeddings = HuggingFaceEmbeddings()
# Initialize tracking lists
successful_tickers = []
unsuccessful_tickers = []
company_tickers = get_company_tickers()
index_name = "stocks"
namespace = "stock-descriptions"
# Load existing successful/unsuccessful tickers
try:
    with open('successful_tickers.txt', 'r') as f:
        successful_tickers = [line.strip() for line in f if line.strip()]
    # print(f"Loaded {len(successful_tickers)} successful tickers")
except FileNotFoundError:
    print("No existing successful tickers file found")

try:
    with open('unsuccessful_tickers.txt', 'r') as f:
        unsuccessful_tickers = [line.strip() for line in f if line.strip()]
    # print(f"Loaded {len(unsuccessful_tickers)} unsuccessful tickers")
except FileNotFoundError:
    print("No existing unsuccessful tickers file found")

def process_stock(stock_ticker: str) -> str:
    # Skip if already processed
    if stock_ticker in successful_tickers:
        return f"Already processed {stock_ticker}"

    try:
        # Get and store stock data
        stock_data = get_stock_info(stock_ticker)
        stock_description = stock_data['Business Summary']

        # Store stock description in Pinecone
        vectorstore_from_texts = PineconeVectorStore.from_documents(
            documents=[Document(page_content=stock_description, metadata=stock_data)],
            embedding=hf_embeddings,
            index_name=index_name,
            namespace=namespace
        )

        # Track success
        with open('successful_tickers.txt', 'a') as f:
            f.write(f"{stock_ticker}\n")
        successful_tickers.append(stock_ticker)

        return f"Processed {stock_ticker} successfully"

    except Exception as e:
        # Track failure
        with open('unsuccessful_tickers.txt', 'a') as f:
            f.write(f"{stock_ticker}\n")
        unsuccessful_tickers.append(stock_ticker)

        return f"ERROR processing {stock_ticker}: {e}"

def parallel_process_stocks(tickers: list, max_workers: int = 10) -> None:
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_ticker = {
            executor.submit(process_stock, ticker): ticker
            for ticker in tickers
        }

        for future in concurrent.futures.as_completed(future_to_ticker):
            ticker = future_to_ticker[future]
            try:
                result = future.result()
                print(result)

                # Stop on error
                if result.startswith("ERROR"):
                    print(f"Stopping program due to error in {ticker}")
                    executor.shutdown(wait=False)
                    raise SystemExit(1)

            except Exception as exc:
                print(f'{ticker} generated an exception: {exc}')
                print("Stopping program due to exception")
                executor.shutdown(wait=False)
                raise SystemExit(1)
            
# Prepare your tickers
tickers_to_process = [company_tickers[num]['ticker'] for num in company_tickers.keys()]

# Process them
parallel_process_stocks(tickers_to_process, max_workers=10)
