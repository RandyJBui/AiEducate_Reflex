import reflex as rx

def subtext() -> rx.component:
    return rx.flex (
        rx.box ( 
            rx.hstack (
            rx.text("Made by "),
            rx.avatar_group(
                rx.avatar(name="E L"),
                rx.avatar(name="R B"),
            ),
            rx.text("Powered by "),
            rx.center(
                rx.image(
                    src="/icon.svg",
                    height="4em",
                    padding="0.5em",
                ),
            ),
            rx.text(" and "),
            rx.center(
                rx.image(
                    src="/mindsdb.svg",
                    height="4em",
                    padding="0.5em",
                ),
            ),
        
        ),
    margin_top="1.5em",
    margin_left="1.5em",
    padding_left="2em",
    margin_bottom="1.5em",
    font_weight="normal",
    position="sticky",
    width="40vw",

        ),

)