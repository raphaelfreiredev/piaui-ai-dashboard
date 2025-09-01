# Guia de Contribuição - Monitor IA Piauí

Obrigado pelo interesse em contribuir com o Monitor IA Piauí! Este documento fornece diretrizes para contribuições éticas e efetivas.

## 🤝 Como Contribuir

### Tipos de Contribuição Bem-vindas

#### 1. **Melhorias no Código**
- Correção de bugs
- Otimização de performance
- Refatoração para melhor legibilidade
- Implementação de novas funcionalidades

#### 2. **Aprimoramento da Análise**
- Expansão das listas de palavras-chave
- Melhoria das regras de sentimento
- Adição de novos termos de busca relevantes
- Validação de resultados

#### 3. **Documentação**
- Correção de erros na documentação
- Tradução para outros idiomas
- Exemplos de uso
- Tutoriais e guias

#### 4. **Interface e UX**
- Melhorias na interface Streamlit
- Novas visualizações
- Acessibilidade
- Design responsivo

### Processo de Contribuição

#### 1. **Issues**
- Verifique se já existe uma issue similar
- Use templates apropriados
- Forneça informações detalhadas
- Inclua exemplos quando possível

#### 2. **Pull Requests**
- Fork o repositório
- Crie uma branch descritiva
- Faça commits claros e concisos
- Teste suas mudanças
- Atualize documentação se necessário

#### 3. **Code Review**
- Seja respeitoso e construtivo
- Foque no código, não na pessoa
- Explique o raciocínio por trás das sugestões
- Reconheça boas práticas

## 📋 Diretrizes Técnicas

### Padrões de Código

#### Python
\`\`\`python
# Use docstrings para funções públicas
def analyze_sentiment(self, text):
    """
    Analyze sentiment of a single text.
    
    Args:
        text (str): Text to analyze
        
    Returns:
        tuple: (sentiment, positive_count, negative_count)
    """
    pass

# Use type hints quando possível
def process_data(df: pd.DataFrame) -> pd.DataFrame:
    pass

# Siga PEP 8 para formatação
# Use nomes descritivos para variáveis
\`\`\`

#### Comentários
- Explique o "porquê", não apenas o "o quê"
- Use português para comentários de domínio específico
- Use inglês para comentários técnicos gerais

### Testes
- Adicione testes para novas funcionalidades
- Mantenha cobertura de testes existente
- Use dados de exemplo realistas
- Teste casos edge

### Documentação
- Atualize README.md para novas funcionalidades
- Documente mudanças em DECISIONS.md
- Mantenha ETHICS.md atualizado
- Use markdown consistente

## 🎯 Áreas Prioritárias

### 1. **Melhoria da Análise de Sentimento**
- **Prioridade**: Alta
- **Descrição**: Expandir listas de palavras-chave específicas para IA no Piauí
- **Habilidades**: Conhecimento de português, contexto local
- **Impacto**: Melhoria direta na qualidade das análises

### 2. **Diversificação de Fontes**
- **Prioridade**: Média
- **Descrição**: Adicionar outras fontes além do Google News
- **Habilidades**: Web scraping, APIs
- **Impacto**: Cobertura mais ampla de notícias

### 3. **Interface e Visualizações**
- **Prioridade**: Média
- **Descrição**: Melhorar dashboard Streamlit
- **Habilidades**: Streamlit, Plotly, UX/UI
- **Impacto**: Melhor experiência do usuário

### 4. **Performance e Escalabilidade**
- **Prioridade**: Baixa
- **Descrição**: Otimizar para volumes maiores de dados
- **Habilidades**: Otimização Python, caching
- **Impacto**: Preparação para crescimento

## 🔍 Revisão de Contribuições

### Critérios de Aceitação

#### Funcionalidade
- [ ] Código funciona conforme especificado
- [ ] Não quebra funcionalidades existentes
- [ ] Inclui tratamento de erros apropriado
- [ ] Performance é aceitável

#### Qualidade
- [ ] Código é legível e bem estruturado
- [ ] Segue padrões estabelecidos
- [ ] Inclui documentação adequada
- [ ] Testes passam

#### Ética
- [ ] Não introduz vieses intencionais
- [ ] Respeita privacidade dos usuários
- [ ] Mantém transparência
- [ ] Considera impacto social

### Processo de Review

1. **Revisão Automática**
   - Testes automatizados
   - Verificação de estilo
   - Análise de segurança básica

2. **Revisão Manual**
   - Funcionalidade
   - Qualidade do código
   - Documentação
   - Considerações éticas

3. **Teste da Comunidade**
   - Feedback de usuários
   - Teste em diferentes cenários
   - Validação de resultados

## 🌟 Reconhecimento

### Contribuidores
- Todos os contribuidores são reconhecidos no README
- Contribuições significativas são destacadas
- Histórico de contribuições é mantido

### Tipos de Reconhecimento
- **Code Contributors**: Contribuições de código
- **Documentation Contributors**: Melhorias na documentação
- **Community Contributors**: Suporte à comunidade
- **Research Contributors**: Validação e pesquisa

## 📞 Comunicação

### Canais
- **Issues**: Para bugs e solicitações de funcionalidades
- **Discussions**: Para discussões gerais e ideias
- **Pull Requests**: Para revisão de código
- **Email**: Para questões sensíveis ou privadas

### Diretrizes de Comunicação
- Seja respeitoso e inclusivo
- Use linguagem clara e objetiva
- Forneça contexto suficiente
- Seja paciente com respostas

## 🚫 Código de Conduta

### Comportamento Esperado
- Respeito mútuo
- Colaboração construtiva
- Foco no bem comum
- Transparência nas intenções

### Comportamento Inaceitável
- Discriminação ou assédio
- Linguagem ofensiva
- Spam ou autopromoção excessiva
- Violação de privacidade

### Consequências
- Advertência
- Suspensão temporária
- Banimento permanente
- Remoção de contribuições

## 📚 Recursos Úteis

### Documentação Técnica
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Plotly Documentation](https://plotly.com/python/)

### Contexto Local
- Notícias sobre tecnologia no Piauí
- Iniciativas de IA no estado
- Universidades e centros de pesquisa locais

### Ferramentas
- Python 3.8+
- Git e GitHub
- Editor de código (VS Code recomendado)
- Ambiente virtual (venv ou conda)

---

**Juntos podemos criar uma ferramenta valiosa para acompanhar o desenvolvimento da IA no Piauí!**

*Para dúvidas sobre este guia, abra uma issue ou entre em contato.*
