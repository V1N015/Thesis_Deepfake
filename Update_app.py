import streamlit as st 
from streamlit_option_menu import option_menu


#Page configuration
st.set_page_config(
    page_title = "Unmask",
    layout = "wide",
    initial_sidebar_state = "expanded"
)

#Hides the streamlit header
hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)

#Menu Sidebar
with st.sidebar:
    st.logo("Assets/icon.png", size = "large")
    selected = option_menu(
        menu_title = None,
        options = ["Home", "Upload", "About"],
        icons = ["houses", "upload", "info-circle" ],
    )
    st.markdown("""---""")
    st.sidebar.text("*Created by the group as part of our Thesis Project*")
#Home Page
if selected == "Home":
        col1, col2= st.columns(2, gap = "large", vertical_alignment = "center")
        with col1:
            st.markdown(""" 
                     <span style="font-size:50px; color: darkred; font-family: 'Roboto Mono', monospace;">Unmask</span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size:50px; font-family: 'Roboto Mono', monospace;">the truth hidden within images</span>
                     """, unsafe_allow_html = True)
            st.markdown("""<span style="font-size:20px; font-family: 'Roboto Mono', monospace;">Our analysis exposes the subtle signs of deepfake manipulation giving you the power to discern reality from illusion. Experience&nbsp;a new level of visual clarity with unmask.</span>""", unsafe_allow_html = True)
        with col2:
            st.image("Assets/sample.png", width = 570)
            
#Upload Page
if selected == "Upload":
    st.markdown("""<span style = "font-family: 'Roboto Mono', monospace; font-size:30px;">Upload Images for Detection</span>""", unsafe_allow_html = True)
    
    # Consent checkbox
    consent = st.checkbox("I agree to the terms and conditions for processing my images.")
    if not consent:
            st.warning("You need to agree to the terms to continue uploading images.")
    else:
        # Upload files only after consent
        reference_file = st.file_uploader("Upload reference set (multiple images allowed)", type=["jpg", "png"], accept_multiple_files=True)
        deepfake_file = st.file_uploader("Upload alleged deepfake image", type=["jpg", "png"])

        if reference_file and deepfake_file:
            st.image(reference_file, caption="Reference Image(s)", use_column_width=True)
            st.image(deepfake_file, caption="Alleged Deepfake Image", use_column_width=True)

            # Cosine similarity-based detection here
            result = "Deepfake"  # Replace with your cosine similarity-based prediction
            if result == "Deepfake":
                st.error("The uploaded image is detected as a deepfake.")
            else:
                    st.success("The uploaded image is not a deepfake.")

#About Page    
if selected == "About":
        st.markdown("""<span style = "font-family: 'Roboto Mono', monospace; font-size:40px;">About the Project</span>""", unsafe_allow_html = True)
        st.markdown("""<span style = "font-family: 'Roboto Mono', monospace; font-size:20px;">This project uses machine learning and cosine similarity to detect deepfake images.
    We compare an uploaded image to a reference set of authentic images, and the cosine similarity score helps assess the similarity between them. 
    If the similarity is below a certain threshold, the image is flagged as a deepfake.
    The goal of this tool is to help users verify the authenticity of media and raise awareness about the dangers of manipulated content.</span>""", unsafe_allow_html = True)