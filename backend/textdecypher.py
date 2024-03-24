import openai 
# OpenAI.api_key = "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"

# client = openai.OpenAI(api_key = "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")
client = openai.OpenAI(api_key = "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")
# Define our prompt.
person = "Ariana Grande"

#context = "Joe Rogan discusses how the Pyramids were built on his podcast. Joe's podcast is known for being informal and laidback. Enderman are creatures from Minecraft. Enderman can only exist in a video game and do not exist in real life. They cannot build pyramids."
#text = "its hard to say theres a lot of candidates. You know Ive always said mighty mouse is one of my best bets because he was so goddamn good and he's still so goddamn good now but now he's fighting in one FC but he was a flyweight champion for a long time. "
#text = "Hi, Allure, it's Ariana Grande. And today I'm gonna be breaking down some of my most iconic videos. By the way, they told me to use the word iconic. I didn't assume that"
text = "I love minecraft. I play valorant. I am an e-girl. I meow after every kill"

#text = "When I started kickboxing that's when I started getting like brain damage. And I was realizing I was getting brain damage cuz we were sparring hard, laying in bed with headaches after, and and there was no money in it and I was like what am I doing."
# text = "So when you think about it, it's entirely possible that it may have been Enderman who were responsible for the construction of the pyramids. Becuase when you look at the sheer weight of these stones that were stacked on top of each other, it doesn't make sense. There needs to be another explanation."
#########################
prompt = (
    #"Based on your knowledge, has {person} said this quote before: {text}? If you are unsure, think whether it is likely that {person} would discuss this topic. Please provide a number 1 - 5 in json."
    "Based on your knowledge, think about the subject that " +  str(person) + " is commonly known for. Does the subject matter in {text} align with the topics that " + str(person) + " usually talks about? Look for satire and what is plausible in real life. Please provide your answer in json."
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

print(response.choices[0].message.content)
