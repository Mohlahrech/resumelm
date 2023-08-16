from pathlib import Path
import streamlit as st
from PIL import Image

#---path settings----------

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "resume.pdf"
profile_pic = current_dir / "assets" / "pic.png"

#------------GENERAL SETTINGS-----------------

PAGE_TITLE = "CV | LAHRECH Mohamed"
PAGE_ICON = ":flag-dz:"
NAME = "Mohamed LAHRECH"
DESCRIPTION = """
IT Support specialist ,Odoo developer supporting entreprises....
"""

EMAIL = "mohamed.lahrech15@gmail.com"
SOCIAL_MEDIA = {
    "Facebook": "https://www.facebook.com/mohamed.lahrech.169/",
    "Linkedin" : "https://www.linkedin.com/in/mohamed-lahrech-787936172/",
    "Github" : "https://github.com/Mohlahrech",
    "Youtube" : "https://www.youtube.com/channel/UC7qe94o1-qnopKoB8iAs2Rw",
}
Projects = {
             "🏆 Projet d'integration de l'Erp Synergie - Société nationale des travaux publics": "http://www.sntp.dz/",
             "🏆 Projet de digitalisation de le gestion documentaire - Société nationale des travaux publics": "http://www.sntp.dz/",
             "🏆 Projet d'optimisation de l'ERP ODOO - Intellisolutions": "http://intellisolutions-dz.com/"

}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

#-------LOAD CSS,PDF AND PROFIL PIC--------
with open(css_file) as f:
    st.markdown("<style>{}<\style>".format(f.read()),unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

#---------HERO_SECTION---------
col1,col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Télécharger CV",
        data= PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
st.markdown("<style>body { background-color: #FFFFFF; }</style>", unsafe_allow_html=True,)
st.write("📫", EMAIL)

#-----SOCIAL_LINKS----------

st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

#--------Experience and qualifications-------
st.write("#")
st.subheader("Experiences et capacités")
st.write("""
- ✔ 4 ans d'experience dans la gestion des systemes d'information
- ✔ Expert en gestion de projets
- ✔ Expert dans les systemes informatiques
- ✔ Plus d'une année de développement sur Odoo
""")

#---SKILLS----
st.write("#")
st.subheader("Compétences")
st.write(
    """
- 📊 Administration réseau
- 🗄️ Sytemes d'exploitations et SGBD: Windows, windows Server, SQL Server
- 💻 Dévelopmement Python / Xml
- 📚 Maitrise des systemes de sécurité 
"""
)

#-----WORK HISTORY-------
st.write("#")
st.subheader("Experiences professionneles")
st.write("---")

#----JOB1
st.write("🚧", "IT support specialist | Intellisolutions")
st.write("07/2022- present")
st.write("""
    - ►Gestion du support clients
    - ►Déploiement des produits (Logiciels) chez les clients
    - ►Gestion interne du parc et du réseau informatique
    - ►Gestion des projets IT internes    
"""
)
# --- JOB 2
st.write('\n')
st.write("🚧", "Chef de service informatique | Société nationale des travaux publics")
st.write("05/2021 - 07/2022")
st.write(
    """
- ► Gestion du systeme d'information (Communication intra et extra entreprise, digitalisation, optimisation)   
- ► Supervisé differents projets de digitalisation (ERP, Gestion documentaire...)
- ► Supervisé differents projets IT (dévelopement du parc informatique, dévelopement de la Cyber-sécurité)
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "Cadre administratif | Société nationale des travaux publics ")
st.write("11/2019 - 05/2021")
st.write(
    """
- ► Gestion logistique du matériel informatique
- ► Helpdesk
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in Projects.items():
    st.write(f"[{project}]({link})")
