from demoqa_test.model.components.left_panel import LeftPanel
from demoqa_test.model.components.output_form import OutputForm
from demoqa_test.model.pages.tex_box_page import TextBoxPage


class Application:
    def __init__(self):
        self.simple_registration = TextBoxPage()
        self.output_form = OutputForm()
        self.left_panel = LeftPanel()


app = Application()
