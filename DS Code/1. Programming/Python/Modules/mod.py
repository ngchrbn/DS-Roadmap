"""
==> When a .py file is imported as a module,
    Python sets the special dunder variable __name__
    to the name of the module.
    However, if a file is run as a standalone script,
    __name__ is (creatively) set to the string '__main__'.

==> For reasons of efficiency, a module is only loaded once
    per interpreter session. If a module contain executable
    statements as well, usually for initialization, there
    will be only executed the first time a module is imported.
    If you make a change to a module and need to reload it,
    you nedd to either restart the interpreter or use
    a function called 'reload()' from module 'importlib'
"""

s = "If Comrade Napoleon says it, it must be right."
a = [100, 200, 300]

def foo(arg):
    print(f'arg = {arg}')

class Foo:
    pass

if (__name__ == '__main__'):
    print('Executing as standalone script')
    print(s)
    print(a)
    foo('quux')
    x = Foo()
    print(x)
