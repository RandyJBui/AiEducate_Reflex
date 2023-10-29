from reflex_trial.templates import template
import reflex as rx
from reflex_trial import styles
from reflex_trial.state import State
from credentials import *

def leftright(a,q) ->rx.Component:
     return rx.box(
        rx.box(
            rx.text(q, style=styles.question_style),
            text_align="right",
        ),
        rx.box(
            rx.text(a, style=styles.answer_style),
            text_align="left",
        ),
        margin_y="1em",
    )
@template(route="/", title="Practice AI")
def main() -> rx.Component: 

    return rx.hstack(rx.container(
        rx.vstack( 
             rx.container(
                rx.vstack( 
                        rx.foreach(State.hist, lambda x: leftright(x[0],x[1])), 
                        rx.box(
                                rx.box(rx.text(State.query, style=styles.question_style), text_align="right",),
                                rx.box(rx.text(State.updates, style=styles.answer_style) ) ,text_align="left",),  
                rx.hstack( 
                    rx.vstack(
                        rx.input(placeholder="Age", value=State.age, on_change=State.set_age),
                        rx.input(placeholder="Prompt", value=State.query, on_change=State.set_query) ), 
                rx.button("Go",color_scheme="green", on_click=State.generate()) ), style=styles.message_style,  )
    ) ) ),
      rx.container(
        rx.vstack( 
             rx.container(
                rx.vstack( 
                        rx.foreach(State.hist, lambda x: leftright(x[0],x[1])), 
                        rx.box(
                                rx.box(rx.text(State.query, style=styles.question_style), text_align="right",),
                                rx.box(rx.text(State.updates, style=styles.answer_style) ) ,text_align="left",),  
                rx.hstack( 
                    rx.vstack(
                        rx.input(placeholder="Age", value=State.age, on_change=State.set_age),
                        rx.input(placeholder="Prompt", value=State.query, on_change=State.set_query) ), 
                rx.button("Go",color_scheme="green", on_click=State.generate()) ), style=styles.message_style,  )
    ) ) ) )