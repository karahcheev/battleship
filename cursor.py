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
        if key == 'right' and self.x < 9:
            self.x += 1
        elif key == 'left' and self.x > 0:
            self.x -= 1
        elif key == 'up' and self.y > 0:
            self.y -= 1
        elif key == 'down' and self.y < 9:
            self.y += 1
        else:
            pass
        cursor = [self.x, self.y]
        return cursor
