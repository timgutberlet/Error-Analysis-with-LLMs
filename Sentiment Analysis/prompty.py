from langchain.prompts import PromptTemplate

prompt_1_zeroshot = PromptTemplate(
    input_variables=["input_text", "entities"],
    template="""
    In the following you are given a sentence with multiple entities and their respective sentiments. 
    Please say if the sentiment on an entity is positive, negative or neutral.

    Sentence: "{input_text}"

    Terms:
    {entities}

    Respond in the following format:
    "entity_name" : "positive" | "negative" | "neutral",
    ...

    """
)

prompt_2_zeroshot = PromptTemplate(
    input_variables=["input_text",  "entities"],
    template="""
    Please Analyze this customer survey response to determine the sentiment towards the different aspects in the response.
    Please ONLY determine if the sentiment is positive, negative or neutral.

    Sentence: "{input_text}"

    {entities}

    Respond in the following format:
    "entity_name" : "positive" | "negative" | "neutral",
    ...

    

    """)

prompt_3_zeroshot_single_term = PromptTemplate(
    input_variables=["input_text", "entity"],
    template="""
    {input_text}

    What is the sentiment on {entity}? Only respond with "positive", "negative" or "neutral" as one word. 
    """)