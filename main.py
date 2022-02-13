from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
import math


Config.set('kivy', 'keyboard_mode', 'systematised')


class CalculatorGridLayout(GridLayout):
    def round_button(self):
        num = round((float(self.display.text)), 2)
        self.display.text = str(num)

    def sqrt_button(self):
        num = round(math.sqrt(float(self.display.text)), 2)
        self.display.text = str(num)

    def pi_button(self):
        num = round(float(math.pi), 4)
        self.display.text += str(num)

    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = 'Error'


class CalculatorApp(App):
    def build(self):
        return CalculatorGridLayout()


if __name__ == '__main__':
    CalculatorApp().run()
