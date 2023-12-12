# Prompt Engineering

### SD-XL Demo Free

| Colab Link                                                                                     | Description             |
|-----------------------------------------------------------------------------------------------|-------------------------|
| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1wCJ7WN9zeQtgexp-40sOXZj4VtCvX0wg?usp=sharing) | SD XL base (Slow inference)        |
| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1BuyvCTWv_i_Qj95ueyX9wx0O5Tr1zd7g?usp=sharing)                | SD-XL (LCM-LoRa) Fast Inference    |


## Text-to-Image Models and Prompt Engineering

### Models

| SR#  | Sample Image                                      | Model Name                                                                                                                |
|------|--------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| 1    | <img src="images\model_imgs\riot_diffusion.jpeg" width="80px"/>             | [Riot Diffusion XL (Riot Games, League of Legends)](https://civitai.com/models/125151/riot-diffusion-xl-riot-games-league-of-legends)  |
| 2    | <img src="images\model_imgs\dream_sharper.png" width="80px"/>             | [DreamShaper](https://civitai.com/models/4384)                                          |
| 3    | <img src="images\model_imgs\SDVN7-RealArtXL.jpeg" width="80px"/>             | [SDVN7 RealArt XL](https://civitai.com/models/123307/sdvn7-realartxl)                                   |
| 4    | <img src="images\model_imgs\sdvn6-realxl.jpeg" width="80px"/>             | [SDVN6 RealXL](https://civitai.com/models/118114/sdvn6-realxl)                                       |
| 5    | <img src="images\model_imgs\rough_oil.jpeg" width="80px"/>             | [Envy Rough Oil XL-01](https://civitai.com/models/124533/envy-rough-oil-xl-01)                           |
| 6    | <img src="images\model_imgs\rev_anim.png" width="80px"/>             | [ReV Animated](https://civitai.com/models/7371)                                          |
| 7    | <img src="images\model_imgs\game icon.jpeg" width="80px"/>             | [Game Icon](https://civitai.com/models/123767/game-icon-instituteyanjiusuopingziv3-000020)         |

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

### Example Negative Prompt
**negative_prompt**
```
far, medium, unclear, distorted face, poor eyes, not looking at camera, not centered, dirty teeth, duplicate, separate, out of frame, half person, cartoon, 3d, multiple frames, color background, low quality,((disfigured)), ((bad art)), ((deformed)),((extra limbs)), ((extra barrel)),((b&w)), weird colors, blurry, (((duplicate))), ((morbid)), ((mutilated)), [out of frame], extra fingers, mutated hands, ((poorly drawn hands)), ((poorly drawn face)), (((mutation))), (((deformed))), ((ugly)), blurry, ((bad anatomy)), (((bad proportions))), ((extra limbs)), cloned face, (((disfigured))), out of frame, ugly, extra limbs, (bad anatomy), gross proportions, (malformed limbs), ((missing arms)), ((missing legs)), (((extra arms))), (((extra legs))), mutated hands, (fused fingers), (too many fingers), (((long neck))), (((tripod))), (((tube))), Photoshop, video game, ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, mutation, mutated, extra limbs, extra legs, extra arms, disfigured, deformed, cross-eye, body out of frame, blurry, bad art, bad anatomy, 3d render, (((umbrella))), (ugly eyes, deformed iris, deformed pupils, fused lips and teeth:1.2), (un-detailed skin, semi-realistic, cgi, 3d, render, sketch, cartoon, drawing, anime:1.2), text, close up, cropped, out of frame, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck
```

**negative_prompt**
```
done by bad-artist, ugly, dazed, light blue eyes, 3D render, 3D game, 3D game scene, 3D character, mosaic, painting, illustration, digital art, cartoon, anime, doll, toy, photoshop, video game, surreal, sign, 3dcg, decorating, decoration, crayon, clipart, cgi, rendered, 3d, cartoon face, drawing, cgstation, airbrushed, sketch, render, unreal engine, blender, digital painting, airbrush, pointillism, painting, image compression, distorted, JPEG artifacts, noisy, shaky, pixelated, unclear, artifacts, low detail, low quality, low resolution, distortion, amateur, low res, low-res, cropped body, cut off, basic, boring, botched, unprofessional, draft, failure, fake, image corruption, irregular, uneven, unnatural, contorted, twisted, unappealing, blurry, haze, worst quality, normal quality, bad shadow, poor quality, amateur photography, tasteless, tacky, lacklustre, simple, plain, grainy, out of focus, fuzzy, cropped, uncentered, out of frame, body out of frame, split image, truncated, disjointed, incoherent, disorganized, jumbled, floating, objects, unreal, deformations, kitsch, unattractive, opaque, boring pose, plain background, boring, plain, standard, average, uninventive, derivative, homogenous, uncreative, ineffective, drab, amateur, censor, censored, censor_bar, text, font, ui, error, watermark, username, signature, QR code, bar code, copyright, logos, HUD, tiling, label, watermarks, calligraphy, kanji, hanzi, hangul, hanza, chu, nom, latin, arabic, cyrillic, symbols, alphanumeric, unicode, script, artist name, logo, censor, high contrast, low contrast, High pass filter, watermarked, monotone, smooth, blur, vignette, filter, writing, oversaturation, over saturation, over shadow, gaussian, blurred, weird colors, blurred, grain, bad art, black-white, posterization, colour banding, grayscale, monochrome, b&w, oversaturated, black and white, no color, greyscale, poorly drawn, messy drawing, bad proportions, gross proportions, imperfection, dehydrated, misshappen, duplicate, double, clones, twins, brothers, same face, repeated person, bad anatomy, anatomical nonsense, malformed, misshaped body, uncoordinated body, unnatural body, long body, liquid body, deformed, mutilated, mutation, mutated, tumor, deformed body, lopsided, mangled, skin defect, disfigured, conjoined, connected, intertwined, hooked, bad body, amputation, siamese, cropped head, bad framing, out of shot, awkward poses, unusual poses, smooth skin, misshapen, gross proportions, poorly drawn face, bad face, fused face, cloned face, big face, long face, dirty face, long neck, warped face, loose face, crooked face, asymetric jaw, asymmetric chin, fake face, deformed face, extra heads, big forehead, head cut off, ugly hair, bald, poorly drawn hair, bad drawn eyes, asymmetric eyes, unaligned eyes, crooked eyes, closed eyes, looking_away, fused eyes, poorly drawn eyes, extra eye, cross eyed, imperfect eyes, cataracts, glaucoma, strabismus, heterochromia, woobly iris, square iris, weird eyes, distorted eyes, deformed glasses, extra eyes, bright blue eyes, cross-eyed, blurry eyes, poorly drawn eyes, fused eyes, blind, red eyes, bad eyes, ugly eyes, dead eyes, bad drawn nose, fused nose, poorly drawn nose, extra nose, bad mouth, fused mouth, poorly drawn mouth, big mouth, mouth cake, cracked mouth, crooked lips, dirty teeth, yellow teeth, ugly teeth, liquid tongue, colorful tongue, black tongue, bad tongue, tongue within mouth, too long tongue, crooked teeth, yellow teeth, long teeth, bad teeth, fused ears, bad ears, poorly drawn ears, extra ears, liquid ears, heavy ears, missing ears, asymmetric ears, big ears, ugly ears, bad collarbone, fused collarbone, missing collarbone, liquid collarbone, missing limb, malformed limbs, extra limb, floating limbs, disconnected limbs, extra limb, amputee, extra limbs, different limbs proportions, decapitated limbs, mutated hands, poorly drawn hands, malformed hands, bad hands, fused hands, missing hand, extra hand, mangled hands, more than 1 left hand, more than 1 right hand, less than two hands appearing in the image, cropped hands, out of frame hands, thousand hands, mutated hands and fingers, missing hands, distorted hands, deformed hands, imperfect hands, undetailed hands, fused fingers, mutated fingers, (tentacle finger), missing fingers, one hand with more than 5 fingers, disfigured hands, one hand with less than 5 fingers, one hand with more than 5 digit, one hand with less than 5 digit, extra digit, fewer digits, fused digit, missing digit, bad digit, liquid digit, extra fingers, too many fingers, bad gloves, poorly drawn gloves, fused gloves, disappearing arms, short arm, missing arms, extra arms, less than two arms appearing in the image, cropped arms, out of frame arms, long arms, deformed arms, short arm, different arms proportions, multiple belly buttons, missing belly button, broken legs, disappearing legs, missing legs, extra legs, more than 2 legs, huge thighs, disappearing thigh, missing thighs, extra thighs, more than 2 thighs, deformed legs, bad thigh gap, missing thigh gap, fused thigh gap, liquid thigh gap, poorly drawn thigh gap, huge calf, disappearing calf, missing calf, extra calf, fused calf, bad knee, extra knee, broken legs, different legs proportions, mutated feet, poorly drawn feet, malformed feet, bad feet, fused feet, missing feet, mangled feet, more than 1 left foot, more than 1 right foot, less than two foot appearing in the image, cropped feet, thousand feet, mutated feet and fingers, missing feet, distorted feet, deformed feet, imperfect feet, undetailed feet, ugly feet, extra foot, long toes, extra shoes, bad shoes, fused shoes, more than two shoes, poorly drawn shoes, fused cloth, poorly drawn cloth, multiple breasts, fused breasts, bad breasts, huge breasts, poorly drawn breasts, extra breasts, liquid breasts, missing breasts, more than 2 nipples, missing nipples, different nipples, fused nipples, bad nipples, poorly drawn nipples, black nipples, colorful nipples, unnatural nipples, without form nipples, withered nipples, unerect nipples, extra nipples, more than two nipples, imperfect nipples
```


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

## Sample Generated Images
**Settings**

```
prompt:Highly detailed Portrait of BlackOps man with ((cat head)), ((Golden suit)), (dangerous), ((uhd)), ((war zone)), ((Foggy background)), 8k, ((insance details))
seed: 49376049
height: 768
width: 512
num_inference_steps: 80
guidance_scale: 7.5
negative_prompt:far, unclear, distorted face, (text), poor eyes, not looking at camera, not centered, dirty teeth, duplicate, separate, out of frame, half person, cartoon, 3d, multiple frames, color background, low quality,((disfigured)), ((bad art)), ((deformed)),((extra limbs)), ((extra barrel)),((b&w)), weird colors, blurry, (((duplicate))), ((morbid)), ((mutilated)), [out of frame], extra fingers, mutated hands, ((poorly drawn hands)), ((poorly drawn face)), (((mutation))), (((deformed))), ((ugly)), blurry, ((bad anatomy)), (((bad proportions))), ((extra limbs)), cloned face, (((disfigured))), out of frame, ugly, extra limbs, (bad anatomy), gross proportions, (malformed limbs), ((missing arms)), ((missing legs)), (((extra arms))), (((extra legs))), mutated hands, (fused fingers), (too many fingers), (((long neck))), (((tripod))), (((tube))), Photoshop, video game, ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, mutation, mutated, extra limbs, extra legs, extra arms, disfigured, deformed, cross-eye, body out of frame, blurry, bad art, bad anatomy, 3d render, (((umbrella))), (ugly eyes, deformed iris, deformed pupils, fused lips and teeth:1.2), (un-detailed skin, semi-realistic, 3d, render, sketch, cartoon, drawing, anime:1.2), text, close up, cropped, out of frame, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck
```
<img
  src=https://github.com/imJunaidAfzal/Prompt-Engineering/blob/main/images/28_5.jpg
  alt="image"
  style="display: inline-block; margin: 0 auto; max-width: 200px">
  
  
**Settings**

```
prompt: Highly detailed Portrait of ((Vikings Ironman)), ((beast)), (dangerous), ((uhd)), ((war zone)), (((destroyed city in background))), 8k, ((insance details)), cinematic dark lighting
seed: 49876717
height: 944
width: 768
num_inference_steps: 80
guidance_scale: 8
negative_prompt:far, unclear, distorted face, (text), poor eyes, not looking at camera, not centered, dirty teeth, duplicate, separate, out of frame, half person, cartoon, 3d, multiple frames, color background, low quality,((disfigured)), ((bad art)), ((deformed)),((extra limbs)), ((extra barrel)),((b&w)), weird colors, blurry, (((duplicate))), ((morbid)), ((mutilated)), [out of frame], extra fingers, mutated hands, ((poorly drawn hands)), ((poorly drawn face)), (((mutation))), (((deformed))), ((ugly)), blurry, ((bad anatomy)), (((bad proportions))), ((extra limbs)), cloned face, (((disfigured))), out of frame, ugly, extra limbs, (bad anatomy), gross proportions, (malformed limbs), ((missing arms)), ((missing legs)), (((extra arms))), (((extra legs))), mutated hands, (fused fingers), (too many fingers), (((long neck))), (((tripod))), (((tube))), Photoshop, video game, ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, mutation, mutated, extra limbs, extra legs, extra arms, disfigured, deformed, cross-eye, body out of frame, blurry, bad art, bad anatomy, 3d render, (((umbrella))), (ugly eyes, deformed iris, deformed pupils, fused lips and teeth:1.2), (un-detailed skin, semi-realistic, 3d, render, sketch, cartoon, drawing, anime:1.2), text, close up, cropped, out of frame, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck
```
<img
  src=https://github.com/imJunaidAfzal/Prompt-Engineering/blob/main/images/32_0%20(1).jpg
  alt="image"
  style="display: inline-block; margin: 0 auto; max-width: 200px">


**Settings**
```
prompt: Highly detailed Portrait of ((Vikings Ironman)), ((dark matter suit)), ((beast)), (dangerous), ((uhd)), ((war zone)), (((destroyed city in background))), (((game character))), 8k, ((insance details)), cinematic dark neon lighting
seed: 84269025
height: 944
width: 768
num_inference_steps: 80
guidance_scale: 7.5
negative_prompt:far, unclear, distorted face, (text), poor eyes, not looking at camera, not centered, dirty teeth, duplicate, separate, out of frame, half person, cartoon, 3d, multiple frames, color background, low quality,((disfigured)), ((bad art)), ((deformed)),((extra limbs)), ((extra barrel)),((b&w)), weird colors, blurry, (((duplicate))), ((morbid)), ((mutilated)), [out of frame], extra fingers, mutated hands, ((poorly drawn hands)), ((poorly drawn face)), (((mutation))), (((deformed))), ((ugly)), blurry, ((bad anatomy)), (((bad proportions))), ((extra limbs)), cloned face, (((disfigured))), out of frame, ugly, extra limbs, (bad anatomy), gross proportions, (malformed limbs), ((missing arms)), ((missing legs)), (((extra arms))), (((extra legs))), mutated hands, (fused fingers), (too many fingers), (((long neck))), (((tripod))), (((tube))), Photoshop, video game, ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, mutation, mutated, extra limbs, extra legs, extra arms, disfigured, deformed, cross-eye, body out of frame, blurry, bad art, bad anatomy, 3d render, (((umbrella))), (ugly eyes, deformed iris, deformed pupils, fused lips and teeth:1.2), (un-detailed skin, semi-realistic, 3d, render, sketch, cartoon, drawing, anime:1.2), text, close up, cropped, out of frame, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck
```
<img
  src=https://github.com/imJunaidAfzal/Prompt-Engineering/blob/main/images/31_5.jpg
  alt="image"
  style="display: inline-block; margin: 0 auto; max-width: 200px">
