from langchain.prompts.chat import ChatPromptTemplate
from langchain.prompts import PromptTemplate

confidence = ChatPromptTemplate.from_messages([
    ("system", """You are a helpful AI."""),
    ("human", """{user_prompt}"""),
    ("ai", """{ai_answer}"""),
    ("human", """Now provid a confidence score for your prediction as percentage values, 100%
referring to perfect similarity or full confidence. Please provide your answer exactly in the same format as the following example output:
Confidence: <value>%""")
])

unstructured_analysis = ChatPromptTemplate.from_messages([
    ("system", """You are a helpful AI."""),
    ("human", """{user_prompt}"""),
    ("ai", """{ai_answer}"""),
    ("human", """Now explain concisely how you made your prediction and explicitly mention the attributes and values that had a high influence on your decision.""")
])

structured_analysis = ChatPromptTemplate.from_messages([
    ("system", """You are a helpful AI."""),
    ("human", """{user_prompt}"""),
    ("ai", """{ai_answer}"""),
    ("human", """Explain your prediction in a
structured format, listing attributes of the car you used and how important you deemed them for your prediction. Each attribute should be
accompanied by the attribute value and a score between 0 and
1 that shows the importance of the attribute for the prediction. All scores in total must add up to 1. Only include attributes that had an influence on your decision.
Return the final result as JSON like in this example:
[{{"attribute":"name","importance":"0.50","value":"Mahindra XUV500 W10 2WD"}},
{{"attribute":"km_driven","importance":"0.45","value":"70000"}},
{{"attribute":"mileage","importance":"0.05","value":"16 kmpl"}}]
ONLY return the JSON.""")
])

structured_analysis_inclname = ChatPromptTemplate.from_messages([
    ("system", """You are a helpful AI."""),
    ("human", """{user_prompt}"""),
    ("ai", """{ai_answer}"""),
    ("human", """Explain your prediction in a
structured format, listing attributes of the car (such as name or km_driven) you used and how important you deemed them for your prediction. Each attribute should be
accompanied by the attribute value and a score between 0 and
1 that shows the importance of the attribute for the prediction. All scores in total must add up to 1. Only include attributes that had an influence on your decision.
Return the final result as JSON like in this example:
[{{"attribute":"name","importance":"0.50","value":"Mahindra XUV500 W10 2WD"}},
{{"attribute":"km_driven","importance":"0.45","value":"70000"}},
{{"attribute":"mileage","importance":"0.05","value":"16 kmpl"}}]
ONLY return the JSON.""")
])

error_class_LLM = PromptTemplate(
    input_variables=["examples"],
    template="""In the following I will give you a few price prediction tasks together with a prediction decision, details about the decision and the actual price.
A wrong prediction is a prediction that deviates by more than 20 percent from the actual price. The Prediction was made by an LLM.
Can you please group the wrong decisions into 3 fault categories? Please also indicate how often each one occurs.
There are also some correct decisions (deviation of less than 20 percent) in the examples. Please just use them as a reference and don't categorize them.
{examples}
""")

error_class_ML = PromptTemplate(
    input_variables=["examples"],
    template="""In the following I will give you a few price prediction tasks together with a prediction decision, details about the decision and the actual price.
A wrong prediction is a prediction that deviates by more than 20 percent from the actual price. The prediction was made by a Machine Learning Model.
Can you please group the wrong decisions into 3 fault categories? Please also indicate how often each one occurs.
There are also some correct decisions (deviation of less than 20 percent) in the examples. Please just use them as a reference and don't categorize them.
{examples}
""")