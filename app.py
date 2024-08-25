import streamlit as st
from PIL import Image

# Set custom page title and favicon
st.set_page_config(
    page_title="Hashir's Life",
    page_icon="icon.png",
    layout="wide",
)

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home","Academic Qualifications", "Professional Experience", "Major Projects", "Extra-Curricular Activities", "Certifications", "Skills", "Contact"])

# Home Page
if page == "Home":
    st.title("Hello, I'm Hashir!")
    # Layout: Two Columns
    col1, col2 = st.columns([2, 1])  # Create two columns with relative width

    # Left Column - Text
    with col1:
        st.subheader("Machine Learning | Generative AI | Computer Science")
        st.write("""
        As a recent graduate from the Institute of Business Administration with a Bachelor of Science in Computer Science, I specialize in Generative AI and ML techniques. Currently, I am applying my expertise as a Junior AI Engineer at Kalorist, an early-stage incubated company. In this role, I play a pivotal part in developing KalCoach, a personalized fitness AI assistant designed to help users achieve their wellness goals.
        My background includes a successful tenure as CFO of the IBA Student Government, where I managed a substantial budget with precision and data-driven insights. With strong skills in ML, NLP, and AI, combined with a drive to innovate, I am committed to digitalizing the world with intelligence.
        """)

    # Right Column - Image (Round)
    with col2:
        img = Image.open("hashir.jpg")  # Replace with your profile picture
        st.image(img, use_column_width=True, output_format="PNG")




# Academic Qualifications Page
elif page == "Academic Qualifications":
    st.title("Academic Qualifications")
    
    st.subheader("Institute of Business Administration, Karachi")
    st.write("""
    **BS Computer Science (2020 - 2024)**
    - CGPA: 3.56 (Honorable Mention in The Dean’s List)
    - Papers: [Link](https://iba.academia.edu/HashirMuzaffar)
    """)
    school="Army Public School, Bahawalpur"
    st.subheader(s)
    st.write("""
    **A LEVELS (2017 - 2019)**
    - Subjects: Computer Science, Physics, Chemistry, Mathematics
    - Grades: 1A*, 3As
    
    **O LEVELS (2014 - 2017)**
    - Subjects: Computer Science, Physics, Chemistry, Mathematics, English
    - Grades: 3A*s, 1A, 1B
    """)

# Professional Experience Page
elif page == "Professional Experience":
    st.title("Professional Experience")
    
    st.subheader("Kalorist - Junior AI Engineer (March 2024 - Present)")
    st.write("""
    - Working on KalCoach, a personalized fitness AI assistant for Kalorist, by testing and implementing open-source text generation LLMs and text embedding.
    - Utilizing RAG and real-time data retrieval with LangChain to enhance the nutrition and health app's capabilities.
    """)
    
    st.subheader("IBA Student Government - Treasurer (Aug 2023 - May 2024)")
    st.write("""
    - Financial Head of all student unions and societies within IBA, managing a budget of 14 million rupees.
    - Utilized advanced Excel functions and data analysis techniques to track expenses, forecast budget needs, and optimize financial allocations.
    - Acted as a bridge between students and Deans of different schools and the Director of IBA, using data-driven insights to effectively resolve student concerns and queries.
    """)
    
    st.subheader("Institute of Business Administration Karachi - Teaching Assistant (Aug 2022 - Dec 2023)")
    st.write("""
    - Worked as Teaching Assistant for introductory level Computer Science courses.
    - Led independent lectures and tutorials on a weekly basis, graded quizzes, and assignments for 500+ students.
    """)
    
    st.subheader("Discourse Analytics - AI Intern (Jun 2023 - Jul 2023)")
    st.write("""
    - Built an AI-powered email automation system using OpenAI models.
    - Customized responses by fine-tuning models with a previous dataset of emails. Developed email sending system API with Node.js.
    - Optimized model efficiency and cost-effectiveness through prompt engineering.
    """)
    
    st.subheader("Institute of Business Administration - Research Assistant (Jan 2024 - Mar 2024)")
    st.write("""
    - Collaborated with the Project Lead to promote indigenous literature in academic research by identifying potential research profiles and strategizing outreach efforts to get local published work cited in local and international research endeavors.
    """)

