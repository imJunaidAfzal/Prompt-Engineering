# Prompting Engineering

## Resources 
- [Google-Prompt-Examples](https://developers.generativeai.google/prompt-gallery)
## GPT-3 / GPT-4 / Chat-GPT Prompting

GPT-3 Large language model (175B Params) and trained on internet (till end of 2021), Audio books, hard books etc. We can perform any NLP base task using it like Classification, text generation, QA, AI assistant, feature extraction etc.

<img
  src="images\OpenAI-GPT-3.png"/>

Here's the best practices to use the gpt-3 to build the most AI base apps most efficiently. You can access playground here: [OpenAI Playground](https://platform.openai.com/playground). Select completion model from right and select GPT-3.

## Prompting methodology

<img src="images\tree-of-thought.png"/>

### The Chain-of-Thought (CoT) methodology
The Chain-of-Thought (CoT) methodology significantly bolsters the cognitive performance of AI models by segmenting complex tasks into more manageable steps. By adopting this prompting strategy, AI models can demonstrate heightened cognitive abilities and offer a deeper understanding of their reasoning processes.

This approach is an example of prompt-based learning, and it requires feeding the model with questions and their corresponding solutions before posing related subsequent questions to it. In other words, our CoT prompt teaches the model to reason about the problem and mimic the same reasoning to respond to further queries correctly.

It is observed that by using one of following prompts, the results and reasoning of LLMs increases greatly. Its known as `Chain-of-Thought approach`
```
Let's think step by step.
Let's work this out in a step-by-step way to be sure we have the right answer.
```

### The Tree-of-Thought approach to Prompt Engineering
At its core, Chain-of-Thought prompting solicits a step-by-step thinking process from the LLM. Compared to the naive/standard/Input-Output prompting, we get far better results with it.

There are some limitations, however. In a research paper (i.e., arXiv:2305.10601), Yao et al. compared various approaches to prompting, including naive prompting, CoT, as well as a new technique called Tree-of-Thought (ToT), as shown in their image below.

For example, in the Game of 24, GPT-4 with Chain-of-Thought prompting solved only 4% of tasks. In comparison, their ToT approach achieved a success rate of 74%.

The researchers remarked that the CoT didn't perform as well as it “lacks mechanisms to try different clues, make changes to decisions, or backtrack.”

And that's the main limitation of CoT. When considering a complex problem, humans (well, systematic and logical ones, at least) tend to explore a tree of thoughts, evaluating what works and what doesn't, backtracking if needed, jumping back to a previous “node” in the tree if it was more beneficial or promising for the resolution of the problem.


### GPT-3 prompting types

You can build the apps using 3 main prompting types:
* **Zero-shot (For simple tasks)** 
* **1-shot (If zero-shot fails)**
* **Few-shot (Complex tasks)**

In zero-shot we do not provide any examples and try to achieve our goal just using system prompt.
In one-shot we add one example for our usecase to make things clear.
In Few-shot we add multiple exampples to make sure our system understands our usecase. This type is used in handling complex usecase where system prompt unable to teach our usecase to gpt-3.

## GPT-3 zero-shot prompting

In the zero-shot we only expalin our main purpose, what we want to do, in this we do not provide any examples. For example lets say we want to create language translator. Its zero-shot prompt looks like this:
Here's a simple example of zero-shot prompting.
**Prompt (Language Translator)**
```
This is language translator tool, it takes input in English and returns output in German language.
Text-in-English: {Your-text-here}
Text-in-German:
```
->GPT-3 will return the output in German language. Sometimes, it start to generate the unnecessary texts, so we can add **Stop Sequence** in setting (at right side of playground). In our case it can be `Text-in-English:`

Now lets make it general (For any to any language).

**General Prompt (Language Translator, Any-To-Any Language)**
We will use the multiple taging to achieve this goal.

**Prompt**
```
This is language translator tool, it takes input in {Language-1} and returns output in {Language-2} language.

Text-in-{Language-1}: {Your-text-here}
Text-in-{Language-2}:
```
Replace tags with languages when you're going to integrate it in app. 

**API example witn python**

**Install openai**
```
pip install openai --upgrade
```


```python
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

```

## GPT-3 One-shot prompting
[COMMING SOON]
## GPT-3 Few-shot prompting
[COMMING SOON]
