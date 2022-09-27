[![Python application test with Github Actions using devcontainers](https://github.com/nogibjj/hugging-face-cli-with-codespaces/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/hugging-face-cli-with-codespaces/actions/workflows/main.yml)


# hugging-face-cli-with-codespaces
Repo that allows me to build AI tools on top of Hugging Face and OpenAI Whisper

## Try out fine-tuning

[Run this script](https://github.com/nogibjj/hugging-face-cli-with-codespaces/blob/main/fineTuningExample/ftHelloWorld.py)  

* [Fine-tuning HuggingFace Tutorial](https://huggingface.co/docs/transformers/training)

"When you use a pretrained model, you train it on a dataset specific to your task. This is known as fine-tuning, an incredibly powerful training technique. In this tutorial, you will fine-tune a pretrained model with a deep learning framework of your choice:"

Tried conda with and failed:

https://huggingface.co/docs/transformers/training

![Screen Shot 2022-09-20 at 8 15 55 PM](https://user-images.githubusercontent.com/58792/191387633-085a3ebb-b70d-47ee-b79a-7599604f64a5.png)

## How to do fast inference using API

* [Use hugging face inference api](https://gradio.app/using_hugging_face_integrations/#using-hugging-face-inference-api)
* [How to use inference](https://huggingface.co/docs/huggingface_hub/how-to-inference)

## Monitor GPU while Training

Use split terminal and do:

`nvidia-smi -l 1` in one
`htop` in another

## Verify GPU working

* [Reference PyTorch site](https://pytorch.org/get-started/locally/)
* `numba -s | grep cuda`
* run `python utils/verify_cuda_pytorch.py`
* run `nvidia-smi` should show a GPU

## Notes on OS X M1

```bash
conda create -n hf python=3.9
conda activate hf
conda env config vars set CONDA_SUBDIR=osx-arm64
#install nightly
pip install -U --pre torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/nightly/cpu
#install rust if not installed
curl — proto ‘=https’ — tlsv1.2 -sSf https://sh.rustup.rs | sh
#install via brew
brew install cmake
brew install pkg-config
```


## References

* [Monitoring GPU Training](https://unix.stackexchange.com/questions/38560/gpu-usage-monitoring-cuda)

