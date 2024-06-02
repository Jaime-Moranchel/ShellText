from textual.app import App, ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.screen import Screen
from textual.widgets import Placeholder, Static


class Header(Placeholder):
    DEFAULT_CSS = """
    Header {
        height: 1;
        dock: top;
        background: blue;
    }
    """


class Footer(Placeholder):
    DEFAULT_CSS = """
    Footer {
        height: 1;
        dock: bottom;
        background: blue;
    }
    """

class Menu(Placeholder):
    DEFAULT_CSS = """
    Menu {
        width: 32;
        dock: left;
        background: green;
    }
    """

TEXT = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""

class MainContent(VerticalScroll):
    DEFAULT_CSS = """
    MainContent {
        background: white;
        color: black;
    }
    """

class TweetScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header(id="header")
        yield Footer(id="footer")
        with Horizontal():
            yield Menu(id="menu")
            yield MainContent(Static(TEXT * 10, id="body"), id="main_content")

class LayoutApp(App):
    def on_ready(self) -> None:
        self.push_screen(TweetScreen())

if __name__ == "__main__":
    app = LayoutApp()
    app.run()
