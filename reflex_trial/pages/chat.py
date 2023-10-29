import reflex as rx
from reflex_trial.state import State
from reflex_trial import style

#input(age, gradeLevel, question)

def chat() -> rx.Component:
    return rx.container(
        rx.box(
            rx.text(State.query),
            style=style.question_style,
            text_align="right"
        ),
        rx.box(
            rx.text(State.updates),
            style=style.answer_style,
            text_align="left",
        ),
    )
def action_bar() -> rx.Component:
    return rx.container(
            rx.box(
                rx.hstack(
                    rx.input(
                        placeholder="Age",
                        style=style.input_style, on_change=State.set_age
                    ),
                    rx.input(
                        placeholder="Question",
                        style=style.input_style, on_change=State.set_query
                    ),
                    rx.button(
                        "Ask!",
                        style=style.button_style, on_click=State.generate
                    ),
                ),
            ),
        )
    
