# Day 12 — Architecture

## What are we building?

A classic arcade game. You control a spaceship at the bottom of the screen.
Arrow keys move left and right. Space fires bullets upward.
Destroy all the aliens before they reach you. You have 3 lives.

---

## Why not one big file?

You *could* write the entire game in one file. It works at first.
Then it grows to 500 lines and you can't find anything.
Changing one thing breaks something unrelated.

The solution is **separation of concerns** — each file owns exactly one thing.
This is not a Pygame rule. It is a universal principle in all software.

---

## File structure

```
alien_invasion.py   the director — owns the game loop, coordinates everything
settings.py         read-only data: all numbers, colors, speeds in one place
ship.py             the Ship class — draws itself, moves itself
bullet.py           the Bullet class — spawned on Space, moves upward
alien.py            the Alien class — one alien; the fleet is a Group of many
```

`alien_invasion.py` is the only file that knows about all the others.
`ship.py` does not import `bullet.py`. `bullet.py` does not import `ship.py`.
They are independent. This is intentional.

**The test:** If you need to change how bullets move, you open one file — `bullet.py`.
Not `alien_invasion.py`. Not `settings.py`. Just `bullet.py`.
This is called the **Single Responsibility Principle**.

---

## The game loop

Every frame (~60 times per second), three things happen in order:

```
1. Check events    ← did the user press a key? close the window?
2. Update state    ← move the ship, move bullets, check collisions
3. Draw            ← paint everything, then flip to the screen
```

"Flip" swaps the hidden frame (where you drew) to the visible screen.
This is what makes animation smooth — you never draw directly to the visible screen.

---

## Why is Settings a separate file?

Without it, magic numbers are scattered everywhere:

```python
# Bad — what does 1200 mean? what does (230,230,230) mean?
self.screen = pygame.display.set_mode((1200, 800))
self.screen.fill((230, 230, 230))
self.x += 1.5
```

With Settings, every number has a name and lives in one place:

```python
# Good — readable, change speed by editing ONE line in settings.py
self.x += self.settings.ship_speed
```

---

## Why does AlienInvasion own the game loop?

The loop needs access to the ship, bullets, aliens, screen, and settings.
Making it a class stores all of those as attributes (`self.ship`, `self.bullets`)
so every method can reach them without passing arguments everywhere.

---

## Why do Ship and Bullet inherit from Sprite?

`pygame.sprite.Sprite` gives you two things for free:

- Your object can join a `Group`
- The `Group` calls `.update()` on every sprite at once and handles collision detection

Without Sprite — manual and fragile:

```python
for bullet in bullets:
    bullet.update()
    if bullet.rect.bottom <= 0:
        bullets.remove(bullet)   # dangerous: removing while iterating
```

With Sprite + Group — clean and safe:

```python
self.bullets.update()                        # updates all at once
collisions = pygame.sprite.groupcollide(…)   # collision detection built-in
```

---

## Why does Ship receive `ai_game` (the whole game object)?

```python
self.ship = Ship(self)   # 'self' is the AlienInvasion instance
```

Ship needs the screen and settings. Instead of passing them separately:

```python
class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen      # takes what it needs
        self.settings = ai_game.settings
```

Short signature, and Ship can access anything it needs later without
changing its interface.

---

## Summary

| File                | One job                                                      |
|---------------------|--------------------------------------------------------------|
| `alien_invasion.py` | Run the game loop and coordinate all pieces                  |
| `settings.py`       | Store every configurable number in one place                 |
| `ship.py`           | Draw the ship and respond to movement flags                  |
| `bullet.py`         | Draw a bullet and move it upward each frame                  |
| `alien.py`          | Draw an alien and move it in the fleet direction             |
