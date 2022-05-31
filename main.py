from battlefield import Battlefield
import os


b = Battlefield()

key = ''
while key != 'q':

    os.system('clear')
    b.print_battlefield()
    b.cursor.update_coordinates()

