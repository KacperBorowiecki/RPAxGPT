from .Agent import Agent


class BusinessAnalyst(Agent):
    def __init__(self, model = "gpt-4", system_prompt = "You are Business analyst"):
        super().__init__(system_prompt=system_prompt)
        self._task_for_developer = ""

    def get_user_answers(self, questions):
        answers = {}
        for key in questions:
            answers[str(key)] = input(f"{questions[key]}\n")
        self.add_message(role="user", content=f"'{answers}'")

    def set_task_for_developer(self, task):
        self._task_for_developer = task

    def get_task_for_developer(self):
        return self._task_for_developer

    def analyze(self):
        while self.get_status() not in "completed":
            response = self.api_call()
            self.set_status(response["status"])
            if self.get_status() in "asking":
                self.add_message(role="assistant", content=f"'{response}'")
                self.get_user_answers(response["questions"])
            if self.get_status() in "completed":
                self.set_task_for_developer(response)
