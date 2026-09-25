from openai import OpenAI

#defining API Key
client = OpenAI(api_key="")

#calling LLM
def call_llm(prompt):
    response=client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role":"user","content":prompt}
        ]
    )
    return response.choices[0].message.content

#Building a function to process text
def process_text(text):
    prompt=f"""
    Give me the output in 3 bullet points {text}
"""
    response=call_llm(prompt)
    return response

user_input=input("what do you want to talk about?")
# with open("input.txt","r") as file:
#    content=file.read()

result=process_text(user_input)
print(result)