import streamlit as st

# Page configuration
st.set_page_config(page_title="Work Vibes | Silvia", page_icon="💼", layout="wide")

# Custom CSS for light/dark mode compatibility and better styling
st.markdown("""
<style>
    /* Custom fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    /* General styling */
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    /* Headings */
    h1, h2, h3, h4 {
        font-weight: 600 !important;
    }
    
    /* Cards and containers */
    .card {
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
    }
    
    /* Service cards */
    .service-card {
        border-left: 4px solid #a29bfe;
        background-color: rgba(162, 155, 254, 0.1);
        padding: 1rem;
        border-radius: 0 10px 10px 0;
        margin-bottom: 1rem;
    }
    
    /* Experience timeline */
    .timeline-item {
        border-left: 2px solid #6c5ce7;
        padding-left: 20px;
        position: relative;
        margin-bottom: 30px;
    }
    
    .timeline-item::before {
        content: "";
        position: absolute;
        left: -9px;
        top: 0;
        width: 16px;
        height: 16px;
        border-radius: 50%;
        background: #6c5ce7;
    }
    
    /* Social media icons */
    .social-icons a {
        transition: transform 0.3s ease;
        display: inline-block;
    }
    
    .social-icons a:hover {
        transform: scale(1.2);
    }
    
    /* Button styling */
    .custom-button {
        background: linear-gradient(45deg, #6c5ce7, #a29bfe);
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 30px;
        font-weight: 500;
        cursor: pointer;
        transition: all 0.3s ease;
        display: inline-block;
        text-decoration: none;
        margin-top: 10px;
    }
    
    .custom-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 5px 15px rgba(108, 92, 231, 0.4);
    }
    
    /* Light/dark mode adaptations */
    @media (prefers-color-scheme: dark) {
        .light-bg {
            background-color: #2d2d2d !important;
            color: #f0f0f0 !important;
        }
        .subtle-bg {
            background-color: #3a3a3a !important;
            color: #f0f0f0 !important;
        }
    }
    
    @media (prefers-color-scheme: light) {
        .light-bg {
            background-color: #f9f9f9 !important;
            color: #333 !important;
        }
        .subtle-bg {
            background-color: #f0f2f6 !important;
            color: #333 !important;
        }
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    # Create a styled text logo
    st.markdown("""
    <div style="background: linear-gradient(45deg, #6c5ce7, #a29bfe); 
                padding: 25px; 
                border-radius: 15px; 
                text-align: center;
                margin-bottom: 30px;
                box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);">
        <h1 style="color: white; font-size: 28px; margin: 0; letter-spacing: 0.5px;">Silvia Moreno Portillo</h1>
        <p style="color: white; font-size: 14px; margin-top: 10px; opacity: 0.9;">Recursos Humanos, pero con H de Humanización</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h3 style='text-align: center; margin-bottom: 20px;'>Conéctate conmigo</h3>", unsafe_allow_html=True)
    
    # Social media links with icons and enhanced styling
    st.markdown("""
    <div class="social-icons" style="display: flex; justify-content: space-around; margin: 25px 0;">
        <a href="https://www.linkedin.com/in/silvia-moreno-portillo/" target="_blank" title="LinkedIn">
            <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="40">
        </a>
        <a href="https://www.instagram.com/workvibesilvia/" target="_blank" title="Instagram">
            <img src="https://cdn-icons-png.flaticon.com/512/174/174855.png" width="40">
        </a>
        <a href="https://www.tiktok.com/@workvibesilvia" target="_blank" title="TikTok">
            <img src="https://cdn-icons-png.flaticon.com/512/3116/3116491.png" width="40">
        </a>
        <a href="https://www.youtube.com/@workvibesilvia" target="_blank" title="YouTube">
            <img src="https://cdn-icons-png.flaticon.com/512/1384/1384060.png" width="40">
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    # Additional links with improved styling
    st.markdown("<hr style='margin: 30px 0; opacity: 0.3;'>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; margin-bottom: 20px;'>Recursos y artículos</h3>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style="display: flex; flex-direction: column; gap: 15px;">
        <a href="#" class="custom-button" style="text-align: center;">
            <span>📝 Mi Blog</span>
        </a>
        <a href="#" class="custom-button" style="text-align: center;">
            <span>📚 Recursos gratuitos</span>
        </a>
    </div>
    """, unsafe_allow_html=True)

