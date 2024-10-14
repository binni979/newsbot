def scrape_latest_news():
    # This function is a placeholder for web scraping news articles
    articles = [
        {
            "title": "Nepal Celebrates Vijaya Dashami Amidst Challenges",
            "description": "Prime Minister K P Sharma Oli and President Ram Chandra Paudel extend greetings to citizens during Vijaya Dashami, urging support for those impacted by recent floods and landslides.",
            "url": "https://www.devdiscourse.com/article/entertainment/2634630-celebrating-amidst-challenges-nepals-vijaya-dashami-festival",
            "source": "Devdiscourse",
            "published_at": "2024-10-12T15:56:00Z"
        },
        {
            "title": "Floods and Landslides Devastate Nepal",
            "description": "Recent natural disasters in Nepal have caused 240 fatalities and displaced thousands, impacting travel during the Dashain festival.",
            "url": "https://www.devdiscourse.com/article/environment/2634632-devastating-floods-and-landslides-wreak-havoc-across-nepal",
            "source": "Devdiscourse",
            "published_at": "2024-10-12T14:30:00Z"
        },
        {
            "title": "Nepal's Dashain Celebrations Amidst Natural Disasters",
            "description": "Despite travel challenges, 1.3 million people traveled home for Dashain, emphasizing the spirit of resilience.",
            "url": "https://www.devdiscourse.com/article/culture/2634633-nepals-dashain-celebrations-amidst-natural-disasters",
            "source": "Devdiscourse",
            "published_at": "2024-10-12T13:45:00Z"
        }
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
