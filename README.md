# 2D Ballistic Physics Engine

A Python-based physics simulation designed to study projectile motion, collisions, and trajectory prediction. This project integrates rigid body dynamics (via Pymunk) with a custom rendering pipeline (via Pygame) to visualize kinematic concepts and solve dynamic interception problems.

<img width="1266" height="783" alt="Screenshot 2026-01-14 141304" src="https://github.com/user-attachments/assets/0d798ab8-fe25-4b84-9abf-fd66807c2881" />

## 🎯 Technical Objectives

* **Kinematic Simulation:** Accurate rendering of projectile motion under constant acceleration (**g**).
* **Collision Dynamics:** Implementation of rigid body interactions (elasticity, friction, mass) using the Chipmunk2D physics engine.
* **Predictive Analysis:** Real-time calculation of trajectory paths prior to launch.
* **Target Interception:** Algorithmic solution to calculate the required launch angle and velocity to hit a moving target.

## 🛠️ Technology Stack

* **Python 3.x**
* **Pygame:** Rendering engine and input handling.
* **Pymunk:** Physics engine wrapper for Chipmunk2D (handling gravity, damping, and collision pairs).
* **NumPy:** Vectorized operations for trajectory calculations.

## ⚙️ Key Features

### 1. Physics Engine Wrapper
The simulation separates the physical world state from the rendering loop. 
* **Gravity:** Variable gravity constants allowing simulation of different planetary environments (controlled via `logic.switch_theme`).
* **Damping:** Air resistance simulation applied to bodies in the `Pymunk.Space`.

### 2. Trajectory Prediction
Implemented in `physics.calculate_trajectory_preview`:
* Uses discretized time steps to project the parabolic path.
* Performs raycasting checks against scene boundaries (Walls/Floors) to clip the preview line visually.

### 3. Dynamic Interception Algorithm
Implemented in `physics.intercept_target`:
* Solves the kinematic equations to find a firing solution required to collide with a target moving at constant velocity.
* Iterates through time steps to find the intersection point between the projectile and the target's future position.

## 🕹️ Controls & Input

| Key / Action | Function |
| :--- | :--- |
| **Mouse Left Click** | Select Input Boxes or Set Target Position (if 'T' active) |
| **Enter** | Confirm/Deselect Input Box |
| **Up Arrow** | Increase Launch Angle (+5°) |
| **Down Arrow** | Decrease Launch Angle (-5°) |
| **Left / Right Arrow** | **Change Gravity** (Switch Planet Theme) |
| **Left Shift** | **Toggle Intercept Mode** (Auto-calculate firing solution) |
| **T** | Toggle Target Selection Mode |
| **N** | Spawn Projectile |
| **ESC** | Reset Simulation / Clear Scene |

## 🚀 Usage

### Prerequisites
Make sure you have Python 3.x installed. Then, install the required dependencies:

```bash
pip install pygame pymunk numpy
```

### Run

Run the command in the root of the project
```
python -m game.main
```
