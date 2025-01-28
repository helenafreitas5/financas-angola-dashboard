import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import numpy as np

# Configuração da página com tema personalizado
st.set_page_config(
    page_title="Análise Financeira GenAI - Angola",
    page_icon="🇦🇴",
    layout="wide"
)

# Função para criar dados fictícios da execução orçamentária
def criar_dados_orcamento():
    """
    Cria dados fictícios de execução orçamentária por setor e período
    Retorna um DataFrame com informações de orçamento planejado vs realizado
    """
    setores = ['Saúde', 'Educação', 'Infraestrutura', 'Agricultura', 'Defesa', 
               'Energia', 'Transportes', 'Tecnologia', 'Administração']
    
    dados = []
    data_inicial = datetime(2023, 1, 1)
    
    for mes in range(12):
        data = data_inicial + timedelta(days=mes*30)
        for setor in setores:
            orcamento_planejado = np.random.uniform(5000000, 15000000)
            # O realizado varia entre 80% e 120% do planejado
            orcamento_realizado = orcamento_planejado * np.random.uniform(0.8, 1.2)
            
            dados.append({
                'Data': data,
                'Setor': setor,
                'Orçamento_Planejado': orcamento_planejado,
                'Orçamento_Realizado': orcamento_realizado,
                'Taxa_Execução': (orcamento_realizado/orcamento_planejado) * 100
            })
    
    return pd.DataFrame(dados)

# Função para criar dados fictícios de receitas fiscais
def criar_dados_receitas():
    """
    Cria dados fictícios de receitas fiscais por tipo e região
    Retorna um DataFrame com informações detalhadas de arrecadação
    """
    tipos_receita = ['IVA', 'Imposto de Renda', 'Royalties Petróleo', 
                     'Taxas Aduaneiras', 'Impostos Corporativos']
    regioes = ['Luanda', 'Benguela', 'Huambo', 'Huíla', 'Cabinda']
    
    dados = []
    data_inicial = datetime(2023, 1, 1)
    
    for mes in range(12):
        data = data_inicial + timedelta(days=mes*30)
        for tipo in tipos_receita:
            for regiao in regioes:
                valor = np.random.uniform(1000000, 8000000)
                dados.append({
                    'Data': data,
                    'Tipo_Receita': tipo,
                    'Região': regiao,
                    'Valor': valor,
                    'Meta_Mensal': valor * np.random.uniform(0.9, 1.1)
                })
    
    return pd.DataFrame(dados)

# Função para criar dados fictícios de dívida pública
def criar_dados_divida():
    """
    Cria dados fictícios da dívida pública
    Retorna um DataFrame com informações sobre a dívida interna e externa
    """
    tipos_divida = ['Interna', 'Externa']
    categorias = ['Títulos Governamentais', 'Empréstimos Bancários', 
                  'Organismos Internacionais', 'Bonds Soberanos']
    
    dados = []
    data_inicial = datetime(2023, 1, 1)
    
    for mes in range(12):
        data = data_inicial + timedelta(days=mes*30)
        for tipo in tipos_divida:
            for categoria in categorias:
                valor = np.random.uniform(10000000, 50000000)
                juros = np.random.uniform(0.03, 0.08)
                dados.append({
                    'Data': data,
                    'Tipo_Dívida': tipo,
                    'Categoria': categoria,
                    'Valor': valor,
                    'Taxa_Juros': juros,
                    'Prazo_Anos': np.random.randint(5, 30)
                })
    
    return pd.DataFrame(dados)

# Função para criar dados fictícios de indicadores econômicos
def criar_dados_indicadores():
    """
    Cria dados fictícios de indicadores econômicos
    Retorna um DataFrame com diversos indicadores macroeconômicos
    """
    dados = []
    data_inicial = datetime(2023, 1, 1)
    
    for mes in range(12):
        data = data_inicial + timedelta(days=mes*30)
        dados.append({
            'Data': data,
            'PIB_Variação': np.random.uniform(-0.5, 2.0),
            'Inflação': np.random.uniform(5, 12),
            'Taxa_Câmbio_USD': np.random.uniform(500, 550),
            'Reservas_Internacionais': np.random.uniform(15000, 20000),
            'Preço_Petróleo': np.random.uniform(70, 90)
        })
    
    return pd.DataFrame(dados)

