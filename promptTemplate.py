from langchain_core.prompts import PromptTemplate
while True:
    templateClass = PromptTemplate(
        input_variables=["role", "experience", "topic", "subject", "level"],
        template="""
Act as a {role} who has {experience} years of experience in {subject}.
Your goal is to write a long textbook-style chapter on the topic "{topic}".
The output should include:
- Relevant headings
- Subheadings
- Important notes
- Detailed explanations
The output should not contain emojis or one-line paragraphs.
Write the entire chapter in very simple English with {level} plagiarism so that an absolute beginner in {subject} can easily understand the concepts.
"""
    )
    choice = input("Do you want to run (Y/N): ")
    if choice.strip().lower() == "y":
        role = input("Enter role: ")
        exp = input("Enter experience (years): ")
        top = input("Enter topic: ")
        sub = input("Enter subject: ")
        lev = input("Enter plagiarism level: ")
        prompt = templateClass.format(
            role=role,
            experience=exp,
            topic=top,
            subject=sub,
            level=lev
        )
        print("\nGenerated Prompt:\n")
        print(prompt)
    else:
        print("You exited the program.")
        break