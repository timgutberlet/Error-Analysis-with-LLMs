from langchain.prompts.chat import ChatPromptTemplate


#TODO: Quelle!! - https://webdatacommons.org/structureddata/smb/
zero_shot_general_prompt = ChatPromptTemplate.from_messages([
    ("system", """Description: Please identify the matching columns between Table A and Table B. For each column in Table A, specify the corresponding column in Table B. If a column in A has no corresponding column in Table B, you can map it to None. Represent each column mapping using a pair of column headers in a list, i.e., [Table A Column, Table B column or None]. Provide the mapping for each column in Table A and return all mappings in a list. Return the final result as JSON in the format {{"column_mappings": "<a list of column pairs>"}}."""),
    ("user", """Question:
Table A:
{Tabel_A}

Table B:
{Table_B}

Return the final result as JSON in the format {{"column_mappings": "<a list of column pairs>"}}.
Answer:"""),
])

#TODO: Quelle!! - https://webdatacommons.org/structureddata/smb/
zero_shot_rules_prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a data engineer and an expert in schema matching (https://en.wikipedia.org/wiki/Schema_matching).
The goal of schema matching is to discover correspondences between pairs of attributes of relational tables. A correspondence states that two attributes refer to the same schema element and thus contain values of the same type.

A pair of matching columns fulfills the following rules:
- Both columns contain semantically related values.
- Both columns contain the same type of values.
- The values in both columns have the same datatype and value range."""),
    ("user", """Below, you are given Table A and Table B:
Table A:
{Tabel_A}

Table B:
{Table_B}

Please find all pairs of matching columns. For each pair of matching columns, output the names of both columns separated by <SEP>. Use a new line for each correspondence."""),
])