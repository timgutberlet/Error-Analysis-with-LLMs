# Error-Analysis-with-LLMs
## Introduction
Prompt-Engineering Methods such as Few-Shot Prompting and Automated Error Analysis have been used to better understand answer structures and improve the performance of LLMs. In this thesis I aim to apply these tech-
niques to three new task types: Schema-Matching, Sentiment Analysis and Price Prediction to
test if and to what extent error analysis can be used to better understand and potentially improve
the performance of solving these tasks with LLMs.

## Instructions
- Create .env in Main directory & Add important API Keys in the following format:
  - OPENAI_API_KEY="..."
  - LANGFUSE_PUBLIC_KEY="..."
  - LANGFUSE_SECRET_KEY="..."
  - LANGFUSE_HOST="https://cloud.langfuse.com"

## Important Libraries & Setup
- The Python Version 3.12.2 was used to the experiments
- To make the code work the following libraries have to be pre-installed in your environment:
  - Langfuse (https://langfuse.com)
  - Langchain (https://www.langchain.com)
  - Sk-Learn (https://scikit-learn.org/stable/)
  - Pandas (https://pandas.pydata.org)
  - Numpy (https://numpy.org/doc/stable/index.html)

## Select the correct kernel in the notebook
Select a kernel -> python environments -> .venv
 
