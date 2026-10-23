import math

class CarPhysics:
    def __init__(self, x, y, mass):
        if mass <= 0:
            raise ValueError("mass must be positive")

        self.x = x
        self.y = y
        self.vx = 0.0
        self.vy = 0.0
        self.angle = 0.0
        self.mass = mass 

        self.engine_force = 200.0 + (mass * 0.25)  # Adjust engine force based on mass
        self.acceleration = self.engine_force / self.mass #F/m = a
        self.friction = 0.05
        self.max_speed = self.mass * 0.005  # Adjust max speed based on mass
        self.turning_coefficient = 10 / (self.mass * 1.2)

    def update(self, throttle, steering, dt, mu_k, mu_s, drifting):
        # Scale the physics calculations based on the frame time to maintain consistent behavior across different frame rates
        frame_scale = dt * 60

        # Calculate forward and right(perpendicular) vectors based on the car's angle
        forward_x = math.sin(self.angle)
        forward_y = -math.cos(self.angle)
        right_x = math.cos(self.angle)
        right_y = math.sin(self.angle)

        self.vx += forward_x * throttle * self.acceleration * frame_scale
        self.vy += forward_y * throttle * self.acceleration * frame_scale

        #dot product of forward vector and velocity vector to get the speed in the forward direction
        forward_speed = self.vx * forward_x + self.vy * forward_y
        self.angle += steering * forward_speed * self.turning_coefficient * frame_scale

        # Recalculate forward and right vectors based on the updated angle
        forward_x = math.sin(self.angle)
        forward_y = -math.cos(self.angle)
        right_x = math.cos(self.angle)
        right_y = math.sin(self.angle)

        # Apply friction and grip
        side_speed = self.vx * right_x + self.vy * right_y
        grip = min(1.0, max(0.0, mu_k if drifting else mu_s))
        grip_fraction = 1 - math.pow(1 - grip, frame_scale)
        self.vx -= side_speed * right_x * grip_fraction
        self.vy -= side_speed * right_y * grip_fraction

        # Apply drag to simulate air resistance
        drag = max(0.0, 1 - self.friction * frame_scale)
        self.vx *= drag
        self.vy *= drag

        #max speed check
        speed = math.hypot(self.vx, self.vy)
        if speed > self.max_speed:
            scale = self.max_speed / speed
            self.vx *= scale
            self.vy *= scale

        #update position
        self.x += self.vx * frame_scale
        self.y += self.vy * frame_scale
