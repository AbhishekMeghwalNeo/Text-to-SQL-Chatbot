# src/llm.py

from openai import AzureOpenAI
from src.config import Config

cfg = Config()

client = AzureOpenAI(
    api_key= cfg.api_key,
    api_version= "2025-01-01-preview",
    azure_endpoint= "https://amiparmar-test-resource.cognitiveservices.azure.com/"
)

# Function to load Azure model and provide sql query as response
def generate_sql(system_prompt: str, user_prompt, model= "gpt-4o") -> str:

    response= client.chat.completions.create(
        model= model,
        messages= [
            {
                "role" : "system",
                "content" : system_prompt
            },
            {
                "role" : "user",
                "content" : user_prompt
            }
        ]
    )

    return response.choices[0].message.content

# def generate_sql(system_prompt: str, user_prompt: str, model="gpt-4.1-mini") -> str:
#     response = client.responses.create(
#         model=model,
#         input=[
#             {"role": "system", "content": system_prompt},
#             {"role": "user", "content": user_prompt},
#         ]
#     )
#     return response.output_text.strip()


# Function to test LLM call
def llm_call_test(model= "gpt-4o") -> str:

    response= client.chat.completions.create(
        model= model,
        messages= [
            {
                "role" : "system",
                "content" : "You are a normal person"
            },
            {
                "role" : "user",
                "content" : "Say Hello"
            }
        ]
    )

    return response.choices[0].message.content

if __name__  == "__main__":

    print(llm_call_test())


