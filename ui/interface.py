import pygame

from data.config import (
    SCREEN_WIDTH, INPUT_BG_COLOR, INPUT_BOX_VELOCITY, INPUT_BOX_ANGLE, BLACK
)

def draw_stats(surface, simulation_theme, text_velocity, text_angle, time_elapsed, FONT, INPUT_FONT, color_angle, color_velocity, velocity):
    pygame.draw.rect(surface, INPUT_BG_COLOR, INPUT_BOX_VELOCITY, border_radius=8)
    pygame.draw.rect(surface, color_velocity, INPUT_BOX_VELOCITY, 3, border_radius=8)
    text_surface_velocity = INPUT_FONT.render(text_velocity, True, BLACK)
    surface.blit(text_surface_velocity, (INPUT_BOX_VELOCITY.x + 14, INPUT_BOX_VELOCITY.y + 8))

    pygame.draw.rect(surface, INPUT_BG_COLOR, INPUT_BOX_ANGLE, border_radius=8)
    pygame.draw.rect(surface, color_angle, INPUT_BOX_ANGLE, 3, border_radius=8)
    text_surface_angle = INPUT_FONT.render(text_angle, True, BLACK)
    surface.blit(text_surface_angle, (INPUT_BOX_ANGLE.x + 14, INPUT_BOX_ANGLE.y + 8))

    label_velocity = FONT.render("Initial Velocity (m/s):", True, simulation_theme.text_color)
    surface.blit(label_velocity, (20, 50))
    label_angle = FONT.render("Launch Angle (degrees):", True, simulation_theme.text_color)
    surface.blit(label_angle, (20, 140))
    label_start = FONT.render("Press SPACE to launch", True, simulation_theme.text_color)
    surface.blit(label_start, (20, 240))
    label_restart = FONT.render("Press ESC to reset", True, simulation_theme.text_color)
    surface.blit(label_restart, (20, 270))

    info_x = SCREEN_WIDTH - 360
    info_y_start = 50

    theme_text = FONT.render(simulation_theme.name , True, simulation_theme.text_color)
    theme_rect = theme_text.get_rect()
    theme_rect.centerx = SCREEN_WIDTH // 2
    theme_rect.y = 10
    surface.blit(theme_text, theme_rect)
    
    velocity_text = FONT.render(f"Required Velocity: {velocity:.2f} m/s", True, simulation_theme.text_color)
    time_text = FONT.render(f"Time: {time_elapsed:.2f}s", True, simulation_theme.text_color)

    surface.blit(velocity_text, (info_x, info_y_start))
    surface.blit(time_text, (info_x, info_y_start + 40))