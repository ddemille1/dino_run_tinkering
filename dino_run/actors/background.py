
import pyray


class Background():

    def __init__(self, file_path, pos_x, pos_y):

        self._file_path = file_path
        self._pos_x = pos_x
        self._pos_y = pos_y

    def draw_background(self):
        _background = pyray.load_texture(self._file_path)
        pyray.draw_texture(_background, self._pos_x, self._pos_y, pyray.RAYWHITE)
