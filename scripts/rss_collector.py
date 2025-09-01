import requests
import xml.etree.ElementTree as ET
import pandas as pd
import re
from datetime import datetime
from urllib.parse import quote

class RSSCollector:
    def __init__(self):
        self.base_url = "https://news.google.com/rss/search"
        self.search_terms = [
            "Inteligência Artificial Piauí",
            "SIA Piauí",
            "IA Piauí",
            "Artificial Intelligence Piauí"
        ]
        
    def clean_text(self, text):
        """Remove HTML tags and special characters from text"""
        if not text:
            return ""
        
        # Remove HTML tags
        clean = re.compile('<.*?>')
        text = re.sub(clean, '', text)
        
        # Remove extra whitespace and special characters
        text = re.sub(r'\s+', ' ', text)
        text = text.strip()
        
        return text
    
    def fetch_news_for_term(self, search_term, max_results=5):
        """Fetch news for a specific search term"""
        try:
            # Encode search term for URL
            encoded_term = quote(search_term)
            url = f"{self.base_url}?q={encoded_term}&hl=pt-BR&gl=BR&ceid=BR:pt-419"
            
            print(f"Fetching news for: {search_term}")
            print(f"URL: {url}")
            
            # Make request with headers to avoid blocking
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            # Parse XML
            root = ET.fromstring(response.content)
            
            news_items = []
            items = root.findall('.//item')[:max_results]
            
            for item in items:
                title = item.find('title')
                link = item.find('link')
                description = item.find('description')
                pub_date = item.find('pubDate')
                
                news_item = {
                    'title': self.clean_text(title.text if title is not None else ''),
                    'link': link.text if link is not None else '',
                    'description': self.clean_text(description.text if description is not None else ''),
                    'pub_date': pub_date.text if pub_date is not None else '',
                    'search_term': search_term,
                    'collected_at': datetime.now().isoformat()
                }
                
                news_items.append(news_item)
            
            print(f"Found {len(news_items)} articles for '{search_term}'")
            return news_items
            
        except requests.RequestException as e:
            print(f"Error fetching news for '{search_term}': {e}")
            return []
        except ET.ParseError as e:
            print(f"Error parsing XML for '{search_term}': {e}")
            return []
        except Exception as e:
            print(f"Unexpected error for '{search_term}': {e}")
            return []
    
    def collect_all_news(self, max_per_term=4):
        """Collect news from all search terms"""
        all_news = []
        
        for term in self.search_terms:
            news_items = self.fetch_news_for_term(term, max_per_term)
            all_news.extend(news_items)
        
        # Remove duplicates based on title
        seen_titles = set()
        unique_news = []
        
        for item in all_news:
            title_lower = item['title'].lower()
            if title_lower not in seen_titles and title_lower:
                seen_titles.add(title_lower)
                unique_news.append(item)
        
        print(f"Total unique articles collected: {len(unique_news)}")
        return unique_news
    
    def save_to_csv(self, news_data, filename="news_data.csv"):
        """Save collected news to CSV file"""
        if not news_data:
            print("No news data to save")
            return
        
        df = pd.DataFrame(news_data)
        df.to_csv(filename, index=False, encoding='utf-8')
        print(f"Data saved to {filename}")
        return df

# Test the collector
if __name__ == "__main__":
    collector = RSSCollector()
    news_data = collector.collect_all_news()
    
    if news_data:
        df = collector.save_to_csv(news_data)
        print("\nSample of collected data:")
        print(df[['title', 'search_term']].head())
    else:
        print("No news data collected")
