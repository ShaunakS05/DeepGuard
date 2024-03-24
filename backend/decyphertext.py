import os
import json
import predictionguard as pg
# pip install predictionguard

#thekey = os.environ.get('INTEL_KEY')
os.environ["PREDICTIONGUARD_TOKEN"] = "q1VuOjnffJ3NO2oFN8Q9m8vghYc84ld13jaqdF7E"
#os.environ['PREDICTIONGUARD_TOKEN'] = thekey


def textDetection(context, text, person):

    prompt = (
      "You are an expert in detecting words from speeches, conversations, and other audio sources that are created from AI or deepfakes. "
      "You work alongside other experts who are also working on detecting AI or deepfakes influence in media. Each expert gives a score that "
      "represents their confidence that the work is from AI or deepfakes, from 1 - 10. Although text is the hardest to know whether something "
      "is fake since it has the least amount of information, the score you give is still important in determining the validity of the media."
      "Specifically, your task is to determine if this text is something that {person} would say. "
      "The text is taken from an audio of {person} speaking within the context: {context}. "
      "Please provide a score from 1 to 10, with 1 being definitely real and something that {person} would say, and 10 being definitely "
      "AI / deepfake. Consider the following factors when assigning your score: "
      "1. Tone and language typical of {person}'s speeches. "
      "2. Consistency with known statements made by {person}. "
      "3. Contextual relevance within the given context. "
      "4. Whether the sentiment and message align with {person}'s public persona and beliefs. "
      "Please provide your score and explanation as a JSON object"   
    )

    content = ("The context is: {context}. The text being said is: {text}. " 
            " Give a confidence score from 1 - 10 if this text sounds like something donald trump would say.")

    messages = [
        {
            "role": "system",
            "content": prompt
        },
        {
            "role": "user",
            "content": content
        }
    ]

    result = pg.Chat.create(
        model="Neural-Chat-7B",
        messages=messages
    )

    try:
        # Accessing the first choice and its message content
        response_content = result['choices'][0]['message']['content']
        print(response_content)  # This will print only the message content
    except KeyError:
        print("Error accessing the response content.")

