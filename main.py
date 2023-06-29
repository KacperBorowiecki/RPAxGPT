import os
import openai
import json
from Classes.BuisnessAnalyst import BusinessAnalyst
from Classes.RPADeveloper import RPADeveloper


# get api key from env_variables
openai.api_key = os.environ["OPENAI"]
# init agents
analyst = BusinessAnalyst(system_prompt=open("Prompts/BusinessAnalyst.txt" , "r").read())
developer = RPADeveloper(system_prompt=open("Prompts/RPADeveloper.txt" , "r").read())

# ask user for the task to do
task = input("Hi. Tell me what whould you like to automate. For example write 'I would like to create word file on desktop'.\n")
analyst.add_message(role="user", content=task)
analyst.analyze()

developer_task = analyst.get_task_for_developer()
developer.add_message(role="user", content=f"'{developer_task}'")
response_dev = developer.api_call()
print("-----------RESPONSE-----------")
print(response_dev,"\n\n\n")
print("-----------CODE-----------")
print(response_dev["code"])
execute = input("Do you want me to execute the code? Type 'Y' if yes. Otherwise NO.\n")
if execute.lower() == "y":
    exec(response_dev["code"])
    print("Code has been executed")






