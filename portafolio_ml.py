from pathlib import Path
import streamlit as st

st.set_page_config(page_title="Portafolio | Machine Learning e IA", page_icon="✦", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');
:root{--navy:#171B35;--navy2:#30345F;--purple:#7567D8;--lav:#EAE8FF;--orange:#FFAA72;--paper:#F7F7FC;--ink:#252943;--muted:#747A93;--line:#E7E7F0}
html,body,[class*="css"]{font-family:'DM Sans',sans-serif}.stApp{background:var(--paper);color:var(--ink)}
[data-testid="stHeader"]{background:rgba(247,247,252,.92)}.block-container{max-width:1400px;padding-top:1.5rem;padding-bottom:3rem}
[data-testid="stSidebar"]{background:var(--navy)}[data-testid="stSidebar"] *{color:#F4F3FF}
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p{color:#BFC2DD}[data-testid="stSidebar"] hr{border-color:#444968}
.brand{display:flex;align-items:center;gap:12px;margin:.4rem 0 2rem}.brand-icon{width:45px;height:45px;border-radius:15px;background:var(--orange);color:var(--navy);display:flex;align-items:center;justify-content:center;font-size:25px;font-weight:700}
.brand-name{font:700 19px 'Space Grotesk',sans-serif}.brand-sub{font-size:9px;letter-spacing:1.8px;color:#BFC2DD;margin-top:2px}
.hero{position:relative;overflow:hidden;background:linear-gradient(115deg,var(--navy),var(--navy2));color:white;padding:36px 38px;border-radius:25px;margin-bottom:24px;box-shadow:0 14px 32px #171b3520}
.hero:after{content:"";position:absolute;width:270px;height:270px;border:1px solid #ffaa7266;border-radius:50%;right:-65px;top:-125px;box-shadow:0 0 0 30px #ffaa720d,0 0 0 65px #ffaa7209}
.kicker{font-size:10px;letter-spacing:2.2px;font-weight:700;color:var(--orange);margin-bottom:13px}.hero-title{font:700 clamp(29px,3.5vw,43px) 'Space Grotesk',sans-serif;letter-spacing:-1.5px;line-height:1.1;max-width:760px}
.hero-copy{color:#D4D6EA;font-size:14px;line-height:1.7;max-width:700px;margin-top:13px}.hero-pill{display:inline-block;margin-top:20px;padding:8px 11px;border:1px solid #ffaa724d;border-radius:8px;background:#ffaa721f;color:#FFD1B2;font-size:10px;font-weight:700;letter-spacing:.8px}
.section-title{font:700 20px 'Space Grotesk',sans-serif;color:var(--navy);margin-bottom:4px}.section-copy{font-size:13px;color:var(--muted);margin-bottom:15px}
.stat{background:white;border:1px solid var(--line);border-radius:15px;padding:15px 18px;min-height:90px}.stat-label{font-size:10px;color:#8589A0;letter-spacing:1.2px;font-weight:700}.stat-value{font:700 25px 'Space Grotesk',sans-serif;color:var(--navy);margin-top:7px}
.portfolio-card{background:white;border:1px solid var(--line);border-radius:17px;padding:19px;min-height:205px;box-shadow:0 5px 16px #1e204208;margin-bottom:15px}
.card-top{display:flex;align-items:center;gap:11px;margin-bottom:13px}.card-icon{width:43px;height:43px;border-radius:13px;background:var(--lav);color:var(--purple);display:flex;align-items:center;justify-content:center;font-size:20px;flex-shrink:0}
.card-category{font-size:9px;letter-spacing:1.25px;color:#898BA2;font-weight:700;text-transform:uppercase}.card-title{font:700 16px 'Space Grotesk',sans-serif;color:var(--navy);line-height:1.25;margin-top:3px}
.card-desc{font-size:12px;color:var(--muted);line-height:1.55;min-height:55px;margin-bottom:13px}.card-link{display:inline-block;color:var(--purple);font-size:12px;font-weight:700;text-decoration:none;border-bottom:1px solid #D8D3FF;padding-bottom:3px}.card-link:hover{color:#5145B5;border-color:#5145B5}
.resource{background:white;border:1px solid var(--line);border-radius:15px;padding:18px 20px;margin:16px 0 22px}.resource-title{font:700 15px 'Space Grotesk',sans-serif;color:var(--navy);margin-bottom:5px}.resource-copy{font-size:12px;color:var(--muted);line-height:1.6;margin-bottom:12px}
.footer{text-align:center;color:#999DB0;font-size:10px;letter-spacing:.8px;margin-top:30px}
div[data-testid="stTextInput"] input,div[data-testid="stSelectbox"] div[data-baseweb="select"]{border-radius:10px!important;border-color:#DFDFEC!important}
@media(max-width:700px){.block-container{padding:1rem .85rem 2rem}.hero{padding:25px 21px;border-radius:19px}}
</style>
""", unsafe_allow_html=True)

APPS = [{'title': 'Lenguaje natural', 'category': 'NLP', 'desc': 'Procesamiento del lenguaje natural y ejercicios interactivos.', 'url': 'https://lenguajenatural-5agf8clgqxasfwcxdstrya.streamlit.app/', 'icon': '✎'}, {'title': 'Espacio vectorial', 'category': 'Machine Learning', 'desc': 'Explora conceptos de espacios vectoriales.', 'url': 'https://espaciovectorial-amq5zcpjwhpermxfchtzwd.streamlit.app/', 'icon': '⌁'}, {'title': 'Texto a audio', 'category': 'Audio e IA', 'desc': 'Convierte contenido escrito en audio.', 'url': 'https://apptextoaudio-ahdvkb5oupjqmtndwusuvc.streamlit.app/', 'icon': '♫'}, {'title': 'Traductor de audio', 'category': 'Audio e IA', 'desc': 'Herramienta de traducción orientada a contenido de audio.', 'url': 'https://apptraductoraudio-jymgkbwhjvczkjxqkq7zkf.streamlit.app/', 'icon': '⇄'}, {'title': 'RNN — Consumo', 'category': 'Redes neuronales', 'desc': 'Red neuronal recurrente aplicada al análisis de consumo.', 'url': 'https://rnnconsumo-dpodv8uqz6vhhwjmzsuya9.streamlit.app/', 'icon': '⌁'}, {'title': 'LSTM para NLP', 'category': 'Redes neuronales', 'desc': 'Modelo LSTM para tareas de procesamiento del lenguaje.', 'url': 'https://lstmnlp-yugcmgvvp7pozbgijcqhbc.streamlit.app/', 'icon': '⟲'}, {'title': 'Visión computacional', 'category': 'Visión artificial', 'desc': 'Explora técnicas de visión computacional.', 'url': 'https://visioncomputacional-tm.streamlit.app/', 'icon': '◎'}, {'title': 'Detección con YOLOv5', 'category': 'Visión artificial', 'desc': 'Detección visual de objetos con YOLOv5.', 'url': 'https://appyolov5-czcwaaeevbjrvw6uegq4bp.streamlit.app/', 'icon': '◉'}, {'title': 'Aplicación multipágina', 'category': 'Streamlit', 'desc': 'Ejemplo de una aplicación organizada en varias páginas.', 'url': 'https://multipagina-elkyyc8kzxg3fnkrc29zcj.streamlit.app/', 'icon': '▦'}, {'title': 'Visión con profesor', 'category': 'Visión artificial', 'desc': 'Proyecto de análisis visual guiado.', 'url': 'https://visioncomprofe-7islmhqepsxupk2ttplezd.streamlit.app/', 'icon': '◈'}, {'title': 'Chat con PDF', 'category': 'IA generativa', 'desc': 'Consulta documentos PDF mediante una interfaz conversacional.', 'url': 'https://chatpdf-khf8kcmvz3g2dqsvvwnbb5.streamlit.app/', 'icon': '▤'}, {'title': 'Prueba Streamlit — KNN', 'category': 'Machine Learning', 'desc': 'Clasificación de datos con K-Nearest Neighbors.', 'url': 'https://machinelearning-wykpjd5xmsfqqvb6zpypep.streamlit.app/', 'icon': '✣'}, {'title': 'Consumo eléctrico', 'category': 'Predicción', 'desc': 'Ejercicio de análisis y regulación del consumo eléctrico.', 'url': 'https://appconsumoenergia.streamlit.app/', 'icon': 'ϟ'}, {'title': 'Neurona artificial', 'category': 'Redes neuronales', 'desc': 'Visualiza la suma de neuronas y sus funciones de activación.', 'url': 'https://neuronaartificialapp-ysvid6optnptwfsjynfzpa.streamlit.app/', 'icon': '✳'}, {'title': 'Regresión logística / K-Means', 'category': 'Machine Learning', 'desc': 'Proyecto de clasificación y agrupamiento de datos.', 'url': 'https://santiagoappseguros.streamlit.app/', 'icon': '⌖'}, {'title': 'Árboles de decisión', 'category': 'Machine Learning', 'desc': 'Explora cómo un árbol de decisión divide datos.', 'url': 'https://arboldedecision-fqqvqqt3xu7eovbgetngs4.streamlit.app/', 'icon': '⑂'}, {'title': 'Algoritmos de clasificación', 'category': 'Machine Learning', 'desc': 'Ejercicio interactivo sobre reglas de clasificación.', 'url': 'https://clasificadorapp.streamlit.app/', 'icon': '⟐'}, {'title': 'Medidor de energía', 'category': 'IoT y energía', 'desc': 'Aplicación práctica de medición de energía.', 'url': 'https://medidordeenergia-ckh2webpsnpldwujpjsf6f.streamlit.app/', 'icon': 'ϟ'}]

with st.sidebar:
    st.markdown("<div class='brand'><div class='brand-icon'>✦</div><div><div class='brand-name'>ML Portfolio</div><div class='brand-sub'>LEARNING · DATA · AI</div></div></div>", unsafe_allow_html=True)
    st.markdown("### Explora el portafolio")
    st.caption("Proyectos y aplicaciones prácticas de Machine Learning e Inteligencia Artificial.")
    st.divider()
    st.markdown("**Tecnologías**")
    st.caption("Python · Streamlit · ML · NLP · IA")

st.markdown("""
<div class="hero">
 <div class="kicker">✦ &nbsp; PORTAFOLIO INTERACTIVO</div>
 <div class="hero-title">Aplicaciones de Machine Learning e Inteligencia Artificial.</div>
 <div class="hero-copy">Un espacio para explorar proyectos, experimentar con modelos y conectar conceptos de ciencia de datos con aplicaciones prácticas.</div>
 <div class="hero-pill">18 PROYECTOS · EXPLORA, PRUEBA Y APRENDE</div>
</div>""", unsafe_allow_html=True)

st.markdown("""<div class="resource"><div class="resource-title">Biblioteca de páginas y ejercicios</div>
<div class="resource-copy">Material complementario para profundizar en aplicaciones de IA y ejercicios prácticos.</div>
<a class="card-link" href="https://sites.google.com/view/aplicacionesdeia/inicio" target="_blank" rel="noopener noreferrer">Explorar recursos externos ↗</a></div>""", unsafe_allow_html=True)

st.markdown('<div class="section-title">Explora los proyectos</div><div class="section-copy">Abre cada aplicación en una pestaña nueva o filtra por tema.</div>', unsafe_allow_html=True)
f1,f2=st.columns([1.5,1])
with f1: search=st.text_input("Buscar",placeholder="Ej.: visión, audio, redes neuronales…",label_visibility="collapsed")
with f2: category=st.selectbox("Categoría",["Todas"]+sorted({a["category"] for a in APPS}),label_visibility="collapsed")
filtered=[a for a in APPS if (category=="Todas" or a["category"]==category) and search.lower().strip() in (a["title"]+" "+a["category"]+" "+a["desc"]).lower()]

c1,c2,c3=st.columns(3)
for col,label,value in [(c1,"PROYECTOS",len(APPS)),(c2,"CATEGORÍAS",len({a["category"] for a in APPS})),(c3,"RESULTADOS",len(filtered))]:
    with col: st.markdown(f'<div class="stat"><div class="stat-label">{label}</div><div class="stat-value">{value}</div></div>',unsafe_allow_html=True)
st.write("")
if not filtered: st.info("No hay proyectos que coincidan. Prueba otro término o categoría.")
else:
    cols=st.columns(3,gap="medium")
    for i,app in enumerate(filtered):
        with cols[i%3]:
            st.markdown(f'<div class="portfolio-card"><div class="card-top"><div class="card-icon">{app["icon"]}</div><div><div class="card-category">{app["category"]}</div><div class="card-title">{app["title"]}</div></div></div><div class="card-desc">{app["desc"]}</div><a class="card-link" href="{app["url"]}" target="_blank" rel="noopener noreferrer">Abrir aplicación ↗</a></div>',unsafe_allow_html=True)

st.markdown('<div class="footer">ML PORTFOLIO · MACHINE LEARNING · ARTIFICIAL INTELLIGENCE</div>',unsafe_allow_html=True)
