import requests
from bs4 import BeautifulSoup

def scrape_news_headlines(url, output_file="headlines.txt"):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        headlines = []
        for tag in soup.find_all(["h2", "title"]):
            headline_text = tag.get_text(strip=True)
            if headline_text:
                headlines.append(headline_text)


        with open(output_file, "w", encoding="utf-8") as file:
            for headline in headlines:
                file.write(headline + "\n")

        print(f"Successfully scraped headlines from {url} and saved to {output_file}.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    news_website_url = input("Enter the news website URL: ")
    scrape_news_headlines(news_website_url)


