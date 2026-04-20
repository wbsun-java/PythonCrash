# Chapter 3 — Introducing Lists
# Key examples from the book

# --- Defining and accessing a list ---
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)          # whole list
print(bicycles[0])       # first item: 'trek'
print(bicycles[-1])      # last item: 'specialized'

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

# --- Changing elements ---
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'
print(motorcycles)   # ['ducati', 'yamaha', 'suzuki']

# --- Adding elements ---
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')            # add to end
motorcycles.insert(0, 'triumph')        # insert at position
print(motorcycles)

# --- Removing elements ---
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
del motorcycles[0]                      # delete by index
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
popped = motorcycles.pop()              # remove and return last item
print(popped)       # 'ducati'

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')            # remove by value
print(motorcycles)

# --- Sorting ---
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()                             # permanent sort
print(cars)

cars.sort(reverse=True)                 # reverse sort
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))                     # temporary sort (original unchanged)
print(cars)

cars.reverse()                          # reverse order (not alphabetical)
print(cars)

# --- Length ---
print(len(cars))   # 4
