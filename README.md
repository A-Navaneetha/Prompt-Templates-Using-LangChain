# Prompt Templates using LangChain

A clean and simple Python repository demonstrating how to create, format, and manage dynamic prompt templates using the official **LangChain** core library. 

This project shows how to transition from basic static strings to interactive, user-driven prompt generation.

---

## 🚀 Getting Started

### Prerequisites
Make sure you have Python installed, then install the core LangChain library:
```bash
pip install langchain-core
```

### Simple Example (Basic String Template)
Here is a straightforward example of using `PromptTemplate.from_template` to automatically detect a variable and format a quick question:

```python
from langchain_core.prompts import PromptTemplate

# 1. Define the template with a placeholder
template = PromptTemplate.from_template("What is the capital city of {country}?")

# 2. Fill in the variable
final_prompt = template.format(country="India")

print(final_prompt)
# Output: What is the capital city of India?
```

---

## 💻 Interactive Prompt Generator

The main script in this repository features an interactive Command Line Interface (CLI) application. It explicitly maps out multiple variables (`role`, `experience`, `topic`, `subject`, `level`) to build detailed, constraint-based textbook content generation prompts for LLMs.

### Run the Application
Save the code to a file (e.g., `app.py`) and execute it.
