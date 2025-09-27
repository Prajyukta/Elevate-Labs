# scraper.py
# Web scraper for news headlines

import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"  # You can change this to any news site
HEADLINES_FILE = "headlines.txt"

def fetch_headlines():
    try:
        response = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
        if response.status_code != 200:
            print("Failed to fetch the page. Status code:", response.status_code)
            return []

        soup = BeautifulSoup(response.text, "html.parser")
        
        # Find headlines (BBC uses <h2> and <h3>)
        headlines = []
        for h in soup.find_all(["h2", "h3"]):
            text = h.get_text(strip=True)
            if text and len(text) > 10:  # filter short/empty ones
                headlines.append(text)

        return headlines

    except Exception as e:
        print("Error occurred:", e)
        return []

def save_headlines(headlines):
    with open(HEADLINES_FILE, "w", encoding="utf-8") as file:
        for line in headlines:
            file.write(line + "\n")

def main():
    print("Fetching headlines...")
    headlines = fetch_headlines()

    if headlines:
        save_headlines(headlines)
        print(f"Saved {len(headlines)} headlines to {HEADLINES_FILE}")
    else:
        print("No headlines found.")

if __name__ == "__main__":
    main()
