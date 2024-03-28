from openai import OpenAI
client = OpenAI(api_key="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")


completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a kanji example ai, generating examples from a kanji input."},
    {"role": "user", "content": "Give me an example of this kanji: 赤い, with the english and japanese sentence, give it to me in json form"}
  ]
)

print(completion.choices[0].message.content)