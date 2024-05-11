import functools
import threading
import httpx
import ida_kernwin
from gepetto.models.base import LanguageModel
import gepetto.config

_ = gepetto.config.translate.gettext

class GPT(LanguageModel):
    def __init__(self, model):
        self.model = model
        self.base_url = "http://localhost:1234/v1/chat/completions"

    def __str__(self):
        return self.model

    def query_model(self, query, cb, additional_model_options=None):
        if additional_model_options is None:
            additional_model_options = {}
        try:
            response = httpx.post(
                self.base_url,
                json={
                    "model": self.model,
                    "messages": [{"role": "user", "content": query}],
                    **additional_model_options
                },
                timeout=20
            )
            response.raise_for_status()
            content = response.json()
            if 'choices' in content and content['choices']:
                message_content = content['choices'][0]['message']['content']
                #print("Content :",message_content)
                ida_kernwin.execute_sync(functools.partial(cb, response=message_content),
                                         ida_kernwin.MFF_WRITE)
            else:
                print(_("Unexpected response format: {content}").format(content=content))
        except httpx.RequestError as e:
            print(_("Error while sending request to local LLM model: {error}").format(error=str(e)))
        except Exception as e:
            print(_("General exception encountered while running the query: {type} - {error}").format(
                type=type(e).__name__, error=str(e)))

    def query_model_async(self, query, cb, additional_model_options=None):
        if additional_model_options is None:
            additional_model_options = {}
        print(_("Request to {model} sent...").format(model=str(gepetto.config.model)))
        t = threading.Thread(target=self.query_model, args=[query, cb, additional_model_options])
        t.start()
