from langchain.prompts import PromptTemplate

prompt_1_zeroshot = PromptTemplate(
    input_variables=["input_text"],
    template="""
    The following is a conversation between a customer and a customer service representative. 
    The customer is upset because they received a defective product. The customer service representative is trying to help the customer."""