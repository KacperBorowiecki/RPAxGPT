from .Agent import Agent


class RPADeveloper(Agent):
    def __init__(self, model = "gpt-4", system_prompt = "You are RPA Developer"):
        super().__init__(system_prompt=system_prompt)