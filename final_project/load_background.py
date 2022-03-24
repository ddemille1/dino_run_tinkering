#desert background from: https://opengameart.org/content/cethiels-desert-background-redux

import pyray

def main():
    SCREEN_WIDTH = 818
    SCREEN_HEIGHT = 640

    pyray.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, 'DINO RUN')
    background = pyray.load_texture('pictures\cethiel-desert-edit.png')

    pyray.set_target_fps(60)

    while not pyray.window_should_close():
        pyray.begin_drawing()
        pyray.clear_background(pyray.RAYWHITE)
        
        
        pyray.draw_texture(background, 0, 0, pyray.RAYWHITE)
        pyray.end_drawing()
    pyray.close_window()

if __name__ == "__main__":
    main()
