import openai
openai.api_key = "YOUR_API_KEY"

def language_translator(text, source_language, target_language):

    # Copy code from playground and create a text file, to keep the code clean.
    prompt = open("language_translator_prompt.txt", "r").read() 
    prompt = prompt.replace("{Language-1}", source_language)  # Replacing input language tag.
    prompt = prompt.replace("{Language-2}", target_language)  # Replacing output language tag.
    prompt = prompt.replace("{Your-text-here}", text)  # Replacing text-input with user text.

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.4,  # More temperature means more randomness.
    max_tokens=256,  # Max output (4 tokens approx 1 word)
    stop=[f"Text-in-{source_language}"]  # to stop unnecessary generation
    )
    return response['choices'][0]['text']

if __name__ == "__main__":
    # Example text-input.
    text = "Hello, how are you?"

    # Example language tags.
    source_language = "English"
    target_language = "Arabic"

    output = language_translator(
      text=text
      source_language=source_language
      target_language=target_language
    )
    print(f"Text in {source_language} is:\n{text}")
    print(f"Text in {target_language} is:\n {output}")