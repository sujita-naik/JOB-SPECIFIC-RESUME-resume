from google import genai
import streamlit as st
client = genai.Client(api_key="AIzaSyBXLYrjEV-0hllxQ3LDR-fSZ2Yr2-ymurU")
st.title("JOB-SPECIFIC RESUME")
name = st.text_input("Full Name")
contact_number=st.text_input("Contact no.")
Email=st.text_input('Email address')
education = st.text_area("Education")
skills = st.text_area("Skills")
projects = st.text_area("Projects")
experience = st.text_area("Experience / Internship")
career_objective = st.text_area("Career Objective")
job_description = st.text_area("Paste Job Description")
if st.button("Generate Resume"):
    if job_description.strip() == "":
        st.warning("Please paste a Job Description")
    else:
        resume_data = f"""
        Name: {name}
        Email:{Email}
        Contact no.:{contact_number}
        Education: {education}
        Skills: {skills}
        Projects: {projects}
        Experience: {experience}
        Career Objective: {career_objective}
        """
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                f"""
                Create a JOB-SPECIFIC resume based on the job description below.
                Match skills, experience, and projects with job requirements.
                Remove irrelevant information.
                Remove extra text or explanation & keep resume exactly.
                JOB DESCRIPTION:
                {job_description}

                CANDIDATE DETAILS:
                {resume_data}
                """
            ]
        )
        st.subheader("Job-Specific Optimized Resume")
        st.success(response.text)