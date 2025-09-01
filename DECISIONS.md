# Decisões de Desenvolvimento - Monitor IA Piauí

Este documento explica as principais decisões técnicas tomadas durante o desenvolvimento do sistema de monitoramento de menções sobre Inteligência Artificial no Piauí.

## 📊 Análise de Sentimento: Por que Regras ao invés de Machine Learning?

### Decisão Tomada
Optamos por uma abordagem baseada em **regras simples** com listas de palavras-chave em português, ao invés de utilizar modelos de Machine Learning pré-treinados.

### Justificativas

#### 1. **Transparência e Explicabilidade**
- **Vantagem**: Cada classificação pode ser facilmente explicada e auditada
- **Impacto**: Usuários podem entender exatamente por que uma notícia foi classificada como positiva, negativa ou neutra
- **Exemplo**: Se uma notícia contém "inovação" e "desenvolvimento", é clara a razão da classificação positiva

#### 2. **Controle Total sobre o Contexto**
- **Vantagem**: Palavras-chave específicas para o contexto "IA no Piauí"
- **Implementação**: Criamos listas customizadas incluindo termos como "SIA Piauí", "universidade", "startup"
- **Flexibilidade**: Fácil ajuste das regras conforme feedback dos usuários

#### 3. **Simplicidade de Implementação e Manutenção**
- **Vantagem**: Não requer modelos complexos, datasets de treinamento ou GPUs
- **Manutenção**: Atualizações simples através da modificação das listas de palavras
- **Debugging**: Fácil identificação e correção de problemas de classificação

#### 4. **Adequação ao Escopo do Projeto**
- **Volume**: Para 10-15 notícias por coleta, a abordagem é suficiente
- **Domínio**: Tema específico (IA no Piauí) permite regras bem direcionadas
- **Objetivo**: Monitoramento geral de tendências, não análise acadêmica profunda

#### 5. **Recursos Limitados**
- **Infraestrutura**: Não requer APIs pagas ou modelos pesados
- **Latência**: Processamento instantâneo sem dependências externas
- **Confiabilidade**: Funciona offline após instalação inicial

### Limitações Reconhecidas

#### 1. **Contextos Complexos**
- **Limitação**: Não detecta sarcasmo, ironia ou contextos implícitos
- **Exemplo**: "Que inovação incrível!" (sarcástico) seria classificado como positivo
- **Mitigação**: Disclaimer claro sobre limitações no dashboard

#### 2. **Nuances Linguísticas**
- **Limitação**: Não considera negações complexas ou modificadores
- **Exemplo**: "não é uma boa inovação" pode ser mal classificado
- **Mitigação**: Revisão periódica das regras baseada em feedback

#### 3. **Evolução da Linguagem**
- **Limitação**: Gírias e termos novos não são automaticamente incorporados
- **Mitigação**: Atualizações manuais das listas de palavras-chave

## 🔧 Tratamento de Erros e Ausência de Notícias

### Estratégias Implementadas

