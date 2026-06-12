from dataclasses import dataclass 


@dataclass
class Settings:
    """Store all settings for Alien Invasion"""
    screen_width: int = 1200
    screen_height: int = 800
    bg_color: tuple[int, int, int] = (230, 230, 230)
    ship_speed: float = 2.5

    bullet_speed: float = 8.0
    bullet_width: int = 3
    bullet_height: int = 15
    bullet_color: tuple[int, int, int] = (60, 60, 60)
    bullets_allowed: int = 10 
