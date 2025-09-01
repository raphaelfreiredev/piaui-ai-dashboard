import pandas as pd
import re
from collections import Counter

class SentimentAnalyzer:
    def __init__(self):
        # Portuguese positive words related to AI and technology
        self.positive_words = {
            'inovação', 'inovador', 'inovadora', 'sucesso', 'avanço', 'progresso',
            'desenvolvimento', 'crescimento', 'melhoria', 'eficiência', 'otimização',
            'revolucionário', 'revolucionária', 'transformação', 'modernização',
            'benefício', 'vantagem', 'oportunidade', 'potencial', 'promissor',
            'promissora', 'excelente', 'positivo', 'positiva', 'bom', 'boa',
            'melhor', 'superior', 'avançado', 'avançada', 'inteligente',
            'eficaz', 'produtivo', 'produtiva', 'competitivo', 'competitiva',
            'líder', 'liderança', 'pioneiro', 'pioneira', 'destaque'
        }
        
        # Portuguese negative words
        self.negative_words = {
            'problema', 'dificuldade', 'desafio', 'obstáculo', 'barreira',
            'limitação', 'preocupação', 'risco', 'ameaça', 'perigo',
            'negativo', 'negativa', 'ruim', 'pior', 'inferior', 'falha',
            'erro', 'fracasso', 'insucesso', 'declínio', 'redução',
            'diminuição', 'perda', 'prejuízo', 'crítica', 'criticar',
            'controverso', 'controversa', 'polêmico', 'polêmica',
            'resistência', 'oposição', 'conflito', 'tensão'
        }
        
        # Context-specific words for AI in Piauí
        self.context_positive = {
            'investimento', 'parceria', 'colaboração', 'universidade',
            'pesquisa', 'startup', 'empreendedorismo', 'tecnologia',
            'digital', 'futuro', 'capacitação', 'treinamento'
        }
        
        self.context_negative = {
            'desemprego', 'substituição', 'automação', 'exclusão',
            'digital', 'atraso', 'falta', 'carência', 'ausência'
        }
        
        # Combine all word sets
        self.all_positive = self.positive_words.union(self.context_positive)
        self.all_negative = self.negative_words.union(self.context_negative)
    
    def preprocess_text(self, text):
        """Clean and preprocess text for analysis"""
        if not text:
            return ""
        
        # Convert to lowercase
        text = text.lower()
        
        # Remove punctuation and special characters
        text = re.sub(r'[^\w\s]', ' ', text)
        
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        
        return text.strip()
    
    def analyze_sentiment(self, text):
        """Analyze sentiment of a single text"""
        if not text:
            return 'neutro', 0, 0
        
        processed_text = self.preprocess_text(text)
        words = processed_text.split()
        
        positive_count = sum(1 for word in words if word in self.all_positive)
        negative_count = sum(1 for word in words if word in self.all_negative)
        
        # Determine sentiment
        if positive_count > negative_count:
            sentiment = 'positivo'
        elif negative_count > positive_count:
            sentiment = 'negativo'
        else:
            sentiment = 'neutro'
        
        return sentiment, positive_count, negative_count
    
    def analyze_dataframe(self, df):
        """Analyze sentiment for entire dataframe"""
        if df.empty:
            return df
        
        sentiments = []
        positive_counts = []
        negative_counts = []
        
        for _, row in df.iterrows():
            # Combine title and description for analysis
            full_text = f"{row.get('title', '')} {row.get('description', '')}"
            sentiment, pos_count, neg_count = self.analyze_sentiment(full_text)
            
            sentiments.append(sentiment)
            positive_counts.append(pos_count)
            negative_counts.append(neg_count)
        
        # Add sentiment columns
        df['sentiment'] = sentiments
        df['positive_words_count'] = positive_counts
        df['negative_words_count'] = negative_counts
        
        return df
    
    def get_word_frequency(self, df, column='title'):
        """Get word frequency for word cloud"""
        if df.empty:
            return {}
        
        all_text = ' '.join(df[column].fillna('').astype(str))
        processed_text = self.preprocess_text(all_text)
        words = processed_text.split()
        
        # Filter out common stop words in Portuguese
        stop_words = {
            'de', 'da', 'do', 'das', 'dos', 'a', 'o', 'as', 'os', 'e', 'em',
            'para', 'com', 'por', 'no', 'na', 'nos', 'nas', 'um', 'uma',
            'uns', 'umas', 'que', 'se', 'é', 'são', 'foi', 'foram', 'ser',
            'ter', 'tem', 'mais', 'muito', 'sua', 'seu', 'suas', 'seus',
            'sobre', 'entre', 'quando', 'onde', 'como', 'também', 'já',
            'ainda', 'só', 'depois', 'antes', 'agora', 'aqui', 'ali',
            'isso', 'isto', 'essa', 'esse', 'esta', 'este'
        }
        
        # Filter words
        filtered_words = [
            word for word in words 
            if len(word) > 2 and word not in stop_words
        ]
        
        return dict(Counter(filtered_words).most_common(50))
    
    def get_sentiment_summary(self, df):
        """Get summary statistics of sentiment analysis"""
        if df.empty or 'sentiment' not in df.columns:
            return {}
        
        sentiment_counts = df['sentiment'].value_counts()
        total = len(df)
        
        summary = {
            'total_articles': total,
            'positive': sentiment_counts.get('positivo', 0),
            'negative': sentiment_counts.get('negativo', 0),
            'neutral': sentiment_counts.get('neutro', 0),
            'positive_percentage': round((sentiment_counts.get('positivo', 0) / total) * 100, 1),
            'negative_percentage': round((sentiment_counts.get('negativo', 0) / total) * 100, 1),
            'neutral_percentage': round((sentiment_counts.get('neutro', 0) / total) * 100, 1)
        }
        
        return summary

# Test the analyzer
if __name__ == "__main__":
    # Test with sample data
    sample_data = {
        'title': [
            'Piauí investe em inteligência artificial para desenvolvimento',
            'Desafios da implementação de IA no estado',
            'Nova startup de IA surge em Teresina'
        ],
        'description': [
            'Estado anuncia investimento em tecnologia inovadora',
            'Dificuldades técnicas impedem progresso',
            'Empreendedores locais criam solução inteligente'
        ]
    }
    
    df = pd.DataFrame(sample_data)
    analyzer = SentimentAnalyzer()
    
    # Analyze sentiment
    df_analyzed = analyzer.analyze_dataframe(df)
    print("Sentiment Analysis Results:")
    print(df_analyzed[['title', 'sentiment']])
    
    # Get summary
    summary = analyzer.get_sentiment_summary(df_analyzed)
    print("\nSentiment Summary:")
    print(summary)