# Função do Agente IA para análise avançada dos dados
def analisar_dados_ia(pergunta, dfs):
    """
    Função que analisa os dados usando processamento de linguagem natural
    Recebe uma pergunta em linguagem natural e os DataFrames com os dados
    Retorna uma resposta contextualizada com análises relevantes
    """
    pergunta = pergunta.lower()
    
    # Extrai os DataFrames do dicionário
    df_orcamento = dfs['orcamento']
    df_receitas = dfs['receitas']
    df_divida = dfs['divida']
    df_indicadores = dfs['indicadores']
    
    # Análise baseada em palavras-chave e contexto
    resposta = ""
    
    # Análise de orçamento
    if any(palavra in pergunta for palavra in ['orçamento', 'gastos', 'despesas']):
        taxa_media_execucao = df_orcamento['Taxa_Execução'].mean()
        setor_maior_orcamento = df_orcamento.groupby('Setor')['Orçamento_Realizado'].sum().idxmax()
        
        resposta += f"A taxa média de execução orçamentária é de {taxa_media_execucao:.1f}%. "
        resposta += f"O setor com maior orçamento realizado é {setor_maior_orcamento}. "

    # Análise de receitas
    if any(palavra in pergunta for palavra in ['receita', 'arrecadação', 'fiscal']):
        receita_total = df_receitas['Valor'].sum()
        regiao_maior_receita = df_receitas.groupby('Região')['Valor'].sum().idxmax()
        
        resposta += f"A receita total é de {receita_total:,.2f} AOA. "
        resposta += f"A região com maior arrecadação é {regiao_maior_receita}. "

    # Análise de dívida
    if any(palavra in pergunta for palavra in ['dívida', 'juros', 'empréstimos']):
        divida_total = df_divida['Valor'].sum()
        taxa_media_juros = df_divida['Taxa_Juros'].mean() * 100
        
        resposta += f"A dívida total é de {divida_total:,.2f} AOA. "
        resposta += f"A taxa média de juros é de {taxa_media_juros:.1f}%. "

    # Análise de indicadores
    if any(palavra in pergunta for palavra in ['indicadores', 'economia', 'inflação', 'pib']):
        inflacao_media = df_indicadores['Inflação'].mean()
        variacao_pib = df_indicadores['PIB_Variação'].mean()
        
        resposta += f"A inflação média é de {inflacao_media:.1f}%. "
        resposta += f"A variação média do PIB é de {variacao_pib:.1f}%. "

    # Análise temporal
    if any(palavra in pergunta for palavra in ['evolução', 'tendência', 'variação']):
        ultima_inflacao = df_indicadores.iloc[-1]['Inflação']
        primeira_inflacao = df_indicadores.iloc[0]['Inflação']
        variacao_inflacao = ((ultima_inflacao / primeira_inflacao) - 1) * 100
        
        resposta += f"A inflação teve uma variação de {variacao_inflacao:.1f}% no período. "

    # Se nenhuma análise específica foi encontrada
    if not resposta:
        resposta = """
        Posso ajudar com análises sobre:
        - Execução orçamentária e gastos por setor
        - Receitas fiscais e arrecadação por região
        - Situação da dívida pública e juros
        - Indicadores econômicos (PIB, inflação, câmbio)
        - Tendências e evolução temporal dos dados
        
        Por favor, reformule sua pergunta usando algumas dessas palavras-chave.
        """
    
    return resposta

# Interface principal da aplicação
def main():
    # Configuração do título e estilo
    st.title("🇦🇴 Análise de Dados com GenAI - Ministério das Finanças de Angola")
    
    # Criação dos dados fictícios
    dfs = {
        'orcamento': criar_dados_orcamento(),
        'receitas': criar_dados_receitas(),
        'divida': criar_dados_divida(),
        'indicadores': criar_dados_indicadores()
    }
    
    # Barra lateral com o Assistente IA
    st.sidebar.title("💡 Assistente IA Financeiro")
    pergunta = st.sidebar.text_input(
        "Faça uma pergunta sobre os dados:",
        placeholder="Ex: Como está a execução orçamentária?"
    )
    
    if pergunta:
        resposta = analisar_dados_ia(pergunta, dfs)
        st.sidebar.markdown(f"**Resposta:**\n{resposta}")
    
    # Tabs para diferentes visões dos dados
    tab1, tab2, tab3, tab4 = st.tabs([
        "Execução Orçamentária", 
        "Receitas Fiscais", 
        "Dívida Pública",
        "Indicadores Econômicos"
    ])
    
    # Tab 1 - Execução Orçamentária
    with tab1:
        st.subheader("Análise da Execução Orçamentária")
        
        # Gráfico de execução por setor
        fig_orcamento = px.bar(
            dfs['orcamento'],
            x='Setor',
            y=['Orçamento_Planejado', 'Orçamento_Realizado'],
            title='Orçamento Planejado vs Realizado por Setor',
            barmode='group'
        )
        st.plotly_chart(fig_orcamento, use_container_width=True)
        
        # Tabela detalhada
        st.dataframe(dfs['orcamento'])
    
    # Tab 2 - Receitas Fiscais
    with tab2:
        st.subheader("Análise de Receitas Fiscais")
        
        # Gráfico de receitas por região
        fig_receitas = px.pie(
            dfs['receitas'].groupby('Região')['Valor'].sum().reset_index(),
            values='Valor',
            names='Região',
            title='Distribuição de Receitas por Região'
        )
        st.plotly_chart(fig_receitas, use_container_width=True)
        
        # Tabela detalhada
        st.dataframe(dfs['receitas'])
    
    # Tab 3 - Dívida Pública
    with tab3:
        st.subheader("Análise da Dívida Pública")
        
        # Gráfico de composição da dívida
        fig_divida = px.sunburst(
            dfs['divida'],
            path=['Tipo_Dívida', 'Categoria'],
            values='Valor',
            title='Composição da Dívida Pública'
        )
        st.plotly_chart(fig_divida, use_container_width=True)
        
        # Tabela detalhada
        st.dataframe(dfs['divida'])
    
    # Tab 4 - Indicadores Econômicos
    with tab4:
        st.subheader("Indicadores Econômicos")
        
        # Gráfico de linha temporal
        fig_indicadores = go.Figure()
        
        fig_indicadores.add_trace(go.Scatter(
            x=dfs['indicadores']['Data'],
            y=dfs['indicadores']['Inflação'],
            name='Inflação (%)'
        ))
        
        fig_indicadores.add_trace(go.Scatter(
            x=dfs['indicadores']['Data'],
            y=dfs['indicadores']['PIB_Variação'],
            name='Variação PIB (%)'
        ))
        
        fig_indicadores.update_layout(title='Evolução dos Indicadores Econômicos')
        st.plotly_chart(fig_indicadores, use_container_width=True)
        
        # Tabela detalhada
        st.dataframe(dfs['indicadores'])

if __name__ == "__main__":
    main()