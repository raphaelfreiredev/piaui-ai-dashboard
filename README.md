# Monitor IA Piauí 🤖

Um painel simplificado para monitorar menções sobre "Inteligência Artificial no Piauí" em fontes de notícias públicas, com foco em análise de sentimento e identificação de temas recorrentes.

## 📋 Funcionalidades

- **Coleta Automatizada**: Busca notícias em feeds RSS do Google Notícias
- **Análise de Sentimento**: Classificação baseada em regras com palavras-chave em português
- **Visualizações Interativas**: 
  - Gráfico de pizza com distribuição de sentimentos
  - Nuvem de palavras com termos mais frequentes
  - Tabela interativa com dados coletados
- **Interface Web**: Dashboard desenvolvido em Streamlit
- **Exportação de Dados**: Download dos dados em formato CSV

## 🚀 Como Executar

### Pré-requisitos

- Python 3.8 ou superior
- Conexão com a internet para coleta de dados

### Instalação

1. Clone ou baixe este repositório
2. Instale as dependências:
\`\`\`bash
pip install -r requirements.txt
\`\`\`

### Execução

#### Opção 1: Dashboard Streamlit (Recomendado)
\`\`\`bash
streamlit run streamlit_app.py
\`\`\`

#### Opção 2: Coleta via linha de comando
\`\`\`bash
python scripts/run_collection.py
\`\`\`

#### Opção 3: Usando o script auxiliar
\`\`\`bash
python scripts/streamlit_runner.py
\`\`\`

O dashboard estará disponível em: https://piaui-ai-dashboard-cbdshy6hddwhq8qxu9fpyc.streamlit.app/

## 📊 Estrutura do Projeto

\`\`\`
├── streamlit_app.py          # Dashboard principal
├── scripts/
│   ├── rss_collector.py      # Coleta de dados RSS
│   ├── sentiment_analyzer.py # Análise de sentimento
│   ├── run_collection.py     # Pipeline completo
│   └── streamlit_runner.py   # Auxiliar para executar Streamlit
├── data/                     # Dados coletados (criado automaticamente)
├── requirements.txt          # Dependências Python
└── README.md                # Este arquivo
\`\`\`

## 🔍 Metodologia

### Coleta de Dados
- **Fonte**: Google Notícias (RSS feeds)
- **Termos de busca**: "Inteligência Artificial Piauí", "SIA Piauí", "IA Piauí"
- **Processamento**: Limpeza de HTML, remoção de duplicatas
- **Volume**: 10-15 notícias por execução

### Análise de Sentimento
- **Abordagem**: Baseada em regras com listas de palavras-chave
- **Idioma**: Português brasileiro
- **Categorias**: Positivo, Negativo, Neutro
- **Contexto**: Palavras específicas para IA e tecnologia

### Visualizações
- **Gráfico de Pizza**: Distribuição percentual dos sentimentos
- **Nuvem de Palavras**: 50 termos mais frequentes
- **Tabela Interativa**: Dados completos com filtros

## ⚠️ Limitações

- A análise de sentimento é baseada em regras simples e pode não capturar sarcasmo ou contextos complexos
- Dependente da disponibilidade dos feeds RSS do Google Notícias
- Resultados podem variar conforme a disponibilidade de notícias sobre o tema
- Não detecta ironia ou contextos implícitos

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**
- **Streamlit**: Interface web interativa
- **Pandas**: Manipulação de dados
- **Plotly**: Gráficos interativos
- **WordCloud**: Nuvem de palavras
- **Requests**: Requisições HTTP
- **XML ElementTree**: Processamento de feeds RSS

## 📈 Próximos Passos

- [ ] Implementar cache para melhor performance
- [ ] Adicionar mais fontes de notícias
- [ ] Melhorar algoritmo de análise de sentimento
- [ ] Implementar alertas para mudanças significativas
- [ ] Adicionar análise temporal (tendências)

## 🤝 Contribuições

Contribuições são bem-vindas! Por favor:

1. Faça um fork do projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto é de código aberto e está disponível sob a licença MIT.

---

**Desenvolvido para acompanhar o desenvolvimento da Inteligência Artificial no Piauí** 🏛️🤖
