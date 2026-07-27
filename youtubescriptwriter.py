from langchain_core.prompts import PromptTemplate

while True:
    templateYouTube = PromptTemplate(
        input_variables=[
            "role", "experience", "topic",
            "duration", "audience", "language"
        ],
        template="""
Act as a {role} with {experience} years of experience in creating YouTube video scripts.

Your goal is to write a complete YouTube script on the topic "{topic}".

The video duration should be approximately {duration}.

Target audience: {audience}

Write the script in {language}.

The script should include:
- A catchy video title
- A strong hook in the first 15 seconds
- A brief introduction
- Well-organized main content
- Real-life examples where appropriate
- A summary of key points
- A call-to-action (Like, Share, Comment, and Subscribe)
- A professional closing

The script should:
- Be engaging and conversational
- Use simple and easy-to-understand language
- Maintain a logical flow
- Avoid emojis
- Avoid one-line paragraphs
"""
    )

    choice = input("Do you want to run (Y/N): ")

    if choice.strip().lower() == "y":
        role = input("Enter role: ")
        exp = input("Enter experience (years): ")
        topic = input("Enter video topic: ")
        duration = input("Enter video duration: ")
        audience = input("Enter target audience: ")
        language = input("Enter language: ")

        prompt = templateYouTube.format(
            role=role,
            experience=exp,
            topic=topic,
            duration=duration,
            audience=audience,
            language=language
        )

        print("\nGenerated Prompt:\n")
        print(prompt)

    else:
        print("You exited the program.")
        break