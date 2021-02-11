This directory uses `pkgutil` to find all modules.

```
[user@host static_approach]$ python3 dynamic.py 
```

ADVANTAGES:

* Does not require any boilerplate in the entities

DISADVANTAGES:

* `pkgutil`, `importlib`, `inspect`, modules and packages are relatively uncommonly used, and the rules governing them are not well known.
