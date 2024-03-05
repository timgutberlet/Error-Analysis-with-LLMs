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

zero_shot_single_table= ChatPromptTemplate.from_messages([
    ("user", """Question:
Table A:
{Table_A}

Table B:
{Table_B}

Task: Identify if Column-A-{Column_A} in Table A and Column-B-{Column_B} in Table B are matching columns. Return "True" if they are matching and "False" if they are not.
ONLY return "True" or "False". Do not return anything else."""),
])