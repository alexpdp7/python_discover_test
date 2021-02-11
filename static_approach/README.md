This directory uses the simplest approach to find all entities.

```
[user@host static_approach]$ python3 static.py 
```

In this code, we import manually *all* modules containing entities we want to register.
Each entity registers itself by calling a `register` method.
This adds them to a list, we then can use this list to access all entities.

ADVANTAGES:

* Simplest implementation, easiest to understand

APPARENT DISADVANTAGES:

* Maintaining a list of all imports might seem error-prone.
  However, if a module is deleted or moved, running the software (or a simple test), will reveal the problem immediately.
  If you add a module, then you will not be able to use it until the imports are updated, so it's hard to miss.

DISADVANTAGES:

* This can be problematic if you truly require to mix entities from different projects.
* It can be considered ugly.