# Main content area - Enhanced Banner
st.markdown("""
<div style="background: linear-gradient(to right, #a29bfe, #6c5ce7); 
            padding: 30px; 
            border-radius: 15px; 
            margin: 20px 0 40px 0;
            box-shadow: 0 10px 30px rgba(108, 92, 231, 0.3);">
    <h2 style="color: white; text-align: center; margin: 0; font-size: 32px; letter-spacing: 1px;">
        Desarrollo del Talento & Bienestar Organizacional
    </h2>
    <p style="color: white; text-align: center; margin-top: 15px; font-size: 18px; max-width: 800px; margin-left: auto; margin-right: auto; line-height: 1.6; opacity: 0.9;">
        Construyendo entornos laborales más humanos, sostenibles y productivos
    </p>
</div>
""", unsafe_allow_html=True)

# Tabbed navigation with enhanced styling
tab1, tab2, tab3 = st.tabs(["🙋‍♀️ Quién Soy", "💼 Experiencia Profesional", "🎓 Educación"])

# Content for "Quién Soy" tab with enhanced styling
with tab1:
    st.markdown("<h2 style='margin-bottom: 30px; margin-top: 20px;'>Quién Soy</h2>", unsafe_allow_html=True)
    
    # Introduction with enhanced styling
    st.markdown("""
    <div class="card subtle-bg" style="margin-bottom: 30px;">
        <p style="font-size: 18px; line-height: 1.6;">
        Con experiencia en el diseño e implementación de estrategias de formación, 
        desarrollo del talento y bienestar organizacional. Mi enfoque combina
        la psicología organizacional con métodos innovadores para crear culturas 
        de trabajo más humanas y efectivas.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Purpose section with enhanced styling
    st.markdown("<h3 style='margin-top: 30px; margin-bottom: 15px;'>Mi Propósito</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div style="padding: 0 5px; margin-bottom: 30px;">
        <p style="font-size: 16px; line-height: 1.7;">
            Humanizar las organizaciones, acompañando a personas y equipos a desplegar todo su potencial 
            en entornos laborales sostenibles, conscientes y emocionalmente saludables. Busco transformar
            la relación entre personas y empresas hacia modelos más equilibrados y satisfactorios para todos.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Approach section with enhanced styling
    st.markdown("<h3 style='margin-top: 30px; margin-bottom: 15px;'>Mi Enfoque</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div style="padding: 0 5px; margin-bottom: 30px;">
        <p style="font-size: 16px; line-height: 1.7;">
            Trabajo en la intersección entre cultura organizacional, employer branding y employee experience, 
            ayudando a construir empresas más conectadas con sus valores, más humanas y, por tanto, más productivas.
            Cada organización es única, por lo que diseño soluciones personalizadas basadas en evidencia y buenas prácticas.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Quote with enhanced styling
    st.markdown("""
    <div style="background: linear-gradient(to right, rgba(162, 155, 254, 0.2), rgba(108, 92, 231, 0.2)); 
                padding: 25px; 
                border-radius: 10px; 
                margin: 30px 0;
                border-left: 5px solid #6c5ce7;
                font-style: italic;
                text-align: center;">
        <p style="font-size: 18px; line-height: 1.7; margin: 0;">
            "Creo firmemente que cuando se cuida a las personas, los resultados llegan solos"
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Services section with enhanced styling
    st.markdown("<h3 style='margin-top: 40px; margin-bottom: 25px;'>Servicios</h3>", unsafe_allow_html=True)
    
    # First service with enhanced styling
    st.markdown("""
    <div class="service-card">
        <h4 style="color: #6c5ce7; margin-top: 0;">🌱 Formación con Propósito</h4>
        <p style="margin-bottom: 10px;">Diseño e imparto programas orientados al:</p>
        <ul style="margin-bottom: 0;">
            <li>Crecimiento profesional y desarrollo de habilidades</li>
            <li>Liderazgo empático y gestión de equipos diversos</li>
            <li>Compromiso de los equipos y cultura organizacional</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Second service with enhanced styling
    st.markdown("""
    <div class="service-card">
        <h4 style="color: #6c5ce7; margin-top: 0;">✨ Bienestar Organizacional</h4>
        <p style="margin-bottom: 10px;">Desarrollo acciones que impactan en:</p>
        <ul style="margin-bottom: 0;">
            <li>Motivación y satisfacción en el entorno laboral</li>
            <li>Retención del talento y employer branding</li>
            <li>Cultura corporativa y valores organizacionales</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Content for "Experiencia Profesional" tab with enhanced styling
with tab2:
    st.markdown("<h2 style='margin-bottom: 30px; margin-top: 20px;'>Experiencia Profesional</h2>", unsafe_allow_html=True)
    
    # Timeline with enhanced styling
    st.markdown("""
    <div class="timeline-item">
        <h3 style="margin: 0;">Especialista en formación</h3>
        <p style="color: #6c5ce7; font-weight: 500; margin: 5px 0;">Cámara de Comercio, Industria y Servicios de Madrid</p>
        <p style="margin-top: 10px;">
            Diseño e impartición de programas formativos orientados al desarrollo profesional, con foco en competencias clave para el mercado laboral actual.
        </p>
    </div>
    
    <div class="timeline-item">
        <h3 style="margin: 0;">Consultor de Talento y Empleabilidad</h3>
        <p style="color: #6c5ce7; font-weight: 500; margin: 5px 0;">Profesional independiente</p>
        <p style="margin-top: 10px;">
            Asesoramiento personalizado en estrategias de desarrollo profesional y planes de carrera adaptados a las necesidades individuales.
        </p>
    </div>
    
    <div class="timeline-item">
        <h3 style="margin: 0;">Responsable de equipo y Support Specialist</h3>
        <p style="color: #6c5ce7; font-weight: 500; margin: 5px 0;">Universidad Europea Online | Jornada completa · 4 años 4 meses</p>
        <p style="margin-top: 10px;">
            Coordinación de equipos y soporte especializado en entornos de educación online, diseñando estrategias de aprendizaje efectivas y gestionando el desarrollo de talento interno.
        </p>
    </div>
    
    <div class="timeline-item">
        <h3 style="margin: 0;">Especialista en formación</h3>
        <p style="color: #6c5ce7; font-weight: 500; margin: 5px 0;">Flou Oposiciones</p>
        <p style="margin-top: 10px;">
            Diseño e implementación de programas formativos específicos para oposiciones, con énfasis en técnicas de estudio y gestión del estrés.
        </p>
    </div>
    
    <div class="timeline-item">
        <h3 style="margin: 0;">Consultor de empleo y Orientación Laboral</h3>
        <p style="color: #6c5ce7; font-weight: 500; margin: 5px 0;">Universidad Nebrija</p>
        <p style="margin-top: 10px;">
            Asesoramiento y orientación profesional a estudiantes y egresados universitarios, desarrollando programas de inserción laboral y competencias transversales.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Content for "Educación" tab with enhanced styling
with tab3:
    st.markdown("<h2 style='margin-bottom: 30px; margin-top: 20px;'>Educación</h2>", unsafe_allow_html=True)
    
    # Education cards with enhanced styling
    st.markdown("""
    <div class="card light-bg">
        <h3 style="margin-top: 0; color: #6c5ce7;">Master en Dirección de Recursos Humanos y Gestión del Talento</h3>
        <p style="font-weight: 500; margin: 5px 0 15px 0;">ENEB - Escuela de Negocios Europea de Barcelona | sept. 2024</p>
        <p>Especialización en estrategias avanzadas de gestión del talento, bienestar organizacional y nuevos modelos de trabajo.</p>
    </div>
    
    <div class="card light-bg">
        <h3 style="margin-top: 0; color: #6c5ce7;">Máster en Psicopedagogía y orientación laboral</h3>
        <p style="font-weight: 500; margin: 5px 0 15px 0;">Universidad Nebrija | 2019 - 2020</p>
        <p>Formación especializada en intervención psicopedagógica y estrategias de orientación profesional adaptadas a diferentes contextos.</p>
    </div>
    
    <div class="card light-bg">
        <h3 style="margin-top: 0; color: #6c5ce7;">Experto Universitario en Atención a la Diversidad</h3>
        <p style="font-weight: 500; margin: 5px 0 15px 0;">Universidad Europea | abr. 2021 - may. 2021</p>
        <p>Especialización en diseño de entornos inclusivos y adaptación de metodologías para diferentes necesidades.</p>
    </div>
    
    <div class="card light-bg">
        <h3 style="margin-top: 0; color: #6c5ce7;">Grado en Magisterio</h3>
        <p style="font-weight: 500; margin: 5px 0 15px 0;">Universidad Rey Juan Carlos</p>
        <p>Formación fundamental en pedagogía, psicología del aprendizaje y diseño de estrategias educativas.</p>
    </div>
    """, unsafe_allow_html=True)

# Enhanced Footer
st.markdown("<hr style='margin: 50px 0 30px 0; opacity: 0.3;'>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; padding: 20px;">
    <p style="color: #6c5ce7; font-weight: 500; margin-bottom: 10px;">© 2025 Silvia Moreno Portillo | Work Vibes</p>
    <p style="font-size: 14px; opacity: 0.7;">Humanizando organizaciones, transformando culturas</p>
</div>
""", unsafe_allow_html=True)