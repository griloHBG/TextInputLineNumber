from kivy.clock import Clock
from kivy.properties import ObjectProperty, NumericProperty, ListProperty, StringProperty, AliasProperty
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.codeinput import CodeInput
from kivy.uix.textinput import TextInput


class LineNumbers(CodeInput):
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


class CustomTextInput(CodeInput):
    amount_lines = NumericProperty(1)
    lines_flags = ListProperty([])
    cursor_line = NumericProperty(1)

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

    def go_to_line(self, line_number):
        print(self.cursor, 'começo')
        self.cursor = (0,0)
        self.cursor_line = 1
        flag_idx = 0
        while self.cursor_line < line_number-1:
            if self.lines_flags[flag_idx] == self.LINE_FLAG_NEWLINE:
                self.cursor_line+=1
            # print(self.cursor, flag_idx, "new line" if self.lines_flags[flag_idx] == self.LINE_FLAG_NEWLINE else "no new line")
            flag_idx+=1
        #TODO: sometimes we get 1 line before the intended line
        # print('linha', self.cursor_line, line_number)
        if not self.lines_flags[flag_idx] == self.LINE_FLAG_NEWLINE:
            flag_idx+=1
        self.cursor = (0, flag_idx)


class TextInputLineNumber(FocusBehavior, BoxLayout):
    text_content = ObjectProperty(None)
    line_numbers = ObjectProperty(None)

    amount_lines = NumericProperty(0)
    lines_flags = ListProperty([])
    text = StringProperty('')
    scroll_y = NumericProperty(0)

    selection = StringProperty('')

    cursor_line = NumericProperty(1)

    def update_graphics(self):
        self.line_numbers._update_graphics()
        self.text_content._update_graphics()

    def do_cursor_movement(self, action, control=False, alt=False):
        self.text_content.do_cursor_movement(action, control, alt)

    def cursor_index(self, cursor=None):
        return self.text_content.cursor_index(cursor)

    def go_to_line(self, line_number):
        self.text_content.go_to_line(line_number)

    def get_current_line(self):
        return self.text_content.cursor_line

    def select_text(self, start, end):
        self.text_content.select_text(start, end)

    def get_cursor_from_xy(self, x, y):
        return self.text_content.get_cursor_from_xy(x, y)

    def get_cursor_from_index(self, text_index):
        return self.text_content.get_cursor_from_index(text_index)