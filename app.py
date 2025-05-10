import streamlit as st


# Page configuration
st.set_page_config(page_title="Work Vibes | Silvia", page_icon="💼", layout="wide")

# Sidebar
with st.sidebar:
    # Create a styled text logo
    st.markdown("""
    <div style="background: linear-gradient(45deg, #6c5ce7, #a29bfe); 
                padding: 20px; 
                border-radius: 10px; 
                text-align: center;
                margin-bottom: 20px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
        <h1 style="color: white; font-size: 28px; margin: 0;">Silvia Moreno Portillo</h1>
        <p style="color: white; font-size: 12px; margin-top: 10px;">Recursos Humanos, pero con H de Humanización</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("## Conéctate conmigo")
    
    # Social media links with icons
    st.markdown("""
    <div style="display: flex; justify-content: space-around; margin-top: 20px;">
        <a href="https://linkedin.com/in/yourprofile" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="40">
        </a>
        <a href="https://instagram.com/workvibesilvia" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/174/174855.png" width="40">
        </a>
        <a href="https://tiktok.com/@workvibesilvia" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/3116/3116491.png" width="40">
        </a>
        <a href="https://youtube.com/@workvibesilvia" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/1384/1384060.png" width="40">
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    # Additional links or text
    st.markdown("---")
    st.markdown("### Recursos y artículos")
    st.markdown("[📝 Mi Blog](#)")
    st.markdown("[📚 Recursos gratuitos](#)")

# Main content area - Banner
st.markdown("""
<div style="background: linear-gradient(to right, #a29bfe, #6c5ce7); 
            padding: 20px; 
            border-radius: 10px; 
            margin: 20px 0;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
    <h2 style="color: white; text-align: center; margin: 0;">Desarrollo del Talento & Bienestar Organizacional</h2>
    <p style="color: white; text-align: center; margin-top: 10px; font-size: 16px;">
        Construyendo entornos laborales más humanos, sostenibles y productivos
    </p>
</div>
""", unsafe_allow_html=True)

# Tabbed navigation
tab1, tab2, tab3 = st.tabs(["🙋‍♀️ Quién Soy", "💼 Experiencia Profesional", "🎓 Educación"])

# Content for "Quién Soy" tab
with tab1:
    st.header("Quién Soy")
    
    # Introduction - now in full width
    st.markdown("""
    <div style="background-color:#f0f2f6; padding:20px; border-radius:10px">
    <p style="font-size:18px;">
    Con experiencia en el diseño e implementación de estrategias de formación, 
    desarrollo del talento y bienestar organizacional.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Purpose section
    st.subheader("Mi Propósito")
    st.write("Humanizar las organizaciones, acompañando a personas y equipos a desplegar todo su potencial en entornos laborales sostenibles, conscientes y emocionalmente saludables.")
    
    # Approach section
    st.subheader("Mi Enfoque")
    st.write("Trabajo en la intersección entre cultura organizacional, employer branding y employee experience, ayudando a construir empresas más conectadas con sus valores, más humanas y, por tanto, más productivas.")
    
    st.info("Creo firmemente que cuando se cuida a las personas, los resultados llegan solos")

    # Services section - now in the main flow
    st.subheader("Servicios")
    
    # First service
    st.markdown("### 🌱 Formación con Propósito")
    st.markdown("""
    Diseño e imparto programas orientados al:
    - Crecimiento profesional
    - Liderazgo empático 
    - Compromiso de los equipos
    """)
    
    # Second service
    st.markdown("### ✨ Bienestar Organizacional")
    st.markdown("""
    Desarrollo acciones que impactan en:
    - Motivación
    - Retención del talento
    - Cultura corporativa
    """)

# Content for "Experiencia Profesional" tab
with tab2:
    st.header("Experiencia Profesional")
    
    # Using columns for a more professional layout
    with st.container():
        st.subheader("Especialista en formación")
        st.caption("Cámara de Comercio, Industria y Servicios de Madrid")
        st.markdown("Diseño e impartición de programas formativos orientados al desarrollo profesional.")
        st.markdown("---")
        
        st.subheader("Consultor de Talento y Empleabilidad")
        st.caption("Profesional independiente")
        st.markdown("Asesoramiento personalizado en estrategias de desarrollo profesional.")
        st.markdown("---")
        
        st.subheader("Responsable de equipo y Support Specialist")
        st.caption("Universidad Europea Online | Jornada completa · 4 años 4 meses")
        st.markdown("Coordinación de equipos y soporte especializado en entornos de educación online.")
        st.markdown("---")
        
        st.subheader("Especialista en formación")
        st.caption("Flou Oposiciones")
        st.markdown("Diseño e implementación de programas formativos específicos para oposiciones.")
        st.markdown("---")
        
        st.subheader("Consultor de empleo y Orientación Laboral")
        st.caption("Universidad Nebrija")
        st.markdown("Asesoramiento y orientación profesional a estudiantes y egresados universitarios.")

# Content for "Educación" tab
with tab3:
    st.header("Educación")
    
    with st.container():
        # Add your education information here
        st.subheader("Universidad / Título")
        st.caption("2010-2014")
        st.markdown("Descripción de tus estudios y especializaciones.")
        st.markdown("---")
        
        # Add more education entries as needed
        st.subheader("Certificaciones y Cursos Relevantes")
        st.markdown("• Certificación en Desarrollo de Talento")
        st.markdown("• Especialización en Bienestar Organizacional")
        st.markdown("• Curso de Liderazgo y Gestión de Equipos")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align:center; padding: 10px; color: #6c5ce7">
<p>© 2023 Silvia Moreno Portillo | Work Vibes</p>
</div>
""", unsafe_allow_html=True)