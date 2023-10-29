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
    output: str="LLM's Best response!"
    outputList: list[str]
    buffer: str
    quizString: list[str]
    hist: list[tuple[str,str]]
    quizList: list[tuple[str,str]]
    quizFlip: bool=False
    answer: str
    percent: str
    given: str
    score: int
    quizBuffer: str

    prompts: list[str]
    promptCount: int
    count: int
    gen: str
   
    
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
            out.append( model.predict( {"text": f'what is the topic being discussed in the question: '  + i  + 'your response should not repeat the actual question and should not use examples '})['response'][0])
        return out
    
    def generateQuiz(self):
        self.quizString.append(model.predict( {"text": f'Create a question with answer, ALWAYS seperated with a / on the topic of ' + self.prompts[self.count] + "it should be answerable within 10 words" } )['response'][0])
        self.given = ( self.quizString[self.count].rsplit( "/",2 ) )
    def quizClicked(self):
        if self.count < 3:
                self.generateQuiz()
                self.count +=1  
                self.quizBuffer=""
                self.gen = self.quizString[self.count].split('/')[0]

                pd.set_option('display.max_colwidth',None)
                #self.percent = model.predict( {"text" : f'Give me a percentage between the accuracy of these two answers: ' + {self.given} + ' and '  + {self.answer} })['response'][0]
                #self.quizList.append((self.gen,self.answer))

        else:
                self.quizFlip=False
    @rx.var
    def quizPrompt(self):
        return self.quizBuffer
    def generate(self):
        self.output = "" 
        if self.iter > 0:
            self.hist.append((self.outputList[self.iter-1], self.quizString[self.iter -1]))
        self.iter += 1  
        if  (self.iter == 4):
            self.quizFlip=True
            self.iter =0
            self.prompts = self.generalizationFilter(self.quizString)
            self.quizString.clear()
            self.generateQuiz()
            self.quizBuffer = self.quizString[0].split("/")[0]
            self.quizList.append((self.quizBuffer, self.answer))
        else:
            self.boilerPlate = "Explain like im " + self.age + "what " + self.query
            self.log()
            self.outputList.append(self.buffer)
            for i in self.buffer:
                self.output += i
                time.sleep(.08)
                yield
            self.quizString.append(self.query)
           

        pass

