[![Python application test with Github Actions using devcontainers](https://github.com/nogibjj/hugging-face-cli-with-codespaces/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/hugging-face-cli-with-codespaces/actions/workflows/main.yml)


# hugging-face-cli-with-codespaces
Repo that allows me to build AI tools on top of Hugging Face

## Try out fine-tuning

* [Fine-tuning HuggingFace Tutorial](https://huggingface.co/docs/transformers/training)

"When you use a pretrained model, you train it on a dataset specific to your task. This is known as fine-tuning, an incredibly powerful training technique. In this tutorial, you will fine-tune a pretrained model with a deep learning framework of your choice:"

Tried conda with and failed:

https://huggingface.co/docs/transformers/training

```
(fineTune) @noahgift ➜ /workspaces/hugging-face-cli-with-codespaces/fineTuningExample (main ✗) $ python script.py 
Traceback (most recent call last):
  File "/opt/conda/envs/fineTune/lib/python3.9/site-packages/transformers/utils/import_utils.py", line 1031, in _get_module
    return importlib.import_module("." + module_name, self.__name__)
  File "/opt/conda/envs/fineTune/lib/python3.9/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 972, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed
  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 850, in exec_module
  File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed
  File "/opt/conda/envs/fineTune/lib/python3.9/site-packages/transformers/models/__init__.py", line 19, in <module>
    from . import (
  File "/opt/conda/envs/fineTune/lib/python3.9/site-packages/transformers/models/mt5/__init__.py", line 40, in <module>
    from ..t5.tokenization_t5_fast import T5TokenizerFast
  File "/opt/conda/envs/fineTune/lib/python3.9/site-packages/transformers/models/t5/tokenization_t5_fast.py", line 23, in <module>
    from ...tokenization_utils_fast import PreTrainedTokenizerFast
  File "/opt/conda/envs/fineTune/lib/python3.9/site-packages/transformers/tokenization_utils_fast.py", line 25, in <module>
    import tokenizers.pre_tokenizers as pre_tokenizers_fast
  File "/opt/conda/envs/fineTune/lib/python3.9/site-packages/tokenizers/__init__.py", line 79, in <module>
    from .tokenizers import (
ImportError: libssl.so.10: cannot open shared object file: No such file or directory

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/workspaces/hugging-face-cli-with-codespaces/fineTuningExample/script.py", line 1, in <module>
    from transformers import AutoTokenizer
  File "<frozen importlib._bootstrap>", line 1055, in _handle_fromlist
  File "/opt/conda/envs/fineTune/lib/python3.9/site-packages/transformers/utils/import_utils.py", line 1021, in __getattr__
    module = self._get_module(self._class_to_module[name])
  File "/opt/conda/envs/fineTune/lib/python3.9/site-packages/transformers/utils/import_utils.py", line 1033, in _get_module
    raise RuntimeError(
RuntimeError: Failed to import transformers.models.auto because of the following error (look up to see its traceback):
libssl.so.10: cannot open shared object file: No such file or directory
```


## How to do fast inference using API

* [Use hugging face inference api](https://gradio.app/using_hugging_face_integrations/#using-hugging-face-inference-api)
* [How to use inference](https://huggingface.co/docs/huggingface_hub/how-to-inference)

## Verify GPU working

* [Reference PyTorch site](https://pytorch.org/get-started/locally/)
* `numba -s | grep cuda`
* run `python utils/verify_cuda_pytorch.py`
* run `nvidia-smi` should show a GPU
