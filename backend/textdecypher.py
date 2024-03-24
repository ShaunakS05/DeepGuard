import openai 
from texttospeech import *

client = openai.OpenAI(api_key = "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")

def textDetection(person, text, context):

  prompt = (
      "Based on your knowledge, think about the subject that " +  str(person) + " is commonly known for. Does the subject matter in {text} align with the topics that " + str(person) + " usually talks about? The context is: " + str(context) + ". Look for satire and what is plausible in real life. Please provide your answer in json."
  )

  content = ("Provide a numerical answer (1 being definitely never aligns, 2 being probably never aligns, 3 being neutral either way, 4 being probably aligns, and 5 being definitely aligns.) Then, give an explanation of why {person} aligns with the {text} in json")

  response = client.chat.completions.create(
    model="gpt-4-turbo-preview",
    response_format={ "type": "json_object" },
    messages=[
          {"role": "system", "content": prompt.format(text=text)},
          {"role": "user", "content": content.format(person=person, text=text)}
      ]
  )
  # print(response.choices[0].message.content)
  return(response.choices[0].message.content)

