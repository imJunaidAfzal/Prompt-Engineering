# Prompt Engineering
## Text-to-Image Models and Prompt Engineering
Text-to-image models are a type of machine learning model that are trained to generate images from text descriptions. These models can be used for a variety of tasks, such as generating images from written stories or creating images from textual descriptions of objects or scenes.

Prompt engineering is the process of designing and fine-tuning the input text prompts that are used to train and evaluate text-to-image models. The goal of prompt engineering is to create prompts that are both diverse and representative of the types of images that the model will be used to generate.

One common approach to prompt engineering is to use a combination of manual curation and automated methods to create a diverse set of prompts. For example, a dataset of images and their associated captions could be manually curated to remove any duplicate or irrelevant images, and then automated methods could be used to extract additional prompts from the remaining data.

Another approach is to use a dataset of images and associated captions to train a language model, which can then be used to generate new prompts that are similar to the ones in the original dataset.

Prompt engineering is an important step in the development of text-to-image models, as the quality and diversity of the prompts used to train the model can have a significant impact on its performance.

Overall, Text-to-image models are powerful tools for creating images from text descriptions. By using prompt engineering techniques, we can create models that are able to generate high-quality images that are representative of a wide range of subjects and styles.

## Prompt Engineering for Stable Diffusion

- Prompt weighting
- Prompt Editing

## Prompt weighting
Prompt weighting is a technique supported by Stable Diffusion that gives users fine control over their prompt. Using prompt weight, you can tell Stable Diffusion where to pay more attention and where to pay less.

**Example**
```
Prompt 1: A hybrid between a Shiba inu:0.7 and a polar bear, photography, award winning, documentary, wildlife, 8k
```
The above prompt tells Stable Diffusion to emphasize Shiba Inu. So, you can expect an image that has the dominance of a Shiba Inu over a polar bear. In this case, Stable Diffusion focuses mostly on Shiba Inu and automatically applies the difference (which is 0.3) to polar bear. 

Alternatively, you can assign weights to each words in your prompt for finer control.

```
Prompt 2: a cute:0.2 hybrid between a Shiba inu:0.5 and a polar bear:0.3, photography, award winning, documentary, wildlife, 8k
```

### Things to Remember About Stable Diffusion Prompt Weighting

- By default, words with no explicit weighting have a weight of 1.0.
- The sum of all text weight has to be greater than zero. Hence, if you mentioned 0.6 for one word, the stable diffusion automatically fills the difference, which is 0.4 in this case, for other subjective word in your prompt.
- As shown in the next heading, you can also use negative weights.

## Negative Prompts

**Negative prompts can be used to remove objects, styles, and image abnormalities in pre-existing images.**

- Ugly
- Morbid
- Extra fingers
- Poorly drawn hands
- Mutation
- Blurry
- Extra limbs
- Gross proportions
- Missing arms
- Mutated hands
- Long neck
- Duplicate
- Mutilated
- Mutilated hands
- Poorly drawn face
- Deformed
- Bad anatomy
- Cloned face
- Malformed limbs
- Missing legs
- Too many fingers

## Prompt Editing

Using prompt editing we tells the model to combine different objects into one or add multiple styles.

**Example**

```
[flowers:skull:0.4], art by greg rutkowski and aubrey beardsley
```
First it generates the image of flowers and then on last 40% steps, it try to convert it into skull.

Similarly we can mentioned the **number of steps** 
**Example**

```
Let you select number_of_steps = 50 for generations.
[flowers:skull:10], art by greg rutkowski and aubrey beardsley
```

It will generate the image of flowers and on last 10 steps it try to generate the skull. 1-40 steps for flowers, remaining 40-50 steps for skull.

### Iterative Generations

We can switch between objects or styles like:
**Example**

```
Let you select number_of_steps = 50 for generations.
[flowers painted by aubrey beardsley|skull painted by greg rutkowski]
```

I will Iteratively follow flowers prompt and skull prompt.

#### We can also use the combination of them like prompt weighting in prompt editing  etc. 

## Useful sources:

- Check this [Prompt Book](https://openart.ai/promptbook) to know more about prompt engineering for stable diffusion.
- To create specific style images use [Artists names for specific styles](https://github.com/kaikalii/stable-diffusion-artists)
- [Stable Diffusion V1 Artist Styles](https://proximacentaurib.notion.site/e28a4f8d97724f14a784a538b8589e7d?v=ab624266c6a44413b42a6c57a41d828c)
- [Stable Diffusion V1 Modifier Studies](https://proximacentaurib.notion.site/2b07d3195d5948c6a7e5836f9d535592?v=b5b75a67cc52483c9965cfc141f6f582)
- [Stable Diffusion Modifiers](https://www.the-ai-art.com/modifiers)
- [Stable Diffusion Top Artists](https://www.urania.ai/top-sd-artists)
- [THE Ultimate Prompting GUIDE](https://prompthero.com/stable-diffusion-prompt-guide)

