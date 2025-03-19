import requests
from datetime import datetime, timedelta

def scrape_latest_news(query="news"):
    # Get today's date in YYYY-MM-DD format
    today = datetime.today()
    from_date = (today - timedelta(days=7)).strftime('%Y-%m-%d')
    to_date = today.strftime('%Y-%m-%d')

    # API Key from NewsAPI
    api_key = 'api_key'
    url = "https://newsapi.org/v2/everything"

    # Define parameters for API request
    params = {
        "q": query,
        "from": from_date,
        "to": to_date,
        "sortBy": "publishedAt",
        "apiKey": api_key,
        "language": "en",
        "pageSize": 50,
    }

    try:
        # Send GET request to NewsAPI
        response = requests.get(url, params=params)
        # print(f"Request URL: {response.url}")  # Debugging URL
        if response.status_code == 200:
            data = response.json()
            # print(f"API Response: {data}")  # Debugging output

            if "articles" in data and data["articles"]:
                articles = data["articles"]
                news_articles = []
                for article in articles:
                    # Extract necessary fields safely
                    news_articles.append({
                        'title': article.get('title', 'No title available'),
                        'description': article.get('description', 'No description available'),
                        'url': article.get('url', 'No URL available'),
                        'source': article.get('source', {}).get('name', 'No source available'),
                        'publishedAt': article.get('publishedAt', 'No published date available'),
                        'author': article.get('author', 'Unknown Author'),
                        'image': article.get('urlToImage', 'No image available'),
                    })

                return news_articles
            else:
                print("No articles found.")
                return []
        else:
            print(f"Error fetching news: {response.status_code} - {response.text}")
            return []

    except Exception as e:
        print(f"Error in scrape_latest_news: {str(e)}")
        return []
