import os
import openai
import json

class Agent:
    def __init__(self, model = "gpt-4", system_prompt = "You are here to help me"):
        self._model = model
        self._system_prompt = system_prompt
        self._messages = []
        self.add_message("system", self._system_prompt)
        self._status = "new"

    def get_system_prompt(self):
        return self._system_prompt

    def set_status(self,status):
        self._status = status

    def get_status(self):
        return self._status

    def add_message(self, role, content):
        self._messages.append({"role": role, "content": content})

    def api_call(self):
        api_response = openai.ChatCompletion.create(
            model=self._model,
            messages=self._messages)
        return json.loads(api_response["choices"][0]["message"]["content"])