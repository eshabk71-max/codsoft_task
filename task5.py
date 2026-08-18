import pandas as pd
import requests
from bs4 import BeautifulSoup

# 1. Web Scraping setup (Quotes to Scrape website)
url = "http://quotes.toscrape.com/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    quotes_data = []
    quotes = soup.find_all("div", class_="quote")

    # 2. Extract Data (Quotes & Authors)
    for q in quotes:
        text = q.find("span", class_="text").text
        author = q.find("small", class_="author").text
        quotes_data.append({"Quote": text, "Author": author})

    # 3. Create DataFrame & Clean Data
    df = pd.DataFrame(quotes_data)

    print("=== Extracted Web Data ===")
    print(df.head())

    # 4. Save to CSV (Bonus Task)
    csv_path = r"C:\Users\eshab khan\OneDrive\Desktop\DataAnalytics\extracted_web_data.csv"
    df.to_csv(csv_path, index=False)
    print(f"\nData saved successfully to: {csv_path}")

else:
    print("Failed to fetch web page.")