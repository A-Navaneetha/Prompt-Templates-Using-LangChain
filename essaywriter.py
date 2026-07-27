from langchain_core.prompts import PromptTemplate

while True:
    templateEssay = PromptTemplate(
        input_variables=[
            "role", "experience", "topic",
            "word_limit", "level", "language"
        ],
        template="""
Act as a {role} with {experience} years of experience in essay writing.

Your goal is to write a well-structured essay on the topic "{topic}".

The essay should be approximately {word_limit} words.

The essay should include:
- A suitable title
- An engaging introduction
- Well-organized body paragraphs
- Relevant examples and explanations
- A strong conclusion

Write the essay in {language} using very simple words.

The writing level should be suitable for {level} students.

The essay should:
- Be original
- Be grammatically correct
- Avoid emojis
- Avoid one-line paragraphs
- Maintain a logical flow throughout
"""
    )

    choice = input("Do you want to run (Y/N): ")

    if choice.strip().lower() == "y":
        role = input("Enter role: ")
        exp = input("Enter experience (years): ")
        topic = input("Enter essay topic: ")
        words = input("Enter word limit: ")
        level = input("Enter education level: ")
        language = input("Enter language: ")

        prompt = templateEssay.format(
            role=role,
            experience=exp,
            topic=topic,
            word_limit=words,
            level=level,
            language=language
        )

        print("\nGenerated Prompt:\n")
        print(prompt)

    else:
        print("You exited the program.")
        break