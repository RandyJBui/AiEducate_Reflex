"""Base state for the app."""

import reflex as rx
import mindsdb_sdk
from credentials import *
import pandas as pd
import time
server = mindsdb_sdk.connect(login=email, password=password)
proj = server.get_project("mindsdb")
model = proj.get_model("aieducate_v11")

class State(rx.State):
    """Base state for the app.

    The base state is used to store general vars used throughout the app.
    """
    boilerPlate: str
    iter: int=0
    age: str="age:"
    query: str = "ask here!"
    output: str
    outputList: list[str]
    buffer: str
    quizString: list[str]
    hist: list[tuple[str,str]]
    def log(self):
        request = model.predict({"text": f'{self.boilerPlate}'})
        pd.set_option('display.max_colwidth', None)
        self.buffer= request['response'][0]

    @rx.var
    def updates(self):
        return self.output
    def generalizationFilter(self,inp: list[str], out: list[str]=[]):

        pd.set_option('display.max_colwidth',None)
        for i in inp:
            out.append( model.predict( {"text": f'What is the main concept in the question: do not repeat the actual question and do not use examples '  + i })['response'][0])
    
        return out
    def generateQuiz(self):
        prompts = self.generalizationFilter(self.quizString)
        self.quizString.clear()
        for i in prompts:
            self.quizString.append(model.predict( {"text": f'Create a question with answer seperated by a \  on the topic of ' + i + "it should be answerable within 10 words" } )['response'][0])
        

    def generate(self):
        self.output = "" 
        if self.iter > 0:
            self.hist.append((self.outputList[self.iter -1], self.quizString[self.iter -1]))
        if  (self.iter == 2):
            self.iter =0
            self.generalizationFilter(self.quizString)
            self.generateQuiz()
        else:
            self.boilerPlate = "Explain like im " + self.age + "what " + self.query
        self.log()
        self.outputList.append(self.buffer)
        for i in self.buffer:
            self.output += i
            time.sleep(.08)
            yield
        self.quizString.append(self.query)
        self.iter += 1
    pass

