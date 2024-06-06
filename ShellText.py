from textual.app import App, ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.screen import Screen
from textual.widgets import Static, TextArea, Placeholder

__version__ = '0.0.2'

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

class Menu(Static):
    DEFAULT_CSS = """
    Menu {
        width: 32;
        dock: left;
        background: red 30%;
        height: 100%;
    }
    """

class MainContent(VerticalScroll):
    DEFAULT_CSS = """
    MainContent {
        # background: grey;
        color: white;
        height: auto;
    }
    """
    def compose(self) -> ComposeResult:
        yield TextArea(id="body")

class AppScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header(id="header")
        yield Footer(id="footer")
        with Horizontal():
            yield Menu(id="menu")
            yield MainContent(id="main_content")

class LayoutApp(App):
    def on_ready(self) -> None:
        self.push_screen(AppScreen())

if __name__ == "__main__":
    app = LayoutApp()
    app.run()
