from langchain_core.prompts import PromptTemplate
from npmai import Grok
from langchain_core.output_parsers import StrOutputParser

prompt = PromptTemplate(
    input_variables=["input"],
    template="Hey you are helpfull code assistant that write code just write code nothing else of it and maintain proper indentation and no hectics just imagine you will give the code and we will execute it, you will be asked to generate code aboout a query generate code,this is the query:{input}"
)

user_actual_query = "Write a python code that create file and where you have to give notes also of NCERT Class 9th Social Science Chapter Democratic Rights right animated and fully interesting notes of this chapter you have to generate notes also and save that note with this file name Democratic Rights Notes this file is not created so create also and generate note also and save also "

llm = Grok()

parser=StrOutputParser()

chain=prompt | llm | parser
response=chain.invoke(prompt.format(input=user_actual_query))
print(response)

cleaned_response = response.strip()
if cleaned_response.startswith('```python'):
    cleaned_response = cleaned_response[len('```python'):]
if cleaned_response.endswith('```'):
    cleaned_response = cleaned_response[:-len('```')]

exec(cleaned_response.strip())
