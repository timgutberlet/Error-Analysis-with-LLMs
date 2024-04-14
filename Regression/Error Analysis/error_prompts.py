# This file is used to store the prompt templates for the error analysis tasks

from langchain.prompts.chat import ChatPromptTemplate
from langchain.prompts import PromptTemplate

#prompt for the confidence analysis
confidence = ChatPromptTemplate.from_messages([
    ("system", """You are a helpful AI."""),
    ("human", """{user_prompt}"""),
    ("ai", """"price": {ai_answer} INR """),
    ("human", """Provide a percentage score on how confident you are that your predicted price is in a range of +-20% of the actual price. 100% referring
    to full confidence. Take into account all diffferent aspects of the car that make you more or less sure that your prediction is in the range. Please provide your answer exactly like in the following format and do not return anything else.
Confidence: <value>%""")
])

#Prompt for the unstructured explanations
unstructured_analysis = ChatPromptTemplate.from_messages([
    ("system", """You are a helpful AI."""),
    ("human", """{user_prompt}"""),
    ("ai", """{ai_answer}"""),
    ("human", """Now explain concisely how you made your prediction and explicitly mention the attributes and values that had a high influence on your decision.""")
])

#Prompt for the structured explanations
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

# Prompt for the structured explanations with the car name explicitly asked for
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

# Prompt for the error classification
error_class_LLM = PromptTemplate(
    input_variables=["examples"],
    template="""In the following I will give you a few price prediction tasks together with a prediction decision, details about the decision and the actual price.
A wrong prediction is a prediction that deviates by more than 20 percent from the actual price. The Prediction was made by an LLM.
Can you please group the wrong decisions into distinct fault categories? Please also indicate how often each one occurs.
There are also some correct decisions (deviation of less than 20 percent) in the examples. Please just use them as a reference and don't categorize them.
{examples}
""")

# Prompt for the error classification without the categories overestimation and underestimation
error_class_LLM_nounderover = PromptTemplate(
    input_variables=["examples"],
    template="""In the following I will give you a few price prediction tasks together with a prediction decision, details about the decision and the actual price.
A wrong prediction is a prediction that deviates by more than 20 percent from the actual price. The Prediction was made by an LLM.
Can you please group the wrong decisions into distinct fault categories? Please also indicate how often each one occurs.
There are also some correct decisions (deviation of less than 20 percent) in the examples. Please just use them as a reference and don't categorize them.
Please go deeper with your analysis and don't use Overestimation or Underestimation as categories.
{examples}
""")

# Prompt for the error classification with the regression predictions and explanations as input
error_class_ML = PromptTemplate(
    input_variables=["examples"],
    template="""In the following I will give you a few price prediction tasks together with a prediction decision, details about the decision and the actual price.
A wrong prediction is a prediction that deviates by more than 20 percent from the actual price. 
The decision was made by a Lasso Regression Machine Learning Model and the additional information shows the weights the model assigned to the different tokens. 
Can you please group the wrong decisions into distinct fault categories? Please also indicate how often each one occurs.
There are also some correct decisions (deviation of less than 20 percent) in the examples. Please just use them as a reference and don't categorize them.
Please go deeper with your analysis and don't just use Overestimation or Underestimation as categories.
{examples}
""")