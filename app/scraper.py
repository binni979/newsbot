def scrape_latest_news():
    # This function returns dummy news articles with detailed descriptions
    articles = [
        {
            "title": "AI Breakthrough in Cancer Detection",
            "description": "Scientists at Global Health Institute have developed a revolutionary AI system capable of detecting early signs of cancer with an accuracy of 98%. This advancement is expected to transform the medical industry by drastically reducing diagnostic errors and enabling earlier treatment interventions, potentially saving millions of lives annually.",
            "url": "https://www.example.com/ai-cancer-detection",
            "source": "Health Today",
            "published_at": "2024-10-12T10:00:00Z"
        },
        {
            "title": "Global Climate Summit Urges Immediate Action",
            "description": "World leaders gathered at the 2024 Global Climate Summit to address the urgent need for sustainable energy solutions. With record-breaking heatwaves and natural disasters increasing worldwide, experts are calling for accelerated investments in renewable energy and stricter carbon emission regulations to mitigate the impact of climate change.",
            "url": "https://www.example.com/global-climate-summit",
            "source": "Eco News",
            "published_at": "2024-10-11T14:45:00Z"
        },
        {
            "title": "Nepal Celebrates Vijaya Dashami Amidst Challenges",
            "description": "Prime Minister K P Sharma Oli and President Ram Chandra Paudel extend greetings to citizens during Vijaya Dashami, urging support for those impacted by recent floods and landslides. The festival's religious importance is being celebrated in parallel with ongoing recovery efforts in affected areas.",
            "url": "https://www.example.com/nepal-dashami-celebration",
            "source": "Devdiscourse",
            "published_at": "2024-10-12T15:56:00Z"
        },
        {
            "title": "Floods and Landslides Devastate Nepal",
            "description": "Recent natural disasters in Nepal have caused 240 fatalities and displaced thousands, severely impacting infrastructure and disrupting travel during the Dashain festival. The government has allocated emergency funds for relief efforts, but the recovery process is expected to take months.",
            "url": "https://www.example.com/nepal-floods-landslides",
            "source": "Devdiscourse",
            "published_at": "2024-10-12T14:30:00Z"
        },
        {
            "title": "Global Tech Companies Eye Expansion in Africa",
            "description": "Tech giants such as Google and Microsoft have announced plans to expand their presence in Africa, aiming to tap into the continent's rapidly growing digital economy. By investing in infrastructure, training, and local talent, these companies hope to establish Africa as a major hub for technology innovation in the coming years.",
            "url": "https://www.example.com/tech-expansion-africa",
            "source": "Tech World",
            "published_at": "2024-10-10T09:00:00Z"
        },
        {
            "title": "SpaceX Successfully Launches First All-Civilian Mission to Mars",
            "description": "In a historic achievement, SpaceX launched its first all-civilian crewed mission to Mars. The crew, composed of scientists and engineers, will conduct groundbreaking research on the Martian surface. This mission marks a significant step toward SpaceX's goal of establishing a permanent human colony on Mars within the next decade.",
            "url": "https://www.example.com/spacex-mars-mission",
            "source": "Space News",
            "published_at": "2024-10-09T18:30:00Z"
        },
        {
            "title": "ç",
            "description": "A team of researchers from MIT has developed a new battery technology capable of storing renewable energy for up to 10 times longer than current solutions. This breakthrough could solve one of the major challenges facing the adoption of solar and wind energy by providing reliable storage during periods of low production.",
            "url": "https://www.example.com/renewable-energy-storage",
            "source": "Science Daily",
            "published_at": "2024-10-11T11:20:00Z"
        },
        {
            "title": "Global Food Prices Surge Amidst Supply Chain Disruptions",
            "description": "The global food supply chain continues to face unprecedented disruptions due to ongoing geopolitical conflicts and climate-related disasters. As a result, food prices have surged by 15% in the last quarter alone, placing significant strain on low-income populations and leading to increased calls for food security reforms.",
            "url": "https://www.example.com/global-food-price-surge",
            "source": "Financial Times",
            "published_at": "2024-10-08T08:10:00Z"
        },
        {
            "title": "Advancements in Quantum Computing Pave the Way for Breakthroughs in Medicine",
            "description": "Quantum computing is set to revolutionize medical research, with new algorithms that can model complex molecular structures at an unprecedented scale. These advancements are expected to accelerate drug discovery processes and provide new insights into genetic diseases, opening the door for personalized medicine breakthroughs.",
            "url": "https://www.example.com/quantum-computing-medicine",
            "source": "Tech Insights",
            "published_at": "2024-10-07T12:00:00Z"
        },
        {
            "title": "World Cup 2024: The Rise of Underdogs",
            "description": "The 2024 FIFA World Cup has seen unexpected victories from teams considered underdogs, sparking excitement among fans worldwide. With several top-ranked teams eliminated early, the tournament has become one of the most unpredictable and thrilling in recent memory, capturing the spirit of competition on the global stage.",
            "url": "https://www.example.com/world-cup-2024-underdogs",
            "source": "Sports Daily",
            "published_at": "2024-10-12T17:45:00Z"
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
