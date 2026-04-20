# 20-Day Python Crash Course Learning Plan

Based on *Python Crash Course* by Eric Matthes.

---

## Part I: Basics (Days 1–12)

| Day | Chapter | Topics | Key Exercises |
|-----|---------|--------|---------------|
| **Day 1** | Ch 1 | Setup, running your first script, Hello World | Ex 1-1, 1-2, 1-3 |
| **Day 2** | Ch 2 | Variables, strings, numbers, comments, Zen of Python | Ex 2-1 through 2-11 |
| **Day 3** | Ch 3 | Lists: creating, accessing, modifying, adding, removing | Ex 3-1 through 3-7 |
| **Day 4** | Ch 3 cont. + Ch 4 start | Sorting, reversing, length; `for` loops, list slices | Ex 3-8 to 3-10, start Ch 4 |
| **Day 5** | Ch 4 | Working with lists: loops, slicing, tuples, list comprehensions | All Ch 4 exercises |
| **Day 6** | Ch 5 | `if` statements, comparisons, boolean logic, conditionals with lists | All Ch 5 exercises |
| **Day 7** | Ch 6 | Dictionaries: create, access, loop, nesting dicts/lists | All Ch 6 exercises |
| **Day 8** | Ch 7 | `input()`, `while` loops, flags, `break`/`continue` | All Ch 7 exercises |
| **Day 9** | Ch 8 | Functions: parameters, return values, `*args`, `**kwargs`, modules | All Ch 8 exercises |
| **Day 10** | Ch 9 | Classes: `__init__`, methods, inheritance, importing classes | All Ch 9 exercises |
| **Day 11** | Ch 10 | Reading/writing files, `with`, exceptions, `try/except/else`, JSON | All Ch 10 exercises |
| **Day 12** | Ch 11 | `unittest`, testing functions and classes, test cases | All Ch 11 exercises |

---

## Part II: Projects (Days 13–20)

### Project 1 — Alien Invasion (pygame game)

| Day | Chapter | What You Build |
|-----|---------|----------------|
| **Day 13** | Ch 12 | Game window, ship class, keyboard movement, bullets |
| **Day 14** | Ch 13 | Alien fleet, collision detection, game reset logic |
| **Day 15** | Ch 14 | Scoreboard, high score, difficulty levels, full playable game |

Install before Day 13: `pip install pygame`

### Project 2 — Data Visualization (matplotlib / Pygal)

| Day | Chapter | What You Build |
|-----|---------|----------------|
| **Day 16** | Ch 15 | Random walks, dice rolls, matplotlib charts, Pygal bar charts |
| **Day 17** | Ch 16 | CSV weather data, JSON earthquake data, world maps |
| **Day 18** | Ch 17 | GitHub API, Hacker News API, live JSON data → charts |

Install before Day 16: `pip install matplotlib numpy pygal`

### Project 3 — Web App (Django)

| Day | Chapter | What You Build |
|-----|---------|----------------|
| **Day 19** | Ch 18 | Django project, models, admin panel, views, templates, URLs |
| **Day 20** | Ch 19–20 | User accounts, login/logout, ownership rules, Bootstrap styling, deploy |

Install before Day 19: `pip install django`

---

## Pacing Notes

- **Days 1–5** are the fastest; exercises are short and concepts are simple.
- **Days 9–12** (functions, classes, files, testing) are the densest — these are the foundation for all three projects.
- **Days 13–15** require `pygame` installed in advance.
- **Days 16–18** require `matplotlib`, `numpy`, `pygal`.
- **Days 19–20** require `django` and a Heroku account for deployment.
