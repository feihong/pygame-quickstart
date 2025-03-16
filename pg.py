"""
Utility module for pygame
"""
import sys
import importlib
from pathlib import Path
import json
import threading
import queue
import tempfile
import pygame
import pygame._sdl2
import watchfiles


screen = None
window = None
position_file = Path(tempfile.gettempdir()) / 'pg_position'


def set_caption(caption):
    pygame.display.set_caption(caption)

def get_screen(w, h):
    global screen
    if screen is None:
        screen = pygame.display.set_mode((w, h))
    return screen

def run(draw, on_event=None):
    init()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                quit()
            else:
                if on_event:
                    on_event(event)

        draw()
        pygame.display.flip()

def run_with_reload(module, reload_queue):
    init()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                quit()
            else:
                if hasattr(module, 'on_event'):
                    module.on_event(event)

        module.draw()

        if not reload_queue.empty():
            reload_queue.get()
            importlib.reload(module)

        pygame.display.flip()

def init():
    global window
    pygame.init()
    window = pygame._sdl2.video.Window.from_display_module()
    if position_file.exists():
        window.position = tuple(json.loads(position_file.read_text()))

def quit():
    position_file.write_text(json.dumps(window.position))
    pygame.quit()
    raise SystemExit

def watch_file(py_file, reload_queue):
    for _changes in watchfiles.watch(py_file):
        reload_queue.put('reload')

if __name__ == '__main__':
    py_file = Path(sys.argv[1])
    module = importlib.import_module(py_file.stem)

    reload_queue = queue.Queue(maxsize=1)

    watch_thread = threading.Thread(target=watch_file, args=(py_file, reload_queue))
    watch_thread.daemon = True
    watch_thread.start()

    run_with_reload(module, reload_queue)
