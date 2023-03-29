import os
import openai
import wandb

OPENAI_API_KEY=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

openai.api_key = os.getenv("OPENAI_API_KEY")

gpt_prompt = "Topic:Cody's date with highschool crush Karen \nThousand words Love Story:"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt= gpt_prompt,
  temperature=0.8,
  max_tokens=600,
  top_p=1.0,
  frequency_penalty=0.5,
  presence_penalty=0.0
)


print(response['choices'][0]['text'])


prediction_table.add_data(gpt_prompt,response['choices'][0]['text'])
