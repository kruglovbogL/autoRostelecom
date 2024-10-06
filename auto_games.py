import main
import window


class Start():
    def Next(self):
        while True:
            button = main.Button()
            button.Cycle()
            screen = window.Screentake()
            screen.screen()


if __name__ == '__main__':
    start = Start()
    start.Next()