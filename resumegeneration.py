from langchain_core.prompts import PromptTemplate

while True:
    templateResume = PromptTemplate(
        input_variables=[
            "role", "experience", "name", "job_role",
            "skills", "education", "language"
        ],
        template="""
Act as a {role} with {experience} years of experience in resume writing.

Your goal is to create a professional resume.

Candidate Name: {name}
Applying for: {job_role}

Skills:
{skills}

Education:
{education}

Write the resume in {language}.

The resume should include:
- Professional Summary
- Technical Skills
- Education
- Projects (if applicable)
- Certifications (if applicable)
- Strengths
- Career Objective

The resume should:
- Be ATS-friendly
- Be professional
- Avoid emojis
- Use clear headings and bullet points
"""
    )

    choice = input("Do you want to run (Y/N): ")

    if choice.strip().lower() == "y":
        role = input("Enter role: ")
        exp = input("Enter experience (years): ")
        name = input("Enter candidate name: ")
        job = input("Enter job role: ")
        skills = input("Enter skills: ")
        education = input("Enter education: ")
        language = input("Enter language: ")

        prompt = templateResume.format(
            role=role,
            experience=exp,
            name=name,
            job_role=job,
            skills=skills,
            education=education,
            language=language
        )

        print("\nGenerated Prompt:\n")
        print(prompt)

    else:
        print("You exited the program.")
        break