import streamlit as st

# Configuración de la página con diseño ancho para aprovechar el formato 16:9
st.set_page_config(page_title="Moral Machine Escolar", page_icon="🧠", layout="wide")

# --- ESTILOS PERSONALIZADOS (Compactación total para evitar scroll en 16:9) ---
st.markdown("""
    <style>
    /* Reducir los márgenes superiores por defecto de Streamlit */
    .block-container { padding-top: 1.5rem; padding-bottom: 1rem; max-width: 1200px; }
    .main { background-color: #f8f9fa; }
    
    /* Control estricto del tamaño de la imagen */
    .stImage > img { max-height: 240px; object-fit: cover; width: 100%; border-radius: 12px; }
    
    /* Botones más compactos y adaptativos */
    .stButton>button { width: 100%; border-radius: 8px; height: 3.2em; font-weight: bold; margin-bottom: 4px; }
    
    /* Pie de página elegante y pegado abajo sin forzar scroll */
    .custom-footer {
        text-align: center;
        margin-top: 25px;
        padding-top: 12px;
        border-top: 1px solid #e2e8f0;
        color: #64748b;
        font-size: 0.85rem;
        font-family: 'Helvetica Neue', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

# Título y subtítulo en una sola línea compacta
st.markdown("<h2 style='text-align: center; color: #1E3A8A; margin-bottom:0;'>🧠 Moral Machine Escolar</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #475569; margin-bottom: 15px;'>Tus decisiones tienen consecuencias. ¿Qué camino vas a elegir?</p>", unsafe_allow_html=True)

# --- INICIALIZACIÓN DE ESTADOS ---
if 'paso' not in st.session_state:
    st.session_state.paso = 1
if 'ruta' not in st.session_state:
    st.session_state.ruta = None
if 'sub_ruta' not in st.session_state:
    st.session_state.sub_ruta = None

# --- PANTALLA DE INICIO / CONTEXTO ---
if st.session_state.paso == 1:
    # Usamos dos columnas en PC: Izquierda para el caso e imagen, Derecha para los botones de acción
    col_izq, col_der = st.columns([1.1, 0.9], gap="large")
    
    with col_izq:
        st.image("https://images.unsplash.com/photo-1577896851231-70ef18881754?auto=format&fit=crop&w=800&q=60")
        st.info("""
        **Escenario Inicial:**
        Estás en el recreo y ves a Mateo rodeado de tres compañeros. Tienen el teléfono de Lucas, un chico tímido del aula. 
        Mateo lee en voz alta y entre risas los mensajes privados que Lucas le envió a una chica. Lucas está rojo, con los ojos llorosos, intentando recuperar su teléfono. El resto de la clase mira, pero nadie dice nada.
        """)
    
    with col_der:
        st.markdown("<h3 style='margin-top: 0;'>🛑 PASO 1: Tu decisión</h3>", unsafe_allow_html=True)
        st.write("Elige cómo vas a actuar como Espectador:")
        
        if st.button("📱 Opción A: Te da risa, te acercas a mirar y sacas tu teléfono para grabar."):
            st.session_state.ruta = 'A'
            st.session_state.paso = 2
            st.rerun()
            
        if st.button("🚶 Opción B: Te sientes incómodo, piensas 'no es mi problema' y te vas."):
            st.session_state.ruta = 'B'
            st.session_state.paso = 2
            st.rerun()
            
        if st.button("🛡️ Opción C: Te pones firme y le dices: 'Ya basta Mateo, devuélvele el teléfono'."):
            st.session_state.ruta = 'C'
            st.session_state.paso = 2
            st.rerun()

# --- PASO 2: CONSECUENCIAS Y SEGUNDA DECISIÓN ---
elif st.session_state.paso == 2:
    col_izq, col_der = st.columns([1.1, 0.9], gap="large")
    
    with col_izq:
        st.markdown(f"### 🔀 Consecuencias de tu elección (Ruta {st.session_state.ruta})")
        
        if st.session_state.ruta == 'A':
            st.error("""
            **Lo que pasó:** Mateo se crece al ver que grabás. Empuja a Lucas al suelo para el video. El archivo se viraliza en el grupo de WhatsApp antes de terminar el recreo.
            
            * **Impacto en Lucas:** Crisis de ansiedad. Falta a la escuela por 3 días.
            * **Para ti:** Dirección analiza el video. Aunque no empujaste, te suspenden por complicidad y ciberacoso.
            """)
        elif st.session_state.ruta == 'B':
            st.warning("""
            **Lo que pasó:** Como nadie frena a Mateo, la humillación dura todo el recreo. Todos aplicaron el 'Efecto Espectador' pensando que otro intervendría.
            
            * **Impacto en Lucas:** Se convence de que a nadie le importa. Baja sus notas y se aísla.
            * **Para ti:** Una semana después, la profesora te pregunta en privado si viste algo.
            """)
        elif st.session_state.ruta == 'C':
            st.success("""
            **Lo que pasó:** Al encontrar resistencia firme y pública, Mateo se ve expuesto. Te dice 'qué amargado' pero le tira el teléfono a Lucas y se va.
            
            * **Impacto en Lucas:** Siente un alivio enorme. Sabe que no está solo.
            * **Impacto en el entorno:** Otros dicen: 'Qué bueno que te plantaste, nosotros no nos animábamos'. Cambiaste la norma del aula.
            """)
            
    with col_der:
        st.markdown("### 🔄 Siguiente decisión")
        
        if st.session_state.ruta == 'A':
            st.write("El Director te muestra el daño de Lucas. ¿Qué haces?")
            if st.button("A.1: 'Solo era un chiste, Lucas es un exagerado'."):
                st.session_state.sub_ruta = 'A1'
                st.session_state.paso = 3
                st.rerun()
            if st.button("A.2: Asumes la responsabilidad y aceptas la sanción."):
                st.session_state.sub_ruta = 'A2'
                st.session_state.paso = 3
                st.rerun()
        elif st.session_state.ruta == 'B':
            st.write("Estás a solas con la profesora. ¿Qué haces?")
            if st.button("B.1: Callas por miedo a represalias (Pacto de silencio)."):
                st.session_state.sub_ruta = 'B1'
                st.session_state.paso = 3
                st.rerun()
            if st.button("B.2: Rompes el silencio y cuentas lo que viste."):
                st.session_state.sub_ruta = 'B2'
                st.session_state.paso = 3
                st.rerun()
        elif st.session_state.ruta == 'C':
            st.write("Lucas se queda llorando en el banco del patio. ¿Qué haces?")
            if st.button("C.1: Lo acompañas a la enfermería o a hablar con el tutor."):
                st.session_state.sub_ruta = 'C1'
                st.session_state.paso = 3
                st.rerun()
            if st.button("C.2: Te vas a jugar al fútbol, ya cumpliste tu parte."):
                st.session_state.sub_ruta = 'C2'
                st.session_state.paso = 3
                st.rerun()

# --- PANTALLA FINAL: METRICAS Y DEBRIEFING ---
elif st.session_state.paso == 3:
    col_izq, col_der = st.columns([1.1, 0.9], gap="large")
    
    with col_izq:
        st.markdown("### 📊 Evaluación de Impacto Psicológico")
        
        desconexión = 100 if st.session_state.sub_ruta == 'A1' else (50 if st.session_state.sub_ruta == 'A2' else 10)
        autoeficacia = 95 if st.session_state.sub_ruta == 'C1' else (75 if st.session_state.sub_ruta == 'C2' else (40 if st.session_state.sub_ruta == 'B2' else 5))
        afrontamiento = "Asertivo y con Red de Apoyo" if 'C' in st.session_state.ruta else ("Pasivo / Aislamiento" if 'B' in st.session_state.ruta else "Indefensión Aguda")

        st.markdown(f"**Desconexión Moral (Agresor/Cómplice): {desconexión}%**")
        st.progress(desconexión / 100)
        
        st.markdown(f"**Autoeficacia para Intervenir: {autoeficacia}%**")
        st.progress(autoeficacia / 100)
        
        st.info(f"**Estado de la Víctima:** {afrontamiento}")
        
    with col_der:
        st.markdown("### 📢 Reflexión Final")
        
        if 'A' in st.session_state.ruta:
            st.error("Al grabar o reírte, validaste la violencia. Quien aplaude es tan responsable como quien agrede.")
        elif 'B' in st.session_state.ruta:
            st.warning("Tu silencio dio vía libre al acoso. La inacción es el combustible que permite que el bullying exista.")
        elif 'C' in st.session_state.ruta:
            st.success("¡Excelente! Mostraste valentía moral. Al poner un límite, transformaste tu escuela en un lugar seguro.")

        with st.expander("❓ Preguntas para debate"):
            st.markdown("""
            * ¿Cómo una omisión puede doler tanto como un golpe?
            * ¿Por qué la víctima prefiere aislarse antes que pedir ayuda?
            """)

        if st.button("🔄 Reiniciar Simulación"):
            st.session_state.paso = 1
            st.session_state.ruta = None
            st.session_state.sub_ruta = None
            st.rerun()

# --- PIE DE PÁGINA ELEGANTE ---
st.markdown('<div class="custom-footer">Recurso del Lic. Gustavo Almaras para encuentros en Colegios</div>', unsafe_allow_html=True)
