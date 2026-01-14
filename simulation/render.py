import pygame, math

from engine.physics import calculate_trajectory_preview

from ui.interface import draw_stats

from data.config import (
    PIXELS_PER_METER, DARK_GRAY, BLACK, FLOOR_HEIGHT, FLOOR_Y, START_Y, RED,
    WALL_HEIGHT, WALL_WIDTH, WALL_X, WALL_Y, SCREEN_WIDTH, START_X
)

def draw_arrow(surface, color, start, angle_rad, length=60, arrow_size=10, arrow_angle=30, width=3):
    end_x = start[0] + length * math.cos(angle_rad)
    end_y = start[1] - length * math.sin(angle_rad)  
    end = (end_x, end_y)

    # line
    pygame.draw.line(surface, color, start, end, width)

    left_angle = angle_rad + math.radians(arrow_angle)
    right_angle = angle_rad - math.radians(arrow_angle)

    # arrow
    left_x = end_x - arrow_size * math.cos(left_angle)
    left_y = end_y + arrow_size * math.sin(left_angle)

    right_x = end_x - arrow_size * math.cos(right_angle)
    right_y = end_y + arrow_size * math.sin(right_angle)

    pygame.draw.line(surface, color, end, (left_x, left_y), width)
    pygame.draw.line(surface, color, end, (right_x, right_y), width)

def draw_moving_projectiles(surface, moving_projectiles, border):
    for projectile in moving_projectiles:
        projectile.draw_trajectory(surface)
        projectile.draw_projectile(surface, border)

def draw_static_projectiles(screen, static_projectiles, border):
    for projectile in static_projectiles:
        projectile.draw_projectile(screen, border)

def draw_preview(screen, static_projectiles, text_angle, text_velocity, start_x, start_y, gravity):
    try:
        if len(static_projectiles) > 0: 
            launch_angle_rad = math.radians(float(text_angle))
            preview_velocity = float(text_velocity) * PIXELS_PER_METER
            preview_angle = math.radians(float(text_angle))
            preview_points = calculate_trajectory_preview((start_x + 12, start_y - 12), preview_velocity, preview_angle, gravity)

            for point in preview_points:
                pygame.draw.circle(screen, DARK_GRAY, point, 2)
            draw_arrow(screen, BLACK, (int(start_x), int(start_y)), launch_angle_rad)
    except ValueError:
        pass

def draw_floor(surface, color):
    pygame.draw.rect(surface, color, (0, FLOOR_Y, SCREEN_WIDTH, FLOOR_HEIGHT))

def draw_wall(surface, color):
    pygame.draw.rect(surface, color, (WALL_X, WALL_Y, WALL_WIDTH, WALL_HEIGHT))

def draw_screen(screen, state, FONT, INPUT_FONT):
    state.background.draw(screen)
    state.scenario.draw(screen)
    draw_moving_projectiles(screen, state.moving_projectiles, state.simulation_theme.text_color)
    draw_static_projectiles(screen, state.static_projectiles, state.simulation_theme.text_color)

    state.structure_sprites.draw(screen)
    state.moving_sprites.draw(screen)

    draw_stats(
        screen,
        state.simulation_theme,
        state.text_velocity,
        state.text_angle,
        state.time_elapsed,
        FONT,
        INPUT_FONT,
        state.color_angle,
        state.color_velocity,
        state.required_velocity,
    )

    draw_preview(
        screen,
        state.static_projectiles,
        state.text_angle,
        state.text_velocity,
        START_X,
        START_Y,
        state.simulation_theme.gravity * PIXELS_PER_METER,
    )

    if state.target_y != 0.0 and state.target_x != 0.0:
        pygame.draw.circle(screen, RED, (state.target_x, state.target_y), 6)
