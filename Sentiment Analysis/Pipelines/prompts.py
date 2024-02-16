from langchain.prompts import PromptTemplate

prompt_multi_term_zeroshot = PromptTemplate(
    input_variables=["terms",  "entities"],
    template="""Task: Analyze the sentiment of specific terms mentioned in a sentence. 
You are required to evaluate whether the sentiment towards each term is 'positive', 'negative', or 'neutral'.

Sentence: "{input_text}"

Terms:
{terms}

Return the final result as JSON in the format {{"term_sentiments": "<a list of [term, sentiment] pairs>"}}.
ONLY return the JSON.
Answer:""")


prompt_multi_term_zeroshot_instructions = PromptTemplate(
    input_variables=["terms",  "entities"],
    template="""Task: Analyze the sentiment of specific terms mentioned in a sentence. 
You are required to evaluate whether the sentiment towards each term is 'positive', 'negative', or 'neutral'.

Sentence: "{input_text}"

Terms:
{terms}

Instructions:
- Ensure to evaluate the sentiment specifically for the term mentioned, considering the adjectives and context provided in the sentence.

Return the final result as JSON in the format {{"term_sentiments": "<a list of [term, sentiment] pairs>"}}.
ONLY return the JSON.
JSON:""")

prompt_single_term_zeroshot = PromptTemplate(
    input_variables=["input_text", "entity"],
    template="""{input_text}

    What is the sentiment in the text towards '{entity}'? Only respond with "positive", "negative" or "neutral" as one word.""")