### What The Repo Has ?

This repository contains an interactive Python CLI application demonstrating dynamic prompt generation using LangChain's PromptTemplate. It allows users to create structured LLM instructions, such as writing educational chapters, based on customized inputs. 

### Example

## Basic Text Completion Template

from langchain_core.prompts import PromptTemplate
template = PromptTemplate.from_template("What is the capital city of {country}?")
final_prompt = template.format(country="India")
print(final_prompt)

# Output: What is the capital city of India?
