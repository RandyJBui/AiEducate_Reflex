"""Base state for the app."""

import reflex as rx
from credentials import *
import mindsdb_sdk
from credentials import *

server = mindsdb_sdk.connect(login=email, password=password)
proj = server.get_project("test")
model = proj.get_model("gpt_model_1")

class State(rx.State):
    """Base state for the app.

    The base state is used to store general vars used throughout the app.
    """
    boilerPlate: str
    iter: int=0
    age: str="0"
    query: str
    output: str
    def log(self):
        print('hi')
        request = model.predict({"text": f'{self.boilerPlate}'})
        self.output = request
        print(self.output)
     
    def generate(self):
        self.boilerPlate = "Explain like im " + self.age + "what " + self.query
        self.log()
    pass

