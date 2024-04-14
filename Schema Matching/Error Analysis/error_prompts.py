from langchain.prompts.chat import ChatPromptTemplate
from langchain.prompts import PromptTemplate

confidence_old = ChatPromptTemplate.from_messages([
    ("system", """You are a helpful AI."""),
    ("human", """{user_prompt}"""),
    ("ai", """{ai_answer}"""),
    ("human", """Now provide a confidence score for how sure you are of your decision to {match} the pair {columns}. The score ranges from 0 - 100 with 100 being the case where you are absolutely sure that your decision is correct. Please provide your output as JSON in the following format and return nothing else:
{{"column_mappings": A list of <"Column-Table A", "Column-Table B or None", "confidence-score"> triples}}""")
])

confidence = ChatPromptTemplate.from_messages([
    ("system", """You are a helpful AI."""),
    ("human", """{user_prompt}"""),
    ("ai", """{ai_answer} """),
    ("human", """Provide a confidence score for your decision to {match} columns {columns}. 100% referring
    to full confidence. Take into account the provided tables and the similarities and differences of the specific columns. Please provide your answer exactly in the following format and do not return anything else.
Confidence: <value>%""")
])

unstructured_analysis = ChatPromptTemplate.from_messages([
    ("system", """You are a helpful AI."""),
    ("human", """{user_prompt}"""),
    ("ai", """{ai_answer}"""),
    ("human", """Now explain concisely how and why you made your decision to {match} the pair {columns} and explicitly mention the values that had a high influence on your decision.""")
])

structured_analysis = ChatPromptTemplate.from_messages([
    ("system", """You are a helpful AI."""),
    ("human", """{user_prompt}"""),
    ("ai", """{ai_answer}"""),
    ("human", """Explain your decision for the pair {columns} in a
structured format, listing the values of the columns you used and how important you deemed them for your decision. Only list important values that had a high influence on your decision.
Return the final result as JSON in this format:
[{{"value":"<value>","importance":"0.50","column":"<column>"}},..]""")
])

error_class_LLM = PromptTemplate(
    input_variables=["examples"],
    template="""In the following I will give you schema matching tasks together with column matching decisions. You are given additional explanation on the predicted matching decision for two specific columns and the actual answer regarding the match of the two columns.
The decision was made by an LLM. Can you please group the wrong decisions into distinct fault categories? Please also indicate how often each one occurs.
There are also some correct decisions in the examples. Please just use them as a reference and don't categorize them.
{examples}
""")

error_class_ML = PromptTemplate(
    input_variables=["examples"],
    template="""In the following I will give you a schema matching tasks together with a column matching decision, details about the decision and the if the columns actually match.
The decision was made by a Logistic Regression Machine Learning Model and the additional information shows the weights the model assigned to the different tokens. 
Can you please group the wrong decisions into distinct fault categories? Please also indicate how often each one occurs.
There are also some correct decisions in the examples. Please just use them as a reference and don't categorize them.
{examples}
""")