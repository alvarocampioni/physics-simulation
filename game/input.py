import pygame
from data.config import (
    START_X, START_Y, INPUT_BOX_VELOCITY, INPUT_BOX_ANGLE
)

from simulation.core import add_projectile
from simulation.logic import switch_theme

from engine.physics import launch_projectile

def handle_mouse_input(event, state):
    mouse_x, mouse_y = event.pos
    if INPUT_BOX_VELOCITY.collidepoint((mouse_x, mouse_y)):
        state.active_box = INPUT_BOX_VELOCITY
    elif INPUT_BOX_ANGLE.collidepoint((mouse_x, mouse_y)):
        state.active_box = INPUT_BOX_ANGLE
    else:
        state.active_box = None
    if state.selecting_target:
        state.target_x, state.target_y = mouse_x, mouse_y
        state.selecting_target = False

def handle_input_box(event, text):
    if event.key == pygame.K_BACKSPACE:
        return text[:-1]
    elif event.unicode.isnumeric() or event.unicode in {'.', '-'}:
        return text + event.unicode
    return text

def handle_keyboard_input(event, state):
    key = event.key

    if key == pygame.K_RETURN:
        state.active_box = None

    elif state.active_box == INPUT_BOX_ANGLE:
        state.text_angle = handle_input_box(event, state.text_angle)
    elif state.active_box == INPUT_BOX_VELOCITY:
        state.text_velocity = handle_input_box(event, state.text_velocity)

    elif key in {pygame.K_SPACE, pygame.K_LSHIFT, pygame.K_ESCAPE, pygame.K_t, pygame.K_n}:
        handle_special_keys(event, state)
    elif key in {pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT}:
        handle_arrow_keys(event, state)

def handle_special_keys(event, state):
    key = event.key
    if key == pygame.K_SPACE:
        if state.static_projectiles:
            if launch_projectile(state.text_velocity, state.text_angle, state.static_projectiles, state.space, state.moving_projectiles):
                state.running_simulation = True
    elif key == pygame.K_LSHIFT and state.static_projectiles:
        state.intercept = not state.intercept
    elif key == pygame.K_ESCAPE:
        state.reset()
    elif key == pygame.K_t:
        state.selecting_target = not state.selecting_target
    elif key == pygame.K_n:
        add_projectile(state.static_projectiles, START_X, START_Y, state.space)

def handle_arrow_keys(event, state):
    key = event.key
    if key in {pygame.K_UP, pygame.K_DOWN}:
        try:
            num_ang = float(state.text_angle)
        except ValueError:
            num_ang = 0.0
        num_ang += 5 if key == pygame.K_UP else -5
        num_ang = max(0, min(90, num_ang))
        state.text_angle = str(num_ang)
    elif key in {pygame.K_LEFT, pygame.K_RIGHT} and not state.running_simulation:
        direction = 1 if key == pygame.K_RIGHT else -1
        state.simulation_theme, gravity = switch_theme(direction, state.simulation_theme.get_current())
        state.space.gravity = (0, gravity)
        state.floor.update(state.simulation_theme.name)
        state.background.update(state.simulation_theme.name)

def handle_events(events, state):
    for event in events:
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.MOUSEBUTTONDOWN:
            handle_mouse_input(event, state)
        elif event.type == pygame.KEYDOWN:
            handle_keyboard_input(event, state)
    return True