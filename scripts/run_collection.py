#!/usr/bin/env python3
"""
Main script to run the complete data collection and analysis pipeline
"""

import sys
import os
from datetime import datetime

# Add the scripts directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from rss_collector import RSSCollector
from sentiment_analyzer import SentimentAnalyzer

def main():
    print("=== AI Piauí News Monitor ===")
    print(f"Starting data collection at {datetime.now()}")
    print("-" * 50)
    
    # Initialize components
    collector = RSSCollector()
    analyzer = SentimentAnalyzer()
    
    # Step 1: Collect news data
    print("Step 1: Collecting news from RSS feeds...")
    news_data = collector.collect_all_news(max_per_term=4)
    
    if not news_data:
        print("❌ No news data collected. Exiting.")
        return
    
    # Step 2: Save raw data
    print("\nStep 2: Saving raw data...")
    df = collector.save_to_csv(news_data, "data/raw_news.csv")
    
    # Step 3: Analyze sentiment
    print("\nStep 3: Analyzing sentiment...")
    df_analyzed = analyzer.analyze_dataframe(df)
    
    # Step 4: Save analyzed data
    print("\nStep 4: Saving analyzed data...")
    df_analyzed.to_csv("data/analyzed_news.csv", index=False, encoding='utf-8')
    
    # Step 5: Generate summary
    print("\nStep 5: Generating summary...")
    summary = analyzer.get_sentiment_summary(df_analyzed)
    word_freq = analyzer.get_word_frequency(df_analyzed)
    
    print("\n" + "="*50)
    print("COLLECTION SUMMARY")
    print("="*50)
    print(f"Total articles collected: {summary['total_articles']}")
    print(f"Positive sentiment: {summary['positive']} ({summary['positive_percentage']}%)")
    print(f"Negative sentiment: {summary['negative']} ({summary['negative_percentage']}%)")
    print(f"Neutral sentiment: {summary['neutral']} ({summary['neutral_percentage']}%)")
    
    print(f"\nTop 10 most frequent words:")
    for word, count in list(word_freq.items())[:10]:
        print(f"  {word}: {count}")
    
    print(f"\nData saved to:")
    print(f"  - data/raw_news.csv")
    print(f"  - data/analyzed_news.csv")
    
    print(f"\nCollection completed at {datetime.now()}")

if __name__ == "__main__":
    # Create data directory if it doesn't exist
    os.makedirs("data", exist_ok=True)
    main()
