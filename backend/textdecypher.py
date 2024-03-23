from openai import OpenAI
# OpenAI.api_key = "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"

client = OpenAI(api_key="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")

context = ("Former president Donald Trump is being interviewed after current president Joe Biden's state of the union address. Compared to Biden's speech, Trump"
"is asked what his vision for the country is since he plans on running in the next presidential election")

text = ("I disagree with many points of Biden's speech. Personally, I love to eat shit. Shit from public restroooms more specifically. I wait until I find a slightly overweight asian man. I then follow him to the bathroom and secretly watch him take a shit. Then I eat it.")

prompt = (
    "You are an expert in detecting words from speeches, conversations, and other audio sources that are created from AI or deepfakes. "
    "You work alongside other experts who are also working on detecting AI or deepfakes influence in media. Each expert gives a score that "
    "represents their confidence that the work is from AI or deepfakes, from 1 - 10. Although text is the hardest to know whether something "
    "is fake since it has the least amount of information, the score you give is still important in determining the validity of the media."
    "Specifically, your task is to determine if this text is something that Donald Trump would say. "
    "The text is taken from an audio of Donald Trump speaking within the context: {context}. "
    "Please provide a score from 1 to 10, with 1 being definitely real and something Donald Trump would say, and 10 being definitely "
    "AI / deepfake. Consider the following factors when assigning your score: "
    "1. Tone and language typical of Donald Trump's speeches. "
    "2. Consistency with known statements made by Donald Trump. "
    "3. Contextual relevance within the given context. "
    "4. Whether the sentiment and message align with Donald Trump's public persona and beliefs. "
    "Please provide your score and explanation as a JSON object. Then also provide a one sentence explanation on why you gave that score, also as a JSON object"
)

content = ("The context is: {context}. The text being said is: {text}. " 
           " Give a confidence score from 1 - 10 if this text sounds like something donald trump would say. Then DO NOT FORGET TO give a sentence explaining why you gave this score. PLEASE GIVE A SENTENCE EXPLAINING WHY YOU GAVE THIS SCORE AFTER")

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  response_format={ "type": "json_object" },
  messages=[
    {"role": "system", "content": prompt},
    {"role": "user", "content": content}
  ]
)

print(response.choices[0].message.content)