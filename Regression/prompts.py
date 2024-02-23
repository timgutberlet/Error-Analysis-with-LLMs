from langchain.prompts import PromptTemplate

zero_shot = PromptTemplate(
input_variables=[],
template=
"""System: Based on the provided attributes of a used car listed below, please predict its selling price in Indian Rupees in the Indian market. The predicted price should be expressed solely as a number followed by the currency "INR".
Ensure that the output contains no additional text or characters beyond this specified format.
Attributes:
name: {name},
year: {year},
km_driven: {km_driven},
fuel: {fuel},
seller_type: {seller_type},
transmission: {transmission},
owner: {owner},
mileage: {mileage},
engine: {engine},
max_power: {max_power},
torque: {torque},
seats: {seats}

Required Output:
"price": <predicted price> INR

Please provide the prediction strictly adhering to the above instructions.""")

few_shot = PromptTemplate(
input_variables=[],
template=
"""Example 1:
{example_1}

Example 2:
{example_2}

Example 3:
{example_3}

System: Based on the provided attributes of a used car listed below, please predict its selling price in Indian Rupees in the Indian market. The predicted price should be expressed solely as a number followed by the currency "INR".
Ensure that the output contains no additional text or characters beyond this specified format.
Attributes:
name: {name},
year: {year},
km_driven: {km_driven},
fuel: {fuel},
seller_type: {seller_type},
transmission: {transmission},
owner: {owner},
mileage: {mileage},
engine: {engine},
max_power: {max_power},
torque: {torque},
seats: {seats}

Required Output:
"price": <predicted price> INR

Please provide the prediction strictly adhering to the above instructions.""")

