import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Moral Machine Escolar", page_icon="🧠", layout="centered")

# --- ESTILOS PERSONALIZADOS (Mejoras visuales y control de tamaño) ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    /* Ajuste para que las imágenes no causen desborde vertical */
    .stImage > img { max-height: 220px; object-fit: cover; width: 100%; border-radius: 12px; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3.3em; font-weight: bold; margin-bottom: 8px; }
    .title { text-align: center; color: #1E3A8A; font-family: 'Helvetica Neue', sans-serif; }
    /* Pie de página elegante */
    .custom-footer {
        text-align: center;
        margin-top: 50px;
        padding-top: 20px;
        border-top: 1px solid #e2e8f0;
        color: #64748b;
        font-size: 0.85rem;
        font-family: 'Helvetica Neue', sans-serif;
        letter-spacing: 0.5px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🧠 Moral Machine Escolar")
st.subheader("Tus decisiones tienen consecuencias. ¿Qué camino vas a elegir?")
st.write("---")

# --- INICIALIZACIÓN DE ESTADOS ---
if 'paso' not in st.session_state:
    st.session_state.paso = 1
if 'ruta' not in st.session_state:
    st.session_state.ruta = None
if 'sub_ruta' not in st.session_state:
    st.session_state.sub_ruta = None

# --- PANTALLA DE INICIO / CONTEXTO ---
if st.session_state.paso == 1:
    # Nueva imagen de patio escolar optimizada en tamaño
    st.image("https://images.unsplash.com/photo-1577896851231-70ef18881754?auto=format&fit=crop&w=800&q=60", caption="El patio de la escuela puede cambiar con un solo acto.")
    
    st.info("""
    **Escenario Inicial:**
    Estás en el recreo y ves a Mateo rodeado de tres compañeros. Tienen el teléfono de Lucas, un chico tímido del aula. 
    Mateo está leyendo en voz alta y entre risas los mensajes privados que Lucas le envió a una chica que le gusta. 
    Lucas está rojo, con los ojos llorosos, intentando recuperar su teléfono sin éxito. El resto de la clase mira de reojo, pero nadie dice nada.
    """)
    
    st.markdown("### 🛑 PASO 1: Tu decisión como Espectador")
    
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
    st.markdown(f"## 🔀 Consecuencias de tu elección (Ruta {st.session_state.ruta})")
    
    if st.session_state.ruta == 'A':
        st.error("""
        **Lo que pasó:** Mateo se crece al ver que lo grabás. Empuja a Lucas al suelo para que el video sea 'más divertido'. El video se viraliza en el grupo de WhatsApp del colegio.
        
        *   **Impacto en Lucas (Víctima):** Sufre una crisis de ansiedad en el baño y falta a la escuela por 3 días.
        *   **Consecuencia para ti:** Dirección analiza el video. Aunque no empujaste, se demuestra que lo difundiste. Te suspenden por complicidad y ciberacoso.
        """)
        st.write("---")
        st.markdown("🔄 **El Director te llama a la oficina y te muestra el daño de Lucas. ¿Qué haces?**")
        if st.button("A.1: 'Solo era un chiste, Lucas es un exagerado'."):
            st.session_state.sub_ruta = 'A1'
            st.session_state.paso = 3
            st.rerun()
        if st.button("A.2: Asumes la responsabilidad, pides disculpas y aceptas la sanción."):
            st.session_state.sub_ruta = 'A2'
            st.session_state.paso = 3
            st.rerun()

    elif st.session_state.ruta == 'B':
        st.warning("""
        **Lo que pasó:** Como nadie frena a Mateo, la humillación dura todo el recreo. Todos aplicaron el 'Efecto Espectador' pensando que otro intervendría.
        
        *   **Impacto en Lucas (Víctima):** Se convence de que a nadie le importa. Baja sus notas y se aísla por completo.
        *   **Consecuencia para ti:** Una semana después, la profesora te pregunta en privado si viste algo raro con Lucas.
        """)
        st.write("---")
        st.markdown("🔄 **Estás a solas con la profesora. ¿Qué haces?**")
        if st.button("B.1: Callas por miedo a que Mateo se entere (Pacto de silencio)."):
            st.session_state.sub_ruta = 'B1'
            st.session_state.paso = 3
            st.rerun()
        if st.button("B.2: Rompes el silencio y le cuentas detalladamente lo que viste."):
            st.session_state.sub_ruta = 'B2'
            st.session_state.paso = 3
            st.rerun()

    elif st.session_state.ruta == 'C':
        st.success("""
        **Lo que pasó:** El grupo de Mateo se desarma. Al encontrar resistencia firme y pública, Mateo se ve expuesto, te dice 'qué amargado' pero le tira el teléfono a Lucas and se va.
        
        *   **Impacto en Lucas (Víctima):** Siente un alivio enorme. Sabe que no está solo en el aula.
        *   **Impacto en el entorno:** Otros compañeros se te acercan y dicen: 'Qué bueno que te plantaste, nosotros no nos animábamos'. Cambiaste la norma social del aula.
        """)
        st.write("---")
        st.markdown("🔄 **Lucas se queda llorando en el banco del patio. ¿Qué haces ahora?**")
        if st.button("C.1: Lo acompañas a la enfermería o a hablar con el tutor."):
            st.session_state.sub_ruta = 'C1'
            st.session_state.paso = 3
            st.rerun()
        if st.button("C.2: Te vas a jugar al fútbol, pensando que ya cumpliste tu parte."):
            st.session_state.sub_ruta = 'C2'
            st.session_state.paso = 3
            st.rerun()

# --- PANTALLA FINAL: METRICAS Y DEBRIEFING ---
elif st.session_state.paso == 3:
    st.markdown("## 📊 Evaluación de Impacto Psicológico")
    st.write("Este es el resultado medible de tus decisiones sobre el clima escolar:")

    desconexión = 100 if st.session_state.sub_ruta == 'A1' else (50 if st.session_state.sub_ruta == 'A2' else 10)
    autoeficacia = 95 if st.session_state.sub_ruta == 'C1' else (75 if st.session_state.sub_ruta == 'C2' else (40 if st.session_state.sub_ruta == 'B2' else 5))
    afrontamiento = "Asertivo y con Red de Apoyo" if 'C' in st.session_state.ruta else ("Pasivo / Aislamiento" if 'B' in st.session_state.ruta else "Indefensión Aguda")

    st.markdown(f"**Desconexión Moral (Agresor/Cómplice): {desconexión}%**")
    st.progress(desconexión / 100)
    
    st.markdown(f"**Autoeficacia para Intervenir (Tu nivel de acción): {autoeficacia}%**")
    st.progress(autoeficacia / 100)
    
    st.info(f"**Estado de Afrontamiento de la Víctima:** {afrontamiento}")

    st.write("---")
    st.markdown("### 📢 Mensaje Final para ti:")
    
    if 'A' in st.session_state.ruta:
        st.error("**Ruta del Reforzador:** Al reírte o grabar, validaste la violencia. En el acoso, quien aplaude o graba es tan responsable del daño como quien golpea o insulta. Las pantallas multiplican las consecuencias.")
    elif 'B' in st.session_state.ruta:
        st.warning("**Ruta del Espectador Pasivo:** Tu silencio le dio vía libre al acoso. La inacción no es neutral; es el combustible que permite que el bullying siga existiendo.")
    elif 'C' in st.session_state.ruta:
        st.success("**Ruta del Espectador Defensor:** ¡Excelente! Mostraste valentía moral. Los agresores dependen del silencio del entorno; al poner un límite, transformaste tu escuela en un lugar seguro.")

    with st.expander("❓ Preguntas para debatir en el aula"):
        st.markdown("""
        1. Al ver los resultados, ¿te diste cuenta de cómo una omisión (no hacer nada) puede doler tanto como un golpe?
        2. En las rutas A y B, ¿por qué creen que Lucas prefirió aislarse en lugar de pedir ayuda de inmediato?
        3. ¿Qué herramientas o seguridad necesita un alumno para pasar de la Ruta B (miedo) a la Ruta C (acción)?
        """)

    if st.button("🔄 Reiniciar Simulación"):
        st.session_state.paso = 1
        st.session_state.ruta = None
        st.session_state.sub_ruta = None
        st.rerun()

# --- PIE DE PÁGINA ELEGANTE (Al final de toda la App) ---
st.markdown('<div class="custom-footer">Recurso del Lic. Gustavo Almaras para encuentros en Colegios</div>', unsafe_allow_html=True)
