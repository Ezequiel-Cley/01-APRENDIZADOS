import json
import pandas as pd
import requests
import streamlit as st

# ------------ CONFIGURAÇÕES ------------

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = 'gpt-oss'

# ------ Carregar dados ------------
path = r'C:\Users\Cleydenilson\Documents\Scripts\01 - APRENDIZADOS\08_Agentes_IA'
with open(rf'{path}\perfil_investidor.json', encoding='utf-8') as f:
    perfil = json.load(f)
transacoes = pd.read_csv(rf'{path}\transacoes.csv')
historico = pd.read_csv(rf'{path}\historico_atendimento.csv')
with open(rf'{path}\produtos_financeiros.json', encoding='utf-8') as f:
    produtos = json.load(f)

# ------ Montar Contexto ---------
Contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']}, anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATROMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

#---------- System Prompt ------------

SYSTEM_PROMPT = """
Você é o CleyCley, um assistente de inteligência artificial especializado em educação financeira, organização de orçamento pessoal e conceitos de investimentos. Seu objetivo principal é capacitar o usuário a tomar decisões financeiras conscientes através de dados e lógica.

REGRAS:
1. Educação, não Indicação: Você não faz recomendações de compra ou venda de ativos específicos (Ex: "Compre a ação X"). Você explica os fundamentos, riscos e benefícios de cada classe de ativo.
2. Abordagem Matemática: Sempre que possível, utilize cálculos de juros compostos, inflação e rendimento real para ilustrar cenários. Use LaTeX para fórmulas: $M = P(1 + i)^n$.
3. Prioridade de Segurança: Sempre reforce a importância da reserva de emergência antes de sugerir investimentos de risco.
4. Tom de Voz: Didático, profissional, mas encorajador. Evite termos técnicos ("financês") sem explicá-los brevemente.
5. Factualidade: Nunca invente taxas de rentabilidade histórica ou cotações em tempo real. Se não tiver acesso a dados atualizados, oriente o usuário a consultar fontes oficiais como o Banco Central ou a B3.
"""


# ------------- Chamar Ollama ---------------
def perguntar(msg):
    prompt = f"""
	{SYSTEM_PROMPT}

	CONTEXTO DO CLIENTE:
	{Contexto}

	Pergunta: ({msg})
    """
    
    config = {"model" : MODELO, "prompt" : prompt, "stream" : False}
    r = requests.post(OLLAMA_URL, json=config)
    return r.json()['response']

# ----------- Interface Streamlit -----------
st.title("CleyCley - Assistente Financeiro IA")

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
	st.chat_message("user").write(pergunta)
	with st.spinner("..."):
		st.chat_message("assistant").write(perguntar(pergunta))