# Major Projects Page
elif page == "Major Projects":
    st.title("Major Projects")
    
    st.subheader("Floor Plan Generation using Generative AI")
    st.write("""
    - Leveraged the power of generative AI and worked closely with my team to generate multi-story floor plans using Stable Diffusion Model, to enhance and build our own research on preexisting research.
    """)
    
    st.subheader("Clothes Re-selling Website - Sycle")
    st.write("""
    - Utilized Typescript, MUI, React, and Figma for front-end design.
    - Used Node.js, Express, and Mongoose for back-end and database operations.
    """)
    
    st.subheader("Data Mining and Analysis")
    st.write("""
    - Completed projects on Kaggle for classification, clustering, regression, and text analysis.
    - Used Python libraries like Pandas, NumPy, Scikit-learn, and NLTK and machine learning algorithms for analysis.
    - Applied techniques like feature engineering, model selection, and hyperparameter tuning to optimize performance.
    - Analyzed and visualized datasets to uncover patterns using Matplotlib and Seaborn.
    """)
    
    st.subheader("Painting Store Web-Based Inventory")
    st.write("""
    - Rapidly developed a web application for an Art Dealership Management System, focusing on SQL and data science principles.
    - Designed and implemented a robust database on Oracle Database using SQL for efficient data storage, retrieval, and manipulation.
    - Utilized JAVA and OJDBC for seamless database connectivity and developed the front-end using HTML and CSS.
    """)
    
    st.subheader("Computer Vision Based Volume Control Remote")
    st.write("""
    - Developed a motion-sensing remote to adjust volume via hand gestures using ML algorithms for real-time gesture recognition.
    - Used Python libraries like OpenCV and NumPy along with other open-source resources, to process and interpret gesture data.
    """)
    
    st.subheader("Student Budgeting Android App – Wallit")
    st.write("""
    - Led a team to develop “Wallit,” an app to boost financial literacy.
    - Developed a full-stack mobile app leveraging JAVA and Firebase.
    - Designed UI in Figma and performed Junit testing.
    """)
    
    st.subheader("End-to-End RAG Based Chatbot")
    st.write("""
    - Developed a complete end-to-end RAG based chatbot using LANGCHAIN and Gorq Fast API.
    - Created front-end using Python Streamlit.
    """)

# Extra-Curricular Activities Page
elif page == "Extra-Curricular Activities":
    st.title("Extra-Curricular Activities")
    
    st.subheader("AIESEC Turkey - Summer Volunteer (Jun 2021 - Aug 2021)")
    st.write("""
    - Interned as a Language and Culture Ambassador at Living It Gaziantep, taught English as a second language.
    """)
    
    st.subheader("United Nations Association of Pakistan - Youth Member (Feb 2022 - Feb 2023)")
    st.write("""
    - Collected an amount of 10,000 PKR for Flood Relief in United Nations Association of Pakistan.
    """)
    
    st.subheader("SHARE IBA - Strategy Manager (Jun 2023 - Nov 2023)")
    st.write("""
    - Analyzed concrete case studies to transform companies’ strategies to be more sustainable & inclusive as a member.
    """)
    
    st.subheader("IBA Public Speaking Society - Assistant Director (Aug 2021 - Aug 2022)")
    st.write("""
    - Streamlined the digital payment process of MUNIK XII as Assistant Director of HR and Registration Department.
    """)
    
    st.subheader("IBA Human Resource Club - Director (Aug 2021 - Aug 2022)")
    st.write("""
    - Derived strategies and marketing campaigns for IBA HR club events and organized career counseling sessions.
    """)

# Certifications Page
elif page == "Certifications":
    st.title("Certifications")
    
    st.write("""
    - **Fundamentals of UX** - Google
    - **Computer Network and Communications** - CISCO
    - **Introduction to Advanced Excel** - IBM
    - **Excel for Data Analytics** - IBM
    - **Deep Learning Essentials** - 10Pearl University
    - **Introduction to Salesforce CRM** - 10Pearl University
    - **Foundations of Project Management** - Google
    - **Python Crash Course** - Google
    - **Teamwork Foundation** - LinkedIn
    - **Automation for Python** - Google
    """)

# Skills Page
elif page == "Skills":
    st.title("Skills")
    
    st.write("""
    - **Proficient in:** SQL, Python, SPSS-IBM, Excel-MS, and JAVA.
    - **Familiarity with:** MERN, Golang, Pandas, NumPy, Scikit-learn, TensorFlow, LangChain, GitHub, and MochaJs.
    """)

# Contact Page
elif page == "Contact":
    st.title("Contact Me")
    
    st.write("Feel free to reach out to me through the following platforms:")
    
    st.markdown("""
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
            # Function to send email would go here
            st.success("Message sent!")

# Footer
st.sidebar.write("---")
st.sidebar.write("Developed by Hashir | © 2024")
