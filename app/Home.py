"""
2TFT Hub — Dashboard de Estatísticas e Meta-Análise
3====================================================
4Página inicial do hub de estatísticas de Teamfight Tactics.
5"""
6
7import streamlit as st
8
9# ---- Configuração da página ----
10st.set_page_config(
11    page_title="TFT Hub",
12    page_icon="🎮",
13    layout="wide",
14    initial_sidebar_state="expanded",
15)
16
17# ---- Cabeçalho ----
18st.title("🎮 TFT Hub")
19st.subheader("Hub de Estatísticas e Meta-Análise para Teamfight Tactics")
20
21st.markdown("---")
22
23# ---- Cards principais ----
24col1, col2, col3 = st.columns(3)
25
26with col1:
27    st.metric(
28        label="📊 Composições Meta",
29        value="Em breve",
30        delta="Fase de construção",
31    )
32
33with col2:
34    st.metric(
35        label="🔮 Augments",
36        value="Em breve",
37        delta="Fase de construção",
38    )
39
40with col3:
41    st.metric(
42        label="⚔️ Itens BIS",
43        value="Em breve",
44        delta="Fase de construção",
45    )
46
47st.markdown("---")
48
49# ---- Explicação do projeto ----
50st.markdown("""
51### 🚧 Projeto em Construção
52
53Este dashboard está sendo desenvolvido como um hub completo de estatísticas para TFT.
54
55**Funcionalidades planejadas:**
56- 📊 **Meta Comps** — Tier list de composições com win rate, pick rate e top4 rate
57- 🔮 **Augments** — Análise dos melhores augments por estágio e por comp
58- ⚔️ **Itens BIS** — Calculadora de melhores itens para cada campeão
59- 📈 **Explorador** — Ferramenta livre para explorar os dados
60
61**Fontes de dados:**
62- Riot Games API (oficial)
63- Scraping complementar de sites públicos de estatísticas
64
65**Etapa atual:** Fundação do projeto — estrutura, ambiente e coleta inicial de dados.
66""")
67
68# ---- Sidebar ----
69with st.sidebar:
70    st.header("⚙️ Configurações")
71    st.info("Filtros e configurações estarão disponíveis nas próximas etapas.")
72    st.markdown("---")
73    st.caption("TFT Hub v0.1.0 — Em desenvolvimento")
