# helper-dude
My personal ai assistant based on langchain, gpt4all, and other open source frameworks

## Goals
- Locally-run gpt with gpt4all and langchain
- An easy-to-use terminal ui with config files (no gui or webapp)
- Customizable chatbots
- Long-term vector memory (via langchain)
- Internet access

## Scope
_Note: This is really just an experiment and me poking around with this stuff for fun!_

This seems to fill a niche I didn't find already implemented with a few quick Google searches: an internet-connected local gpt chatbot with vector database memory.
That doesn't mean someonw else hasn't already done it, and I also have almost no idea what I'm doing.

This is just a hobby project :)

**I really don't have time to work on this right now; maybe I'll get back to it someday.**


## Model
Models are not provided in this repository because I did not create them (obviously).

Here are the steps that worked for me in order to prepare a model:

1. Download a model (like gpt4all-lora-quantized.bin)

2. Download `tokenizer.model` from here: <https://huggingface.co/decapoda-research/llama-7b-hf/blob/main/tokenizer.model>


3. Convert the model:
    ```Bash
    pyllamacpp-convert-gpt4all gpt4all-lora-quantized.bin tokenizer.model gpt4all-model.bin
    ```
