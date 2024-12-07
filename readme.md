# Financial Analysis & Automation with LLMs

## Introduction

This project leverages AI and Natural Language Processing (NLP) to automate the research process for financial stocks. Users can input natural language queries, and the system ranks relevant stocks based on their descriptions, fetched dynamically using APIs. By employing techniques like cosine similarity and vector embedding, the system finds stocks most relevant to the user's query.

This repository also demonstrates optimized stock data processing using parallelization for faster computation, making it scalable and efficient for large datasets.


## Technologies Used
- Python
- Streamlit (Frontend for the chatbot)
- Pinecone (Vector database)
- LangChain (Framework for RAG)
- HuggingFace Transformers (Embeddings)
- Groq/OpenAI API (LLM for generating responses)
- Concurrency

## Sequential vs Parallel Processing
### Sequential Processing
Sequential processing involves fetching and storing data for stocks one by one. While simpler to implement, this method is slow and inefficient for processing a large number of stocks.

- Workflow
1. Fetch stock data for AAPL.
2. Wait for API response, store data.
3. Fetch stock data for GOOGL, and repeat for other stocks sequentially.


### Parallel Processing
To improve efficiency, the project uses parallel processing. Multiple worker threads process stocks simultaneously, significantly reducing processing time.

- Workflow
1. Distribute stocks across workers.
2. Fetch and store data concurrently.
3. Monitor progress and handle errors dynamically.

## Setup and Running Instructions
1. clone the repository
```sh
git clone https://github.com/Ranxin2023/Financial_Analysis_And_Automation_with_LLMs_Ranxin
```

2. Install Dependencies
Ensure you have Python 3.8+ installed. Install required packages:
```sh
pip install -r requirements.txt
```

3. Set Up API Keys
- Create a `.env` file in the root directory and add the following:
```sh
PINECONE_API_KEY=your-pinecone-api-key
GROQ_API_KEY=your-groq-api-key
```

- Replace your-pinecone-api-key and your-groq-api-key with your respective API keys.

4. Set up Pinecone
- Go to [Pinecone Dashboard](https://app.pinecone.io/).
- Create an index with the following settings:
    - Dimension: 768
    - Namespace: `codebase-rag`
- Note the environment (e.g., `us-west1-gcp`) and ensure it matches your code.

5. Get groq keys [here](https://console.groq.com/keys)

6. Process all the stock locally
Run the `process_stocks.py` script to process all the stock data and generate two local files:
- `successful_tickers.txt` (contains successfully processed stocks)
- `unsuccessful_tickers.txt` (contains stocks that failed processing)
```sh
python process_stocks.py

```
The script will update the local files as it processes the stocks. It will stop when no further updates are made to the `successful_tickers.txt` file.
For reference, the number of successfully processed stocks in my case is 6968.


7. Launch the Streamlit app:
```sh
streamlit run app.py

```

## Project Structure
```sh
PROJECT2/
├── modules/                            # Core modules for processing stock data
│   ├── __init__.py                     # Module initialization
│   ├── get_company_tickets.py          # Fetches company tickers
│   ├── get_stock_info.py               # Retrieves stock information from Yahoo Finance
│   └── process_stock.py                # Parallel processing and storing of stock data
│
├── NLP_utils/                          # Utilities for NLP processing
│   ├── __init__.py                     # Module initialization
│   ├── get_cos_similarity.py           # Computes cosine similarity between embeddings
│   └── get_huggingface_embeddings.py   # Generates embeddings using HuggingFace
│
├── assets/                             # Diagrams and JSON files
│   ├── company_tickers.json            # Contains all company tickers data
│   ├── parallel_diagram.png            # Diagram illustrating parallel processing
│   └── serial_diagram.png              # Diagram illustrating sequential processing
│
├── .env                                # Environment variables (API keys)
├── .gitignore                          # Git ignore file
├── app.py                              # Main Streamlit application
├── README.md                           # Project documentation
├── requirements.txt                    # Python dependencies
├── process_stocks                      # process all the stocks in parallel
├── successful_tickers.txt              # List of successfully processed tickers
└── unsuccessful_tickers.txt            # List of unsuccessfully processed tickers

```

## Usage Example

### Question
What are some companies that manufacture consumer hardware?

### Answer
Based on your context, it appears that you are looking for companies that manufacture consumer hardware. Here are some popular companies that fit the bill:

1. NVIDIA (NVDA): Although not exclusively a hardware manufacturer, they design and manufacture graphics processing units (GPUs) that are widely used in gaming and other consumer electronics.
2. Taiwan Semiconductor Manufacturing Company (TSM): TSMC is a leading semiconductor foundry, producing a wide range of consumer electronics components, including processors, memory chips, and other hardware components used in consumer devices.
As for other companies not listed in the provided context:

1. Apple (AAPL): Designs and manufactures iPhones, Macs, iPads, Apple Watches, and AirPods.
2. Samsung Electronics (SSNLF): Manufactures a wide range of consumer electronics, including smartphones, televisions, home appliances, and wearables.
3. Dell Technologies (DELL): Designs and manufactures a broad range of consumer electronics, including PCs, laptops, tablets, and other devices.
4. HP Inc. (HPQ): Manufactures a wide range of consumer electronics, including PCs, printers, laptops, and other devices.
5. Intel Corporation (INTC): Designs and manufactures microprocessors, chipsets, and other hardware components used in consumer electronics.

Please note that the list is not exhaustive, and there are many other companies that manufacture consumer hardware components and devices.