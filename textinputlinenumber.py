from kivy.clock import Clock
from kivy.properties import ObjectProperty, NumericProperty, ListProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


class LineNumbers(TextInput):
    lines_flags = ListProperty([])

    def on_lines_flags(self, *args):
        self._update_line_counting()

    def _update_line_counting(self):
        amount_lines = 0
        text = '1'
        for flag in self.lines_flags:
            if flag == CustomTextInput.LINE_FLAG_NEWLINE:
                amount_lines += 1
                text += f'{amount_lines+1}\n'
            else:
                text += f'\n'
        self.text = text

    def on_scroll_y(self, *args):
        self._update_graphics()


class CustomTextInput(TextInput):
    amount_lines = NumericProperty(1)
    lines_flags = ListProperty([])

    LINE_FLAG_WORDWRAP = 0
    LINE_FLAG_NEWLINE = 1
    LINE_FLAG_WORDBREAK = 2

    # callback on internal _lines property # TODO: should I be using _lines??
    def on__lines(self, *args):
        amount_lines = 1
        self.lines_flags = self._lines_flags
        for flag in self.lines_flags:
            if flag == self.LINE_FLAG_NEWLINE:
                amount_lines += 1
        self.amount_lines = amount_lines

    def on_scroll_y(self, *args):
        self._update_graphics()


class TextInputLineNumber(BoxLayout):
    text_content = ObjectProperty(None)
    line_numbers = ObjectProperty(None)

    amount_lines = NumericProperty(0)
    lines_flags = ListProperty([])
    text = StringProperty('')
    scroll_y = NumericProperty(0)
