import curses
from settings import *

def main(stdscr):
    print(stdscr)
    win = Window(stdscr)
    win.run()

class Window:
    def __init__(self, stdscr):
        curses.curs_set(0)
        stdscr.clear()
        self.stdscr = stdscr
        y, x = (curses.LINES - HEIGHT) // 2, (curses.COLS - WIDTH) // 2
        self.window = stdscr.subwin(HEIGHT, WIDTH, y, x)
        self.running = True
        
    def run(self):
        while self.running:
            self.stdscr.refresh()
            self.window.refresh()
        

# Run the curses application
# win = Window()
curses.wrapper(main)
