from importlib import import_module


def clear_screen():
    print("\n" * 25)


def blue(string: str):
    return string


def back_to_main():
    start = import_module("main").start
    start()
