"""Welcome to Reflex!."""

from reflex_trial import style, styles
from reflex_trial.state import State
# Import all the pages.
import os
from reflex_trial.pages import chat, subtext

from reflex_trial.pages.chat import action_bar
from .pages import *
import reflex as rx
from credentials import *
# Create the app and compile it.

def  quizTime()->rx.Component:
    return rx.hstack( rx.input(placeholder="Quiz Time!", value=State.answer, on_change=State.set_answer), rx.button("Go!",style=style.button_style, on_click=State.quizClicked()))

def dispQuiz()->rx.Component:
      return rx.container(
        rx.box(
            rx.text(State.gen),
            style=style.answer_style,
            text_align="left",
        ),

        rx.box(
            rx.text(State.answer),
            style=style.question_style,
            text_align="right"
        ),
    
    )

def index() ->rx.Component:
    return rx.container(subtext.subtext(), rx.cond(State.quizFlip, dispQuiz(), chat.chat()), rx.cond(State.quizFlip, quizTime(), chat.action_bar()), )

app = rx.App(style=style.message_style)
app.add_page(index)
app.compile()