#### 1. **Múltiplos Termos de Busca**
\`\`\`python
self.search_terms = [
    "Inteligência Artificial Piauí",
    "SIA Piauí", 
    "IA Piauí",
    "Artificial Intelligence Piauí"
]
\`\`\`
- **Objetivo**: Aumentar chances de encontrar conteúdo relevante
- **Benefício**: Cobertura mais ampla mesmo com termos específicos

#### 2. **Tratamento Robusto de Exceções**
\`\`\`python
try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
except requests.RequestException as e:
    print(f"Error fetching news for '{search_term}': {e}")
    return []
\`\`\`
- **Timeout**: 10 segundos para evitar travamentos
- **Headers personalizados**: User-Agent para evitar bloqueios
- **Graceful degradation**: Continua funcionando mesmo com falhas parciais

#### 3. **Validação e Limpeza de Dados**
\`\`\`python
def clean_text(self, text):
    if not text:
        return ""
    # Remove HTML tags, caracteres especiais, etc.
\`\`\`
- **Verificações**: Campos vazios ou nulos são tratados
- **Sanitização**: Remoção de HTML e caracteres especiais
- **Normalização**: Espaços extras e formatação inconsistente

#### 4. **Remoção de Duplicatas**
\`\`\`python
seen_titles = set()
for item in all_news:
    title_lower = item['title'].lower()
    if title_lower not in seen_titles and title_lower:
        seen_titles.add(title_lower)
        unique_news.append(item)
\`\`\`
- **Critério**: Títulos similares (case-insensitive)
- **Benefício**: Evita análises redundantes

#### 5. **Feedback Informativo**
- **Logs detalhados**: Quantidade de artigos por termo de busca
- **Mensagens de status**: Progresso da coleta em tempo real
- **Alertas no dashboard**: Quando não há dados disponíveis

#### 6. **Fallback e Recuperação**
\`\`\`python
if not news_data:
    st.error("Não foi possível coletar notícias. Verifique sua conexão com a internet.")
    return None
\`\`\`
- **Interface**: Mensagens claras sobre problemas
- **Dados salvos**: Utiliza dados anteriores quando disponíveis
- **Retry manual**: Botão para nova tentativa de coleta

### Cenários de Erro Contemplados

#### 1. **Sem Conexão com Internet**
- **Detecção**: Timeout nas requisições HTTP
- **Ação**: Mensagem informativa + uso de dados em cache
- **UX**: Dashboard continua funcional com dados anteriores

#### 2. **RSS Feed Indisponível**
- **Detecção**: Erro HTTP 404/500 ou XML malformado
- **Ação**: Tenta outros termos de busca
- **Fallback**: Informa usuário sobre fonte temporariamente indisponível

#### 3. **Nenhuma Notícia Encontrada**
- **Detecção**: Lista vazia após todas as buscas
- **Ação**: Mensagem explicativa sobre possíveis causas
- **Sugestão**: Tentar novamente em horário diferente

#### 4. **Dados Corrompidos**
- **Detecção**: Erro ao carregar CSV ou dados inconsistentes
- **Ação**: Coleta nova automática
- **Backup**: Logs para debugging

## 🤖 Transparência sobre Uso de IA

### Componentes Desenvolvidos com Auxílio de IA

#### 1. **Estruturação Inicial do Código**
- **Ferramenta**: Assistente de IA (v0)
- **Uso**: Geração da estrutura base das classes e funções
- **Customização**: Adaptação manual para requisitos específicos

#### 2. **Listas de Palavras-chave**
- **Ferramenta**: Assistente de IA para brainstorming inicial
- **Uso**: Sugestão de palavras positivas/negativas em português
- **Validação**: Revisão manual e ajustes contextuais

#### 3. **Interface Streamlit**
- **Ferramenta**: Assistente de IA para layout e componentes
- **Uso**: Estrutura do dashboard e visualizações
- **Personalização**: Styling e funcionalidades específicas

#### 4. **Documentação**
- **Ferramenta**: Assistente de IA para estruturação
- **Uso**: Organização de seções e formatação
- **Conteúdo**: Decisões técnicas e explicações são autorais

### Componentes Desenvolvidos Manualmente

#### 1. **Lógica de Negócio**
- **Algoritmo de sentimento**: Regras específicas para o contexto
- **Tratamento de erros**: Estratégias baseadas em experiência prática
- **Validações**: Critérios específicos para qualidade dos dados

#### 2. **Configurações e Parâmetros**
- **Termos de busca**: Selecionados com base no conhecimento do domínio
- **Thresholds**: Definidos através de testes empíricos
- **Timeouts e limites**: Baseados em performance observada

## 📋 Metodologia de Desenvolvimento

### 1. **Desenvolvimento Iterativo**
- Implementação por etapas (coleta → análise → visualização)
- Testes contínuos com dados reais
- Refinamento baseado em resultados observados

### 2. **Validação Empírica**
- Testes com diferentes termos de busca
- Verificação manual de classificações
- Ajustes baseados em casos edge

### 3. **Documentação Contínua**
- Decisões registradas durante desenvolvimento
- Limitações identificadas e documentadas
- Instruções claras para uso e manutenção

## 🔮 Considerações Futuras

### Possíveis Melhorias

#### 1. **Análise de Sentimento**
- Implementação de modelos de ML quando volume justificar
- Incorporação de análise de contexto mais sofisticada
- Treinamento com dados específicos do domínio

#### 2. **Coleta de Dados**
- Diversificação de fontes (além do Google News)
- Implementação de cache inteligente
- Coleta programada (cron jobs)

#### 3. **Interface e UX**
- Dashboards mais interativos
- Alertas automáticos para mudanças significativas
- Análise temporal e tendências

### Critérios para Evolução
- **Volume**: Quando coleta superar 100+ artigos/dia
- **Precisão**: Se taxa de erro superar 20%
- **Demanda**: Baseado em feedback dos usuários
- **Recursos**: Disponibilidade de infraestrutura adequada

---

*Este documento será atualizado conforme o sistema evolui e novas decisões técnicas são tomadas.*
