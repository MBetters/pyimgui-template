# -*- coding: utf-8 -*-
from __future__ import absolute_import
import sys
import pyglet
# from pyglet import gl # NOTE: This doesn't work
import OpenGL.GL as gl # NOTE: This works
from .testwindow import show_test_window
import imgui
# Note that we could explicitly choose to use PygletFixedPipelineRenderer
# or PygletProgrammablePipelineRenderer, but create_renderer handles the
# version checking for us.
from imgui.integrations.pyglet import create_renderer

# Set the GUI's local variables...
gui_fullscreen = True # TODO: Set this to True or False as desired
window_width = None
window_height = None
if gui_fullscreen:
    if sys.platform == 'win32':
        # Since our GUI is fullscreen, the window width and height can use the screen size,
        # which is gotten from the Win32 "System Metrics" API.
        from win32api import GetSystemMetrics
        window_width = GetSystemMetrics(0)
        window_height = GetSystemMetrics(1)
    else:
        raise Exception("This app only runs on Win32 platforms!")
else:
    raise Exception("This GUI is only designed for running in full-screen! Set gui_fullscreen back to True!")
assert window_width is not None
assert window_height is not None
quit_the_app = False

def on_key_press(symbol, modifiers):
    global quit_the_app
    if symbol == pyglet.window.key.ESCAPE:
        print("Goodbye!!!")
        quit_the_app = True
    # Example of using a modifier key (Ctrl, Shift, etc.)
    # if (modifiers & pyglet.window.key.MOD_CTRL) and symbol == pyglet.window.key.Q:
    #     ...

def on_key_release(symbol, modifiers):
    pass

# This gets called every single frame!
def update(dt):
    # Start rendering a new frame
    imgui.new_frame()
    
    ### MENU BAR BEGIN ###
    if imgui.begin_main_menu_bar():
        if imgui.begin_menu("File", True):
            clicked_quit, selected_quit = imgui.menu_item(
                "Quit", "Esc", False, True
            )
            if clicked_quit:
                exit(1)
            imgui.end_menu()
        # End rendering the menu bar
        imgui.end_main_menu_bar()
    if quit_the_app:
        exit(1)
    ### MENU BAR END ###
    
    # Show a basic test window, if you want
    # show_test_window()

    # TODO: Do any imgui stuff you want here. Here's a simple example...
    # imgui.begin("My Cool Sub-Window", True) # start rendering a sub-window
    # imgui.set_window_size(window_width / 2, window_height) # take up half the screen
    # imgui.text("Here's some awesome text!") # render some text
    # if imgui.button("Click Me!"): # buttons are rendered and checked for clicks in one line!
    #     imgui.text("Button clicked!")
    # imgui.end() # end the sub-window
    
    # Clear the OpenGL buffer for the background color.
    gl.glClearColor(1, 1, 1, 1)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)

def main():
    # TODO: Do any pre-window setup here.
    # ...
    # Make a Pyglet window for PyImGUI to use
    window = pyglet.window.Window(fullscreen=gui_fullscreen)
    # Register functions to handle key presses and releases
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    # Start with a clear background
    gl.glClearColor(1, 1, 1, 1)
    # Create a GUI context and renderer
    imgui.create_context()
    renderer = create_renderer(window)
    # This is a "sub-function" of "main()", used for drawing every frame.
    def draw(dt):
        update(dt) # call the update
        window.clear() # clear the window
        # Render the frame
        imgui.render()
        renderer.render(imgui.get_draw_data())
    # Schedule the "draw" function to get called forever every 1 / 120.0 seconds.
    frame_interval = 1 / 120.0
    pyglet.clock.schedule_interval(draw, frame_interval)
    pyglet.app.run()
    renderer.shutdown()

if __name__ == "__main__":
    main()
