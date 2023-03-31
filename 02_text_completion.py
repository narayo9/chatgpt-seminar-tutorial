import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(model="text-davinci-003", prompt="""Complete the sentence: 
The sky is""")

print(response.choices[0].text)
