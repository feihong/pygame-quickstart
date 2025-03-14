"""
Utility module for pygame
"""
import sys
import importlib
from pathlib import Path
import threading
import queue
import inspect
import pygame
import watchfiles


screen = None


def set_caption(caption):
    pygame.display.set_caption(caption)

def get_screen(w, h):
    global screen
    if screen is None:
        screen = pygame.display.set_mode((w, h))
    return screen

def run(draw, on_event=None):
    pygame.init()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                raise SystemExit
            else:
                if on_event:
                    on_event(event)

        draw()
        pygame.display.flip()

def run_with_reload(module, reload_queue):
    pygame.init()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                raise SystemExit
            else:
                if hasattr(module, 'on_event'):
                    module.on_event(event)

        module.draw()

        if not reload_queue.empty():
            reload_queue.get()
            importlib.reload(module)

        pygame.display.flip()

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
