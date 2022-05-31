import getch as gh

class Cursor:
    def __init__(self):
        self.y = 0
        self.x = 0

    @staticmethod
    def _get_key_from():
        try:
            first_char = gh.getch()
            if first_char == '\x1b':
                return {'[A': 'up', '[B': 'down', '[C': 'right', '[D': 'left'}[gh.getch() + gh.getch()]
            else:
                return
        except OverflowError:
            return None

    def update_coordinates(self):
        key = self._get_key_from()
        if key == 'right':
            self.x += 1
        elif key == 'left':
            self.x -= 1
        elif key == 'up':
            self.y -= 1
        elif key == 'down':
            self.y += 1
        else:
            pass
        cursor = [self.x, self.y]
        return cursor
