# Prompt Engineering
## Text-to-Image Models and Prompt Engineering
Text-to-image models are a type of machine learning model that are trained to generate images from text descriptions. These models can be used for a variety of tasks, such as generating images from written stories or creating images from textual descriptions of objects or scenes.

Prompt engineering is the process of designing and fine-tuning the input text prompts that are used to train and evaluate text-to-image models. The goal of prompt engineering is to create prompts that are both diverse and representative of the types of images that the model will be used to generate.

One common approach to prompt engineering is to use a combination of manual curation and automated methods to create a diverse set of prompts. For example, a dataset of images and their associated captions could be manually curated to remove any duplicate or irrelevant images, and then automated methods could be used to extract additional prompts from the remaining data.

Another approach is to use a dataset of images and associated captions to train a language model, which can then be used to generate new prompts that are similar to the ones in the original dataset.

Prompt engineering is an important step in the development of text-to-image models, as the quality and diversity of the prompts used to train the model can have a significant impact on its performance.

Overall, Text-to-image models are powerful tools for creating images from text descriptions. By using prompt engineering techniques, we can create models that are able to generate high-quality images that are representative of a wide range of subjects and styles.

# Prompt Engineering for Stable Diffusion

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

It will Iteratively follow flowers prompt and skull prompt.

#### We can also use the combination of them like prompt weighting in prompt editing  etc.

## Some useful prompts settings keywords

### lighting
accent lighting, ambient lighting, backlight, blacklight, blinding light, candlelight, concert lighting, crepuscular rays, direct sunlight, dusk, Edison bulb, electric arc, fire, fluorescent, glowing, glowing radioactively, glow-stick, lava glow, moonlight, natural lighting, neon lamp, nightclub lighting, nuclear waste glow, quantum dot display, spotlight, strobe, sunlight, ultraviolet, dramatic lighting, dark lighting, soft lighting, gloomy

### Detail

highly detailed, grainy, realistic, unreal engine, octane render, bokeh, vray, houdini render, quixel megascans, depth of field (or dof), arnold render, 8k uhd, raytracing, cgi, lumen reflections, cgsociety, ultra realistic, volumetric fog, overglaze, analog photo, polaroid, 100mm, film photography, dslr, cinema4d, studio quality

### artistic techniques and materials

Digital art, digital painting, color page, featured on pixiv (for anime/manga), trending on artstation, precise line-art, tarot card, character design, concept art, symmetry, golden ratio, evocative, award winning, shiny, smooth, surreal, divine, celestial, elegant, oil painting, soft, fascinating, fine art

### camera view and quality

ultra wide-angle, wide-angle, aerial view, massive scale, street level view, landscape, panoramic, bokeh, fisheye, dutch angle, low angle, extreme long-shot, long shot, close-up, extreme close-up, highly detailed, depth of field (or dof), 4k, 8k uhd, ultra realistic, studio quality, octane render,

### style and composition

Surrealism, trending on artstation, matte, elegant, illustration, digital paint, epic composition, beautiful, the most beautiful image ever seen,

### colours

Triadic colour scheme, washed colour

### Keep in mind

This could be easily the most difficult part. Ironic, huh? But it’s true – we find ourselves sometimes struggling with the fact that we have this image in our heads and not enough or accurate words to describe it. Therefore, the AI will give us an image maybe close enough to our idea but not entirely.

**Here are some tips that may help you with this blocking:**

- Order matters!!! 
- Just keep in mind order matters – words near the front of your prompt are weighted more heavily than the things in the back of your prompt.
- If you’re still using the word **“very”** before any other word, **STOP IT. IMMEDIATELY**. Try to find an accurate word instead of adding “very” to everything in order to highlight it. There is this website that might help you out with this.
- Try to follow this steps: content type > description > style > composition.
- Content type: What type of artwork you want to achieve? Is it a photograph, drawing, sketch, 3D render..?
- Description: define the subject, subject attributes, environment/scene. The more descriptive you are with the use of adjectives, the better the output.
- Style: we’ve seen the most common ones above, but there are also “sub-categories” – lightning, detail…
- Composition: it refers to aspect ratio, camera view and resolution.

## SD Setting

This is quite a technical concept. It’s an option you can choose when generating images in Stable Diffusion. In short: the output looks more or less the same no matter which sampling method you use, the differences are very subtle and it shouldn’t matter much which one you select. Some people say there are three groups: group A (DDIM, Euler, DPM2, HEUN, LMS, DPM_adaptive and PLMS) is more soft and artsy; group B (DPM_fast) gives more variety and random results; and group C (DPM2, Euler_a) gives results that are a bit more photorealistic and clear. To recap: if you want soft and artsy, you could use DPM_adaptive or DDIM; if you want variety go for DPM_fast; and if you’re looking for photorealism try DPM2 or Euler_a.

### Seed

used to limit randomness. Generations with the same prompt, params and seed will result in the same image.


### Steps
how many steps to spend generating (diffusing) your image. More steps, more image quality and time to generate.


## Useful sources:

- Check this [Prompt Book](https://openart.ai/promptbook) to know more about prompt engineering for stable diffusion.
- To create specific style images use [Artists names for specific styles](https://github.com/kaikalii/stable-diffusion-artists)
- [Stable Diffusion V1 Artist Styles](https://proximacentaurib.notion.site/e28a4f8d97724f14a784a538b8589e7d?v=ab624266c6a44413b42a6c57a41d828c)
- [Stable Diffusion V1 Modifier Studies](https://proximacentaurib.notion.site/2b07d3195d5948c6a7e5836f9d535592?v=b5b75a67cc52483c9965cfc141f6f582)
- [Stable Diffusion Modifiers](https://www.the-ai-art.com/modifiers)
- [Stable Diffusion Top Artists](https://www.urania.ai/top-sd-artists)
- [THE Ultimate Prompting GUIDE](https://prompthero.com/stable-diffusion-prompt-guide)

