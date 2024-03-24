import os
import json
import predictionguard as pg

# Set the PredictionGuard token
os.environ["PREDICTIONGUARD_TOKEN"] = "q1VuOjnffJ3NO2oFN8Q9m8vghYc84ld13jaqdF7E"

def get_author_sentiment(scraped_content, person):
    prompt = (
        f"Analyze, from a rating of 1-3, how biased is this article against {person}. Only return an integer."
    )

    messages = [
        {
            "role": "system",
            "content": prompt
        },
        {
            "role": "user",
            "content": scraped_content
        }
    ]

    try:
        result = pg.Chat.create(
            model="Neural-Chat-7B",
            messages=messages
        )
        # Accessing the first choice and its message content
        response_content = result['choices'][0]['message']['content']
        return response_content  # This will return the message content as a string
    except KeyError as e:
        return f"Error accessing the response content"
    except Exception as e:
        return f"An unexpected error occurred"

# # Example article for demonstration
# fake_article = """
# In a recent turn of events, former President Donald Trump has expressed his views on global economics, stating, "We need to take immediate action to improve our trade policies." Furthermore, he added, "The current situation is not sustainable," highlighting his concerns regarding the ongoing financial trends. Critics argue that his approach may be too aggressive, yet supporters believe it is necessary for long-term growth.
# """

# # Call the function and print its return value for demonstration
# response = get_author_sentiment(fake_article, "Donald Trump")
# print(response)
