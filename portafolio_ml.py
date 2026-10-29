
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
