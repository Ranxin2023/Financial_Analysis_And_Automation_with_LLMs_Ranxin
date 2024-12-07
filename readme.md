# Financial Analysis & Automation with LLMs

## Technologies Used
- Python
- Streamlit (Frontend for the chatbot)
- Pinecone (Vector database)
- LangChain (Framework for RAG)
- HuggingFace Transformers (Embeddings)
- Groq/OpenAI API (LLM for generating responses)
- Concurrency

## Setup Instructions
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

6. Run the Application
Launch the Streamlit app:
```sh
streamlit run app.py

```

## Project Structure
```sh
.
├── modules/
│   ├── get_company_tickets.py    # Module to fetch and manage company tickers from external sources
│   ├── get_stock_info.py         # Module to retrieve stock details from Yahoo Finance and preprocess data
│   ├── process_stock.py          # Methods for processing the stock in serialization and parallelism
│   └── __init__.py               # Module initialization
│── NLP_utils/
│   ├──get_cos_similarity.py         # Utility to calculate cosine similarity between text embeddings
│   ├──get_huggingface_embeddings.py # Utility for generating embeddings using HuggingFace models
├── app.py                        # Main Streamlit application
├── requirements.txt              # Python dependencies
├── .env                          # Environment variables (API keys)
└── README.md                     # Project documentation

```


