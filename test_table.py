from frolic import ConsolePrinter
from levels.table import TableLevel

printer = ConsolePrinter()
printer.clear_screen()
screen = printer.get_empty_screen()

t = TableLevel()
t.draw(screen)

printer.draw_screen(screen)
