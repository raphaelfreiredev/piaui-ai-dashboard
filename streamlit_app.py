import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os
import sys
from datetime import datetime
import io

# Add scripts directory to path
sys.path.append('scripts')

from rss_collector import RSSCollector
from sentiment_analyzer import SentimentAnalyzer

# Page configuration
st.set_page_config(
    page_title="Monitor IA Piauí",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .ethics-disclaimer {
        background-color: #fff3cd;
        border: 1px solid #ffeaa7;
        border-radius: 0.5rem;
        padding: 1rem;
        margin-top: 2rem;
        font-size: 0.9rem;
    }
    .data-source {
        font-size: 0.8rem;
        color: #666;
        font-style: italic;
    }
</style>
""", unsafe_allow_html=True)

def load_data():
    """Load or collect news data"""
    data_file = "data/analyzed_news.csv"
    
    if os.path.exists(data_file):
        try:
            df = pd.read_csv(data_file)
            return df, False  # Data loaded from file
        except Exception as e:
            st.error(f"Erro ao carregar dados salvos: {e}")
    
    # If no saved data, collect new data
    return None, True  # Need to collect new data

def collect_fresh_data():
    """Collect fresh news data"""
    with st.spinner("Coletando notícias do Google News..."):
        collector = RSSCollector()
        analyzer = SentimentAnalyzer()
        
        # Collect news
        news_data = collector.collect_all_news(max_per_term=4)
        
        if not news_data:
            st.error("Não foi possível coletar notícias. Verifique sua conexão com a internet.")
            return None
        
        # Convert to DataFrame and analyze sentiment
        df = pd.DataFrame(news_data)
        df = analyzer.analyze_dataframe(df)
        
        # Save data
        os.makedirs("data", exist_ok=True)
        df.to_csv("data/analyzed_news.csv", index=False, encoding='utf-8')
        
        return df

def create_sentiment_pie_chart(df):
    """Create pie chart for sentiment distribution"""
    if df.empty or 'sentiment' not in df.columns:
        return None
    
    sentiment_counts = df['sentiment'].value_counts()
    
    # Define colors for sentiments
    colors = {
        'positivo': '#2ecc71',
        'negativo': '#e74c3c', 
        'neutro': '#95a5a6'
    }
    
    # Create pie chart
    fig = go.Figure(data=[go.Pie(
        labels=sentiment_counts.index,
        values=sentiment_counts.values,
        hole=0.4,
        marker_colors=[colors.get(label, '#3498db') for label in sentiment_counts.index],
        textinfo='label+percent',
        textfont_size=12
    )])
    
    fig.update_layout(
        title={
            'text': "Distribuição de Sentimentos",
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18}
        },
        showlegend=True,
        height=400,
        margin=dict(t=60, b=20, l=20, r=20)
    )
    
    return fig

def create_wordcloud(df):
    """Create word cloud from news titles"""
    if df.empty:
        return None
    
    analyzer = SentimentAnalyzer()
    word_freq = analyzer.get_word_frequency(df, 'title')
    
    if not word_freq:
        return None
    
    # Create word cloud
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white',
        colormap='viridis',
        max_words=50,
        relative_scaling=0.5,
        random_state=42
    ).generate_from_frequencies(word_freq)
    
    # Create matplotlib figure
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    ax.set_title('Palavras Mais Frequentes', fontsize=16, pad=20)
    
    return fig

def format_dataframe_for_display(df):
    """Format dataframe for better display"""
    if df.empty:
        return df
    
    # Select and rename columns for display
    display_df = df[['title', 'description', 'sentiment', 'search_term', 'pub_date']].copy()
    
    display_df.columns = [
        'Título',
        'Descrição', 
        'Sentimento',
        'Termo de Busca',
        'Data de Publicação'
    ]
    
    # Truncate long descriptions
    display_df['Descrição'] = display_df['Descrição'].apply(
        lambda x: x[:100] + "..." if len(str(x)) > 100 else x
    )
    
    # Translate sentiment values
    sentiment_translation = {
        'positivo': '😊 Positivo',
        'negativo': '😞 Negativo', 
        'neutro': '😐 Neutro'
    }
    display_df['Sentimento'] = display_df['Sentimento'].map(sentiment_translation)
    
    return display_df

def main():
    # Header
    st.markdown('<h1 class="main-header">🤖 Monitor IA Piauí</h1>', unsafe_allow_html=True)
    st.markdown('<p class="data-source">Monitoramento de menções sobre Inteligência Artificial no Piauí</p>', unsafe_allow_html=True)
    
    # Sidebar
    st.sidebar.title("⚙️ Configurações")
    
    # Data loading/collection
    df, needs_collection = load_data()
    
    if st.sidebar.button("🔄 Coletar Dados Atualizados"):
        df = collect_fresh_data()
        if df is not None:
            st.sidebar.success("Dados coletados com sucesso!")
            st.rerun()
    
    if df is None and needs_collection:
        st.warning("Nenhum dado encontrado. Clique em 'Coletar Dados Atualizados' para buscar notícias.")
        df = collect_fresh_data()
    
    if df is None or df.empty:
        st.error("Não foi possível carregar ou coletar dados de notícias.")
        return
    
    # Display last update time
    if os.path.exists("data/analyzed_news.csv"):
        mod_time = os.path.getmtime("data/analyzed_news.csv")
        last_update = datetime.fromtimestamp(mod_time).strftime("%d/%m/%Y às %H:%M")
        st.sidebar.info(f"📅 Última atualização: {last_update}")
    
    # Main metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("📰 Total de Notícias", len(df))
    
    with col2:
        positive_count = len(df[df['sentiment'] == 'positivo'])
        st.metric("😊 Sentimento Positivo", positive_count)
    
    with col3:
        negative_count = len(df[df['sentiment'] == 'negativo'])
        st.metric("😞 Sentimento Negativo", negative_count)
    
    with col4:
        neutral_count = len(df[df['sentiment'] == 'neutro'])
        st.metric("😐 Sentimento Neutro", neutral_count)
    
    st.divider()
    
    # Charts section
    col1, col2 = st.columns(2)
    
    with col1:
        # Sentiment pie chart
        pie_fig = create_sentiment_pie_chart(df)
        if pie_fig:
            st.plotly_chart(pie_fig, use_container_width=True)
        else:
            st.warning("Não foi possível gerar o gráfico de sentimentos.")
    
    with col2:
        # Word cloud
        st.subheader("☁️ Nuvem de Palavras")
        wordcloud_fig = create_wordcloud(df)
        if wordcloud_fig:
            st.pyplot(wordcloud_fig)
        else:
            st.warning("Não foi possível gerar a nuvem de palavras.")
    
    st.divider()
    
    # Data table
    st.subheader("📋 Dados Coletados e Classificados")
    
    # Filter options
    col1, col2 = st.columns(2)
    with col1:
        sentiment_filter = st.selectbox(
            "Filtrar por sentimento:",
            ["Todos", "positivo", "negativo", "neutro"]
        )
    
    with col2:
        search_terms = df['search_term'].unique()
        term_filter = st.selectbox(
            "Filtrar por termo de busca:",
            ["Todos"] + list(search_terms)
        )
    
    # Apply filters
    filtered_df = df.copy()
    if sentiment_filter != "Todos":
        filtered_df = filtered_df[filtered_df['sentiment'] == sentiment_filter]
    if term_filter != "Todos":
        filtered_df = filtered_df[filtered_df['search_term'] == term_filter]
    
    # Display filtered data
    display_df = format_dataframe_for_display(filtered_df)
    st.dataframe(display_df, use_container_width=True, height=400)
    
    # Download button
    if not df.empty:
        csv = df.to_csv(index=False, encoding='utf-8')
        st.download_button(
            label="📥 Baixar dados completos (CSV)",
            data=csv,
            file_name=f"ia_piaui_monitor_{datetime.now().strftime('%Y%m%d_%H%M')}.csv",
            mime="text/csv"
        )
    
    # Ethics disclaimer
    st.markdown("""
    <div class="ethics-disclaimer">
        <h4>⚠️ Limitações da Análise</h4>
        <p>Esta análise de sentimento é baseada em regras simples e pode não capturar sarcasmo ou contextos complexos. 
        Os resultados devem ser interpretados como uma aproximação e não como uma análise definitiva do sentimento público.</p>
        
        <p><strong>Metodologia:</strong> A coleta de dados utiliza feeds RSS do Google Notícias com termos de busca específicos. 
        A análise de sentimento emprega listas de palavras-chave em português para classificação automática.</p>
        
        <p><strong>Transparência:</strong> Este sistema foi desenvolvido com auxílio de IA para estruturação do código e 
        implementação de funcionalidades específicas.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<p style='text-align: center; color: #666; font-size: 0.8rem;'>"
        "Monitor IA Piauí - Desenvolvido para acompanhar o desenvolvimento da Inteligência Artificial no estado"
        "</p>", 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
