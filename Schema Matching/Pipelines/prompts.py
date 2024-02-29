from langchain.prompts.chat import ChatPromptTemplate




#TODO: Quelle!! - https://webdatacommons.org/structureddata/smb/
dynamic_fewshot_multi_table= ChatPromptTemplate.from_messages([
    ("user", """Example 1: 
{example_1}

Example 2:
{example_2}
"""),
    ("system", """Description: Please identify the matching columns between Table A and Table B. 
     For each column in Table A, specify the corresponding column in Table B. 
     If a column in A has no corresponding column in Table B, you can map it to 'None'. 
     Represent each column mapping using a pair of column headers in a list, i.e., [Table A Column, Table B column or None]. 
     Provide the mapping for each column in Table A and return all mappings in a list. Return the final result as JSON in the format {{"column_mappings": "<a list of column pairs>"}}."""),
    ("user", """Question:
Table A:
{Table_A}

Table B:
{Table_B}

Return the final result as JSON in the format {{"column_mappings": "<a list of column pairs>"}}. ONLY return the JSON and nothing else.
Answer:"""),
])

#TODO: Quelle!! - https://webdatacommons.org/structureddata/smb/
fix_fewshot_multi_table= ChatPromptTemplate.from_messages([
    ("user", """Example 1: 
{example_1}

Example 2:
{example_2}
"""),
    ("system", """Description: Please identify the matching columns between Table A and Table B. 
     For each column in Table A, specify the corresponding column in Table B. 
     If a column in A has no corresponding column in Table B, you can map it to 'None'. 
     Represent each column mapping using a pair of column headers in a list, i.e., [Table A Column, Table B column or None]. 
     Provide the mapping for each column in Table A and return all mappings in a list. Return the final result as JSON in the format {{"column_mappings": "<a list of column pairs>"}}."""),
    ("user", """Question:
Table A:
{Table_A}

Table B:
{Table_B}

Return the final result as JSON in the format {{"column_mappings": "<a list of column pairs>"}}. ONLY return the JSON and nothing else.
Answer:"""),
])

zero_shot_multi_table= ChatPromptTemplate.from_messages([
    ("system", """Description: Please identify the matching columns between Table A and Table B. 
     For each column in Table A, specify the corresponding column in Table B. 
     If a column in A has no corresponding column in Table B, you can map it to 'None'. 
     Represent each column mapping using a pair of column headers in a list, i.e., [Table A Column, Table B column or None]. 
     Provide the mapping for each column in Table A and return all mappings in a list. Return the final result as JSON in the format {{"column_mappings": "<a list of column pairs>"}}."""),
    ("user", """Question:
Table A:
{Table_A}

Table B:
{Table_B}

Return the final result as JSON in the format {{"column_mappings": "<a list of column pairs>"}}. ONLY return the JSON and nothing else.
Answer:"""),
])

#TODO: Quelle!! - https://webdatacommons.org/structureddata/smb/
zero_shot_rules_prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a data engineer and an expert in schema matching (https://en.wikipedia.org/wiki/Schema_matching).
The goal of schema matching is to discover correspondences between pairs of attributes of relational tables. A correspondence states that two attributes refer to the same schema element and thus contain values of the same type.
The Values in a column are separated by '|'.
A pair of matching columns fulfills the following rules:
- Both columns contain semantically related values.
- Both columns contain the same type of values.
- The values in both columns have the same datatype and value range."""),
    ("user", """Below, you are given Table A and Table B:
Table A:
{Table_A}

Table B:
{Table_B}

Return the final result as JSON in the format {{"column_mappings": "<a list of column pairs>"}}. ONLY return the JSON and nothing else.
Answer:"""),
])




zero_shot_single_table = ChatPromptTemplate.from_messages([
    ("system", """
    You are tasked with schema matching, a process to identify if two columns from different relational tables match. Matching is established when both columns represent the same schema element, implying they contain values of the same type.  
    Given one column from Table A and one column from Table B, determine if these columns match based on their content. For two columns to be considered matching, they do not have have to have the exact same values but the only need to be same kind of datatype, value range and semantic meaning. If you see an indication of this, you can consider the columns to be matching.
    If the columns match, return True. If they do not match, return False.
    The Values in a column are separated by '|'."""),
    ("user", """Question:
Column from Table A:
{Table_A}

Column from Table B:
{Table_B}

ONLY return True or False and nothing else.
Answer:"""),
])


zero_shot_single_table_rules_prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a data engineer and an expert in schema matching.
The goal of schema matching is to discover correspondences between pairs of attributes of relational tables. A correspondence states that two attributes refer to the same schema element and thus contain values of the same type.
The Values in a column are separated by '|'.
A pair of matching columns fulfills the following rules:
- Both columns contain semantically related values.
- Both columns contain the same type of values.
- The values in both columns have the same datatype and value range."""),
    ("user", """Below, you are given a column from Table A and a column from Table B:
Column Table A:
{Table_A}

Column Table B:
{Table_B}

Please return "True" if the columns are matching and "False" if they are not. Do not return anything else."""),
])