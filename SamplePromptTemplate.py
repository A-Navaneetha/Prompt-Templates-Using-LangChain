from langchain_core.prompts import PromptTemplate

while True:
    templateClass=PromptTemplate(
    input_variables=["experience","topic","subject","level"],
    partial_variables={"role":"Project Manager"},
   # template=" Act like SUBJECT MATTER EXPERT who had {experience} of experience in {subject}. Your goal is to write a long textbook style article on the {topic}. The output should contain relevant headings,sub headings, and note points.The output should not contain any emojis,one line paragraph, need a long chapter.The entire chapter should be written with {level} plagarism using very simple english, So that an absolute beginner in {subject} can understand the concept easily."
   # )
   template=" Act like {role} who had {experience} of experience in {subject}. Your goal is to write a long textbook style article on the {topic}. The output should contain relevant headings,sub headings, and note points.The output should not contain any emojis,one line paragraph, need a long chapter.The entire chapter should be written with {level} plagarism using very simple english, So that an absolute beginner in {subject} can understand the concept easily."
       )
    choice=input("Do you want to run Y/N:")
    if choice.strip().lower() == "y":
        exp=input("Enter Experience:")
        top=input("Enter Topic:")
        sub=input("Enter Subject:")
        lev=input("Enter Plagraism Level:")
        print(templateClass.format(experience=exp, topic=top, subject=sub, level=lev))
        print("========================================================================")
    else:
        print("<=============== YOU EXITED ===============")
        break