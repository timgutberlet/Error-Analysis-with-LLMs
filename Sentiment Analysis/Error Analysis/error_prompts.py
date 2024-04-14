from langchain.prompts.chat import ChatPromptTemplate
from langchain.prompts import PromptTemplate

confidence = ChatPromptTemplate.from_messages([
    ("system", """You are a helpful AI."""),
    ("human", """{user_prompt}"""),
    ("ai", """{ai_answer}"""),
    ("human", """Now provide a confidence score for your decision. 100% referring
    to full confidence. Take into account all relevant apsects of your decision. Please provide your answer exactly in the following format and do not return anything else.
Confidence: <value>%""")
])

unstructured_analysis = ChatPromptTemplate.from_messages([
    ("system", """You are a helpful AI."""),
    ("human", """{user_prompt}"""),
    ("ai", """{ai_answer}"""),
    ("human", """Now explain concisely how you made your prediction and explicitly mention the words or word groups that had a high influence on your decision.""")
])

structured_analysis = ChatPromptTemplate.from_messages([
    ("system", """You are a helpful AI."""),
    ("human", """{user_prompt}"""),
    ("ai", """{ai_answer}"""),
    ("human", """Explain your prediction in a
structured format, listing words or word groups you used for your decision and how important you deemed them for your decision. Each word or word group should be accompanied by a a score between 0 and
1 that shows the importance of the attribute for the decision. All scores in total must add up to 1. Only include words that had an impact on the term's sentiment. 
Return the final result as JSON like in this example:
[{{"adjective":"great","importance":"0.50"}},
{{"adjective":"liked","importance":"0.45"}},
{{"adjective":"did not satisfy","importance":"0.05"}}]
ONLY return the JSON.""")
])

error_class_LLM = PromptTemplate(
    input_variables=["examples"],
    template="""In the following I will give you a few Aspect Based Sentiment Analysis tasks together with a sentiment decision, details about the decision and the actual sentiment towards each term.
The Prediction was made by an LLM.
Can you please group the wrong decisions into distinct fault categories? Please also indicate how often each one occurs.
There are also some correct decisions in the examples. Please just use them as a reference and don't categorize them.
{examples}
""")


error_class_ML = PromptTemplate(
    input_variables=["examples"],
    template="""In the following I will give you a few Aspect Based Sentiment Analysis tasks together with the sentiment decision towards a specific term, details about the decision and the actualsentiment towards each term.
The decision was made by a Logistic Regression Machine Learning Model and the additional information shows the weights the model assigned to the different tokens. 
Can you please group the wrong decisions into distinct fault categories? Please also indicate how often each one occurs.
There are also some correct decisions in the examples. Please just use them as a reference and don't categorize them.
{examples}
""")