import streamlit as st
from PIL import Image

# Set custom page title and favicon
st.set_page_config(
    page_title="Hashir's life",
    page_icon="icon.png",
    layout="wide",
)

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Experience", "Contact"])

# Home Page
if page == "Home":
    st.title("Hello, I'm Hashir!")
    # Layout: Two Columns
    col1, col2 = st.columns([2, 1])  # Create two columns with relative width

    # Left Column - Text
    with col1:
        st.subheader("Junior AI Engineer | AI Enthusiast | Teacher")
        st.write("""
        As a recent graduate from the Institute of Business Administration with a Bachelor of Science in Computer Science, I specialize in Generative AI and ML techniques. Currently, I am applying my expertise as a Junior AI Engineer at Kalorist, an early-stage incubated company. In this role, I play a pivotal part in developing KalCoach, a personalized fitness AI assistant designed to help users achieve their wellness goals.
        My background includes a successful tenure as CFO of the IBA Student Government, where I managed a substantial budget with precision and data-driven insights. With strong skills in ML, NLP, and AI, combined with a drive to innovate, I am committed to digitalizing the world with intelligence.
        """)

    # Right Column - Image (Round)
    with col2:
        img = Image.open("hashir.jpg")  # Replace with your profile picture
        st.image(img, use_column_width=True, output_format="PNG")



# Projects Page
elif page == "Projects":
    st.title("Projects")
    
    st.subheader("KalCoach AI Assistant")
    st.write("""
    - Developing KalCoach, a personalized AI fitness assistant for Kalorist, using GPT-4, LangChain, and RAG.
    - Involves testing and implementing open-source text generation models and improving real-time data retrieval for nutrition and health.
    """)
    
    st.subheader("Generative AI Floor Plans")
    st.write("""
    - Worked on generating multi-story floor plans using generative AI and Stable Diffusion, building on existing research.
    - The project aimed to automate architectural planning using AI.
    """)
    
    st.subheader("Email Automation System")
    st.write("""
    - Created an email automation system for Discourse Analytics using OpenAI LLMs.
    - This system automated email processing and response generation, improving organizational cost-efficiency.
    """)

# Experience Page
elif page == "Experience":
    st.title("Experience")
    
    st.subheader("Kalorist - Junior AI Engineer (March 2024 - Present)")
    st.write("""
    - Developing a personalized AI fitness assistant with advanced LLMs and real-time data retrieval.
    - Working with text generation and embedding techniques for better user engagement.
    """)
    
    st.subheader("Discourse Analytics - AI Intern")
    st.write("""
    - Built an AI-powered email automation system using OpenAI models.
    - Successfully fine-tuned models for more accurate email processing.
    """)
    
    st.subheader("AIESEC")
    st.write("""
    - Participated in global experiences, including a Language and Culture Ambassador internship in Turkey.
    - Promoted social cohesion and taught English to underprivileged children, enhancing cultural understanding.
    """)

# Contact Page
elif page == "Contact":
    st.title("Contact Me")
    
    st.write("Feel free to reach out to me through the following platforms:")
    
    st.markdown("""
    - **Email:** hashir@example.com
    - **LinkedIn:** [Hashir Muzaffar](https://www.linkedin.com/in/hashir-muzaffar)
    - **GitHub:** [hashirmuzaffar](https://github.com/hashirmuzaffar)
    """)
    
    # Contact Form
    st.subheader("Contact Form")
    with st.form(key="contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Send")
        
        if submit_button:
            st.success("Message sent!")

# Footer
st.sidebar.write("---")
st.sidebar.write("Developed by Hashir | © 2024")
