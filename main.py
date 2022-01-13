from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivy import utils
from kivy.core.window import Window
from kivymd.toast import toast

if utils.platform != 'ios':
    Window.size = (320, 640)


class MainApp(MDApp):
    user_input = StringProperty('')
    answer = StringProperty('')
    logic = StringProperty('')
    temporary = StringProperty('')
    operators = StringProperty('')

    def first(self, adds):
        self.logic = adds
        self.temporary = self.user_input
        self.answer = self.user_input
        self.user_input = ''

    def second(self):
        if self.logic == 'add':
            self.answer = str(int(self.temporary) + int(self.user_input))

        elif self.logic == 'minus':
            self.answer = str(int(self.temporary) - int(self.user_input))

        elif self.logic == 'multi':
            self.answer = str(int(self.temporary) * int(self.user_input))

        elif self.logic == 'div':
            self.answer = str(int(self.temporary) / int(self.user_input))

        elif self.logic == '.':
            toast('Oops!! still in development........')

        elif self.logic == 'exponent':
            self.answer = str(int(self.temporary) ** int(self.user_input))


        else:
            toast('Please enter an operation')

    def aquilline(self):
        if self.theme_cls.theme_style == "Dark":
            self.theme_cls.theme_style = 'Light'
        else:
            self.theme_cls.theme_style = 'Dark'

    def clear(self):
        self.temporary = ''
        self.user_input = ''
        self.answer = ''


MainApp().run()
