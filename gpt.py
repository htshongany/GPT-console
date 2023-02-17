import os
import openai

from dotenv import load_dotenv

main_menu ="""
=====================_GPT-MENU_=====================
>>> help          -> Get the available command menu 
>>> add           -> Add api key
>>> exit          -> Exit the console
>>> clear or cls  -> Clean the console
>>> gpt           -> Use the gpt prompt 
====================================================
"""

gpt_menu ="""
=====================_GPT-MENU_=====================
>>> help          -> Get the available command menu 
>>> exit          -> Exit the console
>>> clear or cls  -> Clean the console
====================================================
"""

def add_key(api_key):
	with open('.env', 'w+') as file:
		file.write(f"OPENAI_API_KEY = '{api_key}'")

def load_api_key():
	load_dotenv()
	openai.api_key = os.getenv("OPENAI_API_KEY")

load_api_key()

def gpt_prompt(prompt):

	response = openai.Completion.create(

    	model="text-davinci-003",
    	prompt=f"prompt:{prompt}",
    	temperature=0.7,
    	max_tokens=4000,
    	top_p=1,
    	frequency_penalty=0,
    	presence_penalty=0,

    )

	return response["choices"][0]["text"]

def run():
	while True:
		command = input("[CMD]>>> ").lower().strip()

		if command == 'exit':
			break
		elif command == 'help':
			print(f"{main_menu}")
			continue

		elif command == 'cls' or command == 'clear':
			os.system('cls')
			continue
		elif command == 'add':
			key = input("Enter your api key : ")
			add_key(key)
			load_api_key()

		elif command == 'gpt':

			while True:
				prompt = input("[GPT]>>> ").strip().lower()

				if prompt == 'exit':
					break
				elif prompt == 'help':
					print(f"{gpt_menu}")
					continue
				elif prompt == 'cls' or prompt == 'clear':
					os.system('cls')
					continue
				try:
					print(gpt_prompt(prompt))
					
				except Exception as e:
					print(f"ERROR ({e}) : some things don't work :(")
					break 
		else:
			print(f"{command} is not a valid command : [ Use the help command ]")


if __name__=='__main__':run()