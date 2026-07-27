from langchain_core.prompts import PromptTemplate
while True:
    templateStory = PromptTemplate(
        input_variables=["role", "experience", "genre", "topic", "length", "language"],
        template="""
Act as a {role} who has {experience} years of experience in writing {genre} stories.
Your goal is to write a complete and engaging story on the topic "{topic}".
The story should include:
- A creative title
- An interesting introduction
- Well-developed characters
- A clear setting
- A logical plot
- Dialogues where appropriate
- Conflict and suspense
- A meaningful climax
- A satisfying ending
- A moral or life lesson (if applicable)

The story should be approximately {length}.

Write the entire story in {language} using very simple and natural words so that readers of all ages can easily understand it.

The output should:
- Be creative and engaging
- Maintain continuity throughout the story
- Use descriptive paragraphs instead of one-line paragraphs
- Avoid emojis
- Avoid unnecessary repetition
- Make the story emotionally engaging and easy to visualize.
"""
    )

    choice = input("Do you want to run (Y/N): ")

    if choice.strip().lower() == "y":
        role = input("Enter role: ")
        exp = input("Enter experience (years): ")
        genre = input("Enter story genre: ")
        topic = input("Enter story topic: ")
        length = input("Enter story length (e.g., 1000 words): ")
        language = input("Enter language: ")

        prompt = templateStory.format(
            role=role,
            experience=exp,
            genre=genre,
            topic=topic,
            length=length,
            language=language
        )

        print("\nGenerated Prompt:\n")
        print(prompt)

    else:
        print("You exited the program.")
        break   