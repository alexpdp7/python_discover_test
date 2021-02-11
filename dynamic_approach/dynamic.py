import importlib
import inspect
import pkgutil

import dynamic
import plugins


class Exercise:
    pass

def find_plugins():
    plugin_classes = []

    for module in pkgutil.walk_packages(plugins.__path__, plugins.__name__ + '.'):
        module = importlib.import_module(module.name)
        for element in module.__dict__.values():
            if inspect.isclass(element) and dynamic.Exercise in inspect.getmro(element):
                plugin_classes.append(element)

    return plugin_classes



if __name__ == "__main__":
    print(find_plugins())
