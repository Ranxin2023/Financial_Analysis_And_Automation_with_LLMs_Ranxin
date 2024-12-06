"""# Get all the Stocks in the Stock Market

First, we need to get the symbols (also known as tickers) of all the stocks in the stock market
"""
import requests, json
def get_company_tickers():
    """
    Downloads and parses the Stock ticker symbols from the GitHub-hosted SEC company tickers JSON file.

    Returns:
        dict: A dictionary containing company tickers and related information.

    Notes:
        The data is sourced from the official SEC website via a GitHub repository:
        https://raw.githubusercontent.com/team-headstart/Financial-Analysis-and-Automation-with-LLMs/main/company_tickers.json
    """
    # URL to fetch the raw JSON file from GitHub
    url = "https://raw.githubusercontent.com/team-headstart/Financial-Analysis-and-Automation-with-LLMs/main/company_tickers.json"

    # Making a GET request to the URL
    response = requests.get(url)

    # Checking if the request was successful
    if response.status_code == 200:
        # Parse the JSON content directly
        company_tickers = json.loads(response.content.decode('utf-8'))

        # Optionally save the content to a local file for future use
        with open("company_tickers.json", "w", encoding="utf-8") as file:
            json.dump(company_tickers, file, indent=4)

        print("File downloaded successfully and saved as 'company_tickers.json'")
        return company_tickers
    else:
        print(f"Failed to download file. Status code: {response.status_code}")
        return None