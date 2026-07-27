from langchain_core.prompts import PromptTemplate

while True:
    templateEmail = PromptTemplate(
        input_variables=["role", "experience", "purpose", "recipient", "tone", "language"],
        template="""
Act as a {role} with {experience} years of experience in professional email writing.

Your goal is to write a well-structured email.

Purpose: {purpose}

Recipient: {recipient}

Writing tone: {tone}

Write the email in {language}.

The email should include:
- A suitable subject line
- A polite greeting
- A clear introduction
- A detailed body
- A professional closing
- Sender's name as [Your Name]

The email should:
- Be professional and grammatically correct
- Avoid emojis
- Be clear and concise
"""
    )

    choice = input("Do you want to run (Y/N): ")

    if choice.strip().lower() == "y":
        role = input("Enter role: ")
        exp = input("Enter experience (years): ")
        purpose = input("Enter email purpose: ")
        recipient = input("Enter recipient: ")
        tone = input("Enter tone: ")
        language = input("Enter language: ")

        prompt = templateEmail.format(
            role=role,
            experience=exp,
            purpose=purpose,
            recipient=recipient,
            tone=tone,
            language=language
        )

        print("\nGenerated Prompt:\n")
        print(prompt)

    else:
        print("You exited the program.")
        break