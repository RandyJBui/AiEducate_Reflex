from reflex_trial.templates import template
import reflex as rx
from reflex_trial.state import State
from credentials import *



@template(route="/main", title="Practice AI")

    


def main() -> rx.Component: 
    return rx.container(
         rx.hstack( 
             rx.vstack(
                rx.input(placeholder="Age", value=State.age, on_change=State.set_age),
                rx.input(placeholder="Prompt", value=State.query, on_change=State.set_query) ), 
        rx.button("Go",color_scheme="green", on_click=State.generate()) )
    )