import pymunk, math, numpy
from data.config import (
    FLOOR_Y, WALL_X, WALL_Y, WALL_WIDTH, 
    PIXELS_PER_METER
)

def intercept_target(proj_pos, target_pos, target_vel, gravity, max_speed, max_time=5.0, dt=1/60.0, tolerance=10):
    xs, ys = proj_pos
    xt0, yt0 = target_pos
    vtx, vty = target_vel
    g = gravity * PIXELS_PER_METER
    v = max_speed * PIXELS_PER_METER

    for t in numpy.arange(dt, max_time, dt):
        xt = xt0 + vtx * t
        yt = yt0 + vty * t

        dx = xt - xs
        dy = ys - yt  

        if dx == 0:
            continue  

        try:
            angle_rad = math.atan2(dy + 0.5 * g * t**2, dx)
            vx = v * math.cos(angle_rad)
            vy = v * math.sin(angle_rad)

            xp = xs + vx * t
            yp = ys - (vy * t - 0.5 * g * t**2)

            dist = math.hypot(xp - xt, yp - yt)

            if dist < tolerance:
                ang = round(math.degrees(angle_rad))
                if ang > 0 and ang < 90:
                    return str(max_speed), str(ang)
        except:
            continue

    return None

def start_falling(arbiter, space, data):
    flying_body = arbiter.shapes[0].body
    flying_body.velocity_func = pymunk.Body.update_velocity
    flying_body.isHit = True
    return True

def calculate_velocity(target_x, target_y, t_angle, gravity, start_x, start_y):
    try:
        angle = math.radians(float(t_angle))
    except ValueError:
        return 0.0

    dx = (target_x - start_x) / PIXELS_PER_METER
    dy = (start_y - target_y) / PIXELS_PER_METER 

    cos_theta = math.cos(angle)

    if cos_theta == 0:
        return 0.0

    try:
        denominator = 2 * (cos_theta**2) * (dx * math.tan(angle) - dy)
        if denominator <= 0:
            return 0.0

        velocity_squared = gravity * dx**2 / denominator
        if velocity_squared <= 0:
            return 0.0

        velocity_m_s = math.sqrt(velocity_squared)
        return velocity_m_s
    except:
        return 0.0


def calculate_trajectory_preview(start_pos, velocity, angle_rad, gravity, max_time=1.0, step=0.05):
    points = []
    x0, y0 = start_pos
    vx = velocity * math.cos(angle_rad)
    vy = velocity * math.sin(angle_rad)

    t = 0.0
    while t < max_time:
        x = x0 + vx * t
        y = y0 - (vy * t - 0.5 * gravity * t ** 2)
        if y > FLOOR_Y or (y > WALL_Y and x < WALL_WIDTH):
            break
        points.append((int(x), int(y)))
        t += step
    return points

def launch_projectile(text_velocity, text_angle, static_projectiles, space, moving_projectiles):
    try:
        current_velocity_real = float(text_velocity)
        current_angle_deg = float(text_angle)
    except ValueError:
        return False
    start_velocity = current_velocity_real * PIXELS_PER_METER
    start_angle = math.radians(current_angle_deg)

    projectile = static_projectiles.pop(0)
    x = start_velocity*math.cos(start_angle)
    y = -start_velocity*math.sin(start_angle)

    projectile.body.velocity = x, y

    projectile.body.angular_velocity = 0

    if projectile.shape not in space.shapes:
        space.add(projectile.body, projectile.shape)

    moving_projectiles.append(projectile)
    return True
