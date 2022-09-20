[![Python application test with Github Actions using devcontainers](https://github.com/nogibjj/hugging-face-cli-with-codespaces/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/hugging-face-cli-with-codespaces/actions/workflows/main.yml)


# hugging-face-cli-with-codespaces
Repo that allows me to build AI tools on top of Hugging Face


## How to do fast inference using API

* [Use hugging face inference api](https://gradio.app/using_hugging_face_integrations/#using-hugging-face-inference-api)
* [How to use inference](https://huggingface.co/docs/huggingface_hub/how-to-inference)

## Verify GPU working

* [Reference PyTorch site](https://pytorch.org/get-started/locally/)
* `numba -s | grep cuda`
* run `python utils/verify_cuda_pytorch.py`
* run `nvidia-smi` should show a GPU
