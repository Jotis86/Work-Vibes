import streamlit as st


st.set_page_config(page_title="Work Vibes | Silvia", page_icon="💼", layout="wide")

# Header section with custom styling
st.title("💫 Recursos Humanos, pero con H de Humanización")
st.markdown("---")

# Add this code near the top of your [app.py](app.py) file (after the imports)
# Sidebar
with st.sidebar:
    # Use a reliable online HR image
    st.image("https://images.unsplash.com/photo-1552664730-d307ca884978?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80", 
             caption="Silvia")
    
    st.markdown("## Conéctate conmigo")
    
    # Social media links with icons
    st.markdown("""
    <div style="display: flex; justify-content: space-around; margin-top: 20px;">
        <a href="https://linkedin.com/in/yourprofile" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="40">
        </a>
        <a href="https://twitter.com/workvibesilvia" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/733/733579.png" width="40">
        </a>
        <a href="https://instagram.com/workvibesilvia" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/174/174855.png" width="40">
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    # Additional links or text
    st.markdown("---")
    st.markdown("### Recursos y artículos")
    st.markdown("[📝 Mi Blog](#)")
    st.markdown("[📚 Recursos gratuitos](#)")

# Introduction in a highlighted container
with st.container():
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        <div style="background-color:#f0f2f6; padding:20px; border-radius:10px">
        <p style="font-size:18px; font-style:italic">
        Con experiencia en el diseño e implementación de estrategias de formación, 
        desarrollo del talento y bienestar organizacional.</p>
        </div>
        """, unsafe_allow_html=True)

# Mission statement
st.header("Mi Propósito")
st.write("Humanizar las organizaciones, acompañando a personas y equipos a desplegar todo su potencial en entornos laborales sostenibles, conscientes y emocionalmente saludables.")

# Areas of expertise
st.header("Mi Enfoque")
st.write("Trabajo en la intersección entre cultura organizacional, employer branding y employee experience, ayudando a construir empresas más conectadas con sus valores, más humanas y, por tanto, más productivas.")

st.info("Creo firmemente que cuando se cuida a las personas, los resultados llegan solos")

# Services with visual improvements
st.header("Servicios")
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🌱 Formación con Propósito")
    st.markdown("""
    Diseño e imparto programas orientados al:
    - Crecimiento profesional
    - Liderazgo empático 
    - Compromiso de los equipos
    """)
    
    st.markdown("### 🧭 Orientación Laboral")
    st.markdown("""
    Acompaño procesos de orientación y transformación profesional desde una perspectiva individualizada y consciente.
    """)

with col2:
    st.markdown("### ✨ Bienestar Organizacional")
    st.markdown("""
    Desarrollo acciones que impactan directamente en:
    - Motivación
    - Retención del talento
    - Cultura corporativa
    """)

# Social media footer
st.markdown("---")
st.markdown("""
<div style="text-align:center">
<p>📲 También comparto recursos, reflexiones y herramientas en mis redes como 
<span style="font-weight:bold; color:#FF4B4B">@workvibesilvia</span></p>
<p>Bienestar | Talento | Humanización del trabajo | Tips para encontrar empleo</p>
</div>
""", unsafe_allow_html=True)

# Add a contact button
st.button("Contáctame", use_container_width=True)