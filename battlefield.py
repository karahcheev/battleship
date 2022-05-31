from importlib.util import set_loader
from cursor import Cursor

class Battlefield:
    def __init__(self):
        self.battlefield = [['.'] * 10 for y in range(10)]
        self.length_field = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.X = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К']
        self.cursor = Cursor()

    def print_battlefield(self):
        print('  ',*self.X, sep=' ')
        for y in range(10):
            print('{0:2}'.format(y+1), end=' ')
            for x in range(10):
                if self.cursor.x == x and self.cursor.y == y:
                    print("X", end=' ')
                else:
                    print(self.battlefield[x][y], end=' ')
                if x == 9:
                    print('')





