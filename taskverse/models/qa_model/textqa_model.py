from typing import Callable, Union

import torch

from .base_qa_model import QAModel, QAModelInstance

textqa_models = {

	"gpt4v"            : ("GPT4V", "<openai-api>"),
	"gpt4o"            : ("GPT4O", "<openai-api>"),
	"qwen-vl-plus"     : ("QwenVLPlus", ['<qwen-api>', '<aliyun-access-id>', '<aliyun-access-secret>']),
	"qwen-vl-max"      : ("QwenVLMax", ['<qwen-api>', '<aliyun-access-id>', '<aliyun-access-secret>']),
	"gemini-vision-pro": ("GeminiVisionPro", "<google-api>"),
}


def set_textqa_model_key(model_name, key):
	textqa_models[model_name] = (textqa_models[model_name][0], key)


def list_textqa_models():
	return list(textqa_models.keys())


class TextQAModel(QAModel):
	def __init__(
			self,
			model_name: str,
			prompt_name: str,
			prompt_func: Callable,
			model: QAModelInstance = None,
			torch_device: Union[int, str] = -1,
			precision=torch.bfloat16,
			choice_format='letter',
			enable_choice_search: bool = False,
			cache_path: str = None,

	):
		super().__init__(model_name, prompt_name, prompt_func, choice_format, enable_choice_search, cache_path)

		if isinstance(torch_device, str):
			torch_device = torch.device(torch_device)
		else:
			if torch_device == -1:
				torch_device = torch.device("cuda") if torch.cuda.is_available() else "cpu"
			else:
				torch_device = torch.device(f"cuda:{torch_device}")

		if model is None:
			print(f"Loading {model_name}...")
			class_name, ckpt = textqa_models[model_name]
			self.model_precision = precision
			self.model = eval(class_name)(ckpt, torch_device, self.model_precision)
			print(f"Finish loading {model_name}")
		else:
			print(f"Using provided model...")
			self.model = model

	def _data_to_str(self, data):
		assert isinstance(data, str)
		return data


class MathQAModel(QAModel):
	@torch.no_grad()
	def qa(self, data, question, answer=None):
		prompt = self.prompt_func(question)
		free_form_answer = self._qa(data, prompt)

		result = {
			"free_form_answer": free_form_answer,
		}
		if answer is not None:
			# TODO: how to check answer for math? search "exact match"
			# check this out https://arxiv.org/abs/2304.15004
			result["?"] = None
		return result
