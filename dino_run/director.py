#desert background from: https://opengameart.org/content/cethiels-desert-background-redux

import pyray


class Director():
    def __init__(self, keyboard_service, video_service, cactus, background):
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._cactus = cactus
        self._background = background

    def start_game(self):
        self._video_service.open_window()   
        while self._video_service.is_window_open(): 
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
        self._video_service.close_window()

        
        

        

        while not pyray.window_should_close():
            pyray.begin_drawing()
            pyray.clear_background(pyray.RAYWHITE)

    

    def _get_inputs(self):
        pass

    def _do_updates(self):
        pass

    def _do_outputs(self):
        self._video_service.clear_buffer()
        self._background.draw_background()
        self._cactus.draw_cactus()

        self._video_service.flush_buffer()

