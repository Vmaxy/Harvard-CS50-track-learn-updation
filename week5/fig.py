from pyfiglet import Figlet
from random import choice
import sys

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    font = choice(fonts)
elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fonts:
    font = sys.argv[2]
else:
    sys.exit("Invalid usage")

text = input("Input: ")
figlet.setFont(font=font)
print(figlet.renderText(text))


