import yaml

from openai import OpenAI

Message = dict[str, str]

class ModelInterface:
    def __init__(self):
        """Model Interface class for communicating with the model"""
        with open("config.yaml", "r") as f:
            config = yaml.safe_load(f)

            self.model = config.get("MODEL", "hugging-quants/llama-3.2-3b-instruct")

            LM_STUDIO_URL = config.get("LM_STUDIO_URL", "http://127.0.0.1:1234/v1")
            LM_STUDIO_API_KEY = config.get("LM_STUDIO_API_KEY", "lm-studio")
            self.client = OpenAI(base_url=LM_STUDIO_URL, api_key=LM_STUDIO_API_KEY)

    def chatcompletion(
            self,
            messages: list[Message],
            temperature: float = 0.7,
            stream: bool = False
    ):
        """Use a language model to generate text"""
        resp = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=temperature
        )
        return resp.choices[0].message.content