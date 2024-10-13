# scraper.py

def scrape_latest_news():
    """
    Scrapes the latest news articles.
    
    This is a placeholder function that currently returns dummy news articles.
    """
    print("Scraping news... (placeholder)")

    # Return some dummy articles for now
    articles = [
        {
            "title": "Sample News Article 1",
            "description": "This is a description of sample news article 1. It covers the latest developments in technology.",
            "url": "https://example.com/article1",
            "source": "Example News",
            "published_at": "2024-10-01T12:00:00Z"
        },
        {
            "title": "Sample News Article 2",
            "description": "This is a description of sample news article 2. It discusses recent events in global politics.",
            "url": "https://example.com/article2",
            "source": "Example News",
            "published_at": "2024-10-02T12:00:00Z"
        },
        {
            "title": "Sample News Article 3",
            "description": "This is a description of sample news article 3. It analyzes the current economic trends.",
            "url": "https://example.com/article3",
            "source": "Example News",
            "published_at": "2024-10-03T12:00:00Z"
        },
        {
            "title": "Sample News Article 4",
            "description": "This is a description of sample news article 4. It provides insights into the latest scientific discoveries.",
            "url": "https://example.com/article4",
            "source": "Example News",
            "published_at": "2024-10-04T12:00:00Z"
        },
        {
            "title": "Sample News Article 5",
            "description": "This is a description of sample news article 5. It features the latest trends in entertainment.",
            "url": "https://example.com/article5",
            "source": "Example News",
            "published_at": "2024-10-05T12:00:00Z"
        },
    ]
    return articles

# Example usage for testing
if __name__ == "__main__":
    articles = scrape_latest_news()
    for article in articles:
        print(f"Title: {article['title']}")
        print(f"Description: {article['description']}")
        print(f"URL: {article['url']}")
        print(f"Source: {article['source']}")
        print(f"Published At: {article['published_at']}")
        print("=" * 40)
