from dataclasses import dataclass


@dataclass
class Settings:
    screen_width: int = 1200
    screen_height: int = 800
    background_color: tuple = (230, 230, 230)
    ship_speed: float = 2.0
    ship_direction: int = 1
    ship_limit: int = 3
    bullet_speed: float = 10.0
    bullet_width: int = 3
    bullet_height: int = 15
    bullet_color: tuple = (60, 60, 60)
    bullets_allowed: int = 3
    alien_speed: float = 1.0
    fleet_drop_speed: float = 10.0
    fleet_direction: int = 1
    