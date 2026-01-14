import pygame, time
from game.game_state import GameState
from game.input import handle_events

from data.config import (
    FPS, SCREEN_HEIGHT, SCREEN_WIDTH, get_font
)

from simulation.render import draw_screen

from simulation.logic import update_simulation

def calculate_delta_time(state):
    delta_time = min(time.time() - state.last_time, 1.0 / FPS)  
    state.last_time = time.time()
    return delta_time

def run_game():
    pygame.init()
    pygame.display.set_caption("Physics Project")
    
    FONT, INPUT_FONT = get_font()

    running = True
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    state = GameState()

    while running:
        delta_time = calculate_delta_time(state)
        running = handle_events(pygame.event.get(), state)
        update_simulation(state, delta_time)
        draw_screen(screen, state, FONT, INPUT_FONT)
        pygame.display.flip()
    
    pygame.quit()