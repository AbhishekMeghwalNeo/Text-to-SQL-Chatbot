"""
Docstring for src.llm.llm_client.py

"""

from openai import OpenAI
import json
from src.config import Config
# from src.agent.tools import write_file, finish, retrieve_documents


cfg = Config()

client = OpenAI(api_key= cfg.api_key)

SYSTEM_PROMPT = """
You are just a normal person.
"""

TASK = "say hello"


def call_llm(model= "gpt-4.1-mini", system_prompt= SYSTEM_PROMPT, task= TASK):
    response = client.responses.create(
        model= model,
        input= [
                {
                    "role" : "system",
                    "content" : system_prompt
                },
                {
                    "role" : "user",
                    "content" : task
                }
            ]
    )
    return response.output_text

if __name__ == "__main__":

    output = call_llm(system_prompt= SYSTEM_PROMPT, task= TASK)

    print(output)


