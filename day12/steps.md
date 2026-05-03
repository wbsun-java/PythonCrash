# Day 12 — Build Steps

Build in this order. The game should run at every step — never in a broken state.

```
Step 1 — settings.py         just data, no logic, no Pygame needed
Step 2 — alien_invasion.py   window + game loop (empty but runnable)
Step 3 — ship.py             draw the ship on screen
Step 4 — movement            arrow keys move the ship left/right
Step 5 — bullet.py           Space fires bullets upward
```

---

## Step 1 — settings.py

Create a class called `Settings`. In `__init__`, define:

```python
screen_width    = 1200
screen_height   = 800
bg_color        = (230, 230, 230)   # light gray
ship_speed      = 1.5
bullet_speed    = 2.0
bullet_width    = 3
bullet_height   = 15
bullet_color    = (60, 60, 60)
bullets_allowed = 3
```

No imports. No Pygame. Just a class with attributes.

---

## Step 2 — alien_invasion.py

Open a window and run the game loop. The window is empty but it runs.

```python
import sys
import pygame
from settings import Settings

class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
```

**Run:** `python alien_invasion.py` — you should see a gray window.

---

## Step 3 — ship.py

Load the ship image and place it at the bottom center.

```python
import pygame

class Ship:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
```

In `alien_invasion.py`, add:

- `from ship import Ship` at the top
- `self.ship = Ship(self)` at the end of `__init__`
- `self.ship.blitme()` in `_update_screen()`, BEFORE `pygame.display.flip()`

> You need `day12/images/ship.bmp` — download from https://ehmatthes.github.io/pcc_3e/

---

## Step 4 — Movement

Move the ship with arrow keys. Keep it within the screen edges.

**Key idea:** Store position as a float (`self.x`) for smooth movement.
Copy it to `self.rect.x` each frame (rect only stores integers).

**Add to `ship.py` — in `__init__` after `midbottom`:**

```python
self.moving_right = False
self.moving_left  = False
self.x = float(self.rect.x)
self.settings = ai_game.settings
```

**Add `update()` to `ship.py`:**

```python
def update(self):
    if self.moving_right and self.rect.right < self.screen_rect.right:
        self.x += self.settings.ship_speed
    if self.moving_left and self.rect.left > 0:
        self.x -= self.settings.ship_speed
    self.rect.x = self.x
```

**Add to `_check_events()` in `alien_invasion.py`:**

```python
if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_RIGHT:
        self.ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        self.ship.moving_left = True

if event.type == pygame.KEYUP:
    if event.key == pygame.K_RIGHT:
        self.ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        self.ship.moving_left = False
```

**Add to `alien_invasion.py` and call it in `run_game()` before `_update_screen()`:**

```python
def _update_ship(self):
    self.ship.update()
```

> Why KEYDOWN + KEYUP? KEYDOWN fires once on press. KEYUP fires once on release.
> The flag (`moving_right`) keeps the ship moving every frame while the key is held.

---

## Step 5 — bullet.py

Create a bullet on Space. Bullets move upward. Remove them when off screen.

```python
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen   = ai_game.screen
        self.settings = ai_game.settings
        self.color    = self.settings.bullet_color
        self.rect = pygame.Rect(
            0, 0,
            self.settings.bullet_width,
            self.settings.bullet_height
        )
        self.rect.midtop = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed   # upward = y decreases
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
```

**Add to `alien_invasion.py`:**

At the top:

```python
from pygame.sprite import Group
from bullet import Bullet
```

In `__init__`:

```python
self.bullets = Group()
```

New methods:

```python
def _fire_bullet(self):
    if len(self.bullets) < self.settings.bullets_allowed:
        self.bullets.add(Bullet(self))

def _update_bullets(self):
    self.bullets.update()
    for bullet in self.bullets.copy():
        if bullet.rect.bottom <= 0:
            self.bullets.remove(bullet)
```

In `_check_events()`, inside the KEYDOWN block:

```python
elif event.key == pygame.K_SPACE:
    self._fire_bullet()
```

Call `self._update_bullets()` in `run_game()`.

In `_update_screen()`, before `flip()`:

```python
for bullet in self.bullets.sprites():
    bullet.draw_bullet()
```

---

## What you should have at the end of Day 12

- Gray window opens
- Ship sits at bottom center
- Arrow keys move the ship left/right, stops at edges
- Space fires bullets upward (max 3 on screen)
- Bullets disappear when they reach the top

---

## Common mistakes

| Mistake                              | Effect                  | Fix                                      |
|--------------------------------------|-------------------------|------------------------------------------|
| Drawing ship AFTER `flip()`          | Ship invisible          | Always draw before `flip()`              |
| Moving `rect.x` directly            | Choppy movement         | Use float `self.x`, copy to `rect.x`     |
| Not removing off-screen bullets      | Memory grows forever    | Check `bullet.rect.bottom <= 0`          |
| Only KEYDOWN, no KEYUP               | Ship won't stop moving  | Set flag False on KEYUP                  |
