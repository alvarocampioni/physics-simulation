import random

from data.config import (
    START_X, START_Y, PIXELS_PER_METER, TRAJECTORY_INTERVAL,
    COLOR_ACTIVE, COLOR_INACTIVE, INPUT_BOX_VELOCITY, INPUT_BOX_ANGLE, 
    SPAWN_INTERVAL, PLANET_THEMES, INTERCEPT_SPEED_LIMIT
)

from engine.obstacle import MovingObstacle

from engine.physics import calculate_velocity, intercept_target, launch_projectile

def switch_theme(delta, current):
    current = (current + delta) % len(PLANET_THEMES)
    theme = PLANET_THEMES[current]
    return theme, theme.gravity * PIXELS_PER_METER

def update_ui_state(state):
    state.color_velocity = COLOR_ACTIVE if state.active_box == INPUT_BOX_VELOCITY else COLOR_INACTIVE
    state.color_angle = COLOR_ACTIVE if state.active_box == INPUT_BOX_ANGLE else COLOR_INACTIVE

def update_sprites(state, delta_time):
    state.moving_sprites.update(delta_time)
    state.structure_sprites.update()

def update_required_velocity(state):
    if state.target_y != 0.0 and state.target_x != 0.0:
        state.required_velocity = calculate_velocity(
            state.target_x, state.target_y,
            state.text_angle, state.simulation_theme.gravity,
            START_X, START_Y
        )

def update_trajectory(state, delta_time):
    state.traj_timer += delta_time
    if state.running_simulation and state.traj_timer >= TRAJECTORY_INTERVAL:
        for projectile in state.moving_projectiles:
            if len(projectile.trajectory) > 100:
                projectile.trajectory.pop(0)
            projectile.trajectory.append(projectile.body.position)
        state.traj_timer = 0.0

def handle_interception(state):
    if state.intercept and state.static_projectiles and state.moving_obstacles:
        result = intercept_target(
            (START_X, START_Y),
            state.moving_obstacles[-1].body.position,
            state.moving_obstacles[-1].body.velocity,
            state.simulation_theme.gravity, INTERCEPT_SPEED_LIMIT
        )
        if result:
            state.text_velocity, state.text_angle = result
            launch_projectile(state.text_velocity, state.text_angle,
                              state.static_projectiles, state.space, state.moving_projectiles)
            state.running_simulation = True
        else:
            print("Not possible in these conditions")
        state.intercept = False

def handle_moving_obstacles(state, delta_time):
    if len(state.moving_obstacles) == 0 or (
        state.moving_obstacles[-1].body.isHit and state.moving_timer >= SPAWN_INTERVAL):
        
        state.moving_timer = 0.0
        new_obstacle = MovingObstacle(2000, 300, 128, 64, 
            (-random.randint(5, 10) * PIXELS_PER_METER, 0))
        
        state.moving_obstacles.append(new_obstacle)
        state.moving_sprites.add(new_obstacle)
        state.space.add(new_obstacle.body, new_obstacle.shape)

    if state.moving_obstacles[-1].body.isHit:
        state.moving_timer += delta_time

def update_simulation(state, delta_time):
    state.space.step(delta_time)
    update_ui_state(state)
    update_sprites(state, delta_time)
    update_required_velocity(state)
    update_trajectory(state, delta_time)
    handle_interception(state)
    handle_moving_obstacles(state, delta_time)
    state.time_elapsed += delta_time