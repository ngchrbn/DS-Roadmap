"""

If a file named __init__.py is present in a package
directory, it is invoked when the package or 
a module in the package is imported.
This can be used for execution of package initialization
code, such as initialization of package-level data.

==> __init__.py can also be used to effect automatic
    importing of modules from a package.

==> Note: Much of the Python documentation states that
    an __init__.py file must be present in the package
    directory when creating a package. 
    This was once true. It used to be that the very 
    presence of __init__.py signified to Python that 
    a package was being defined. 
    The file could contain initialization code or 
    even be empty, but it had to be present.

    Starting with Python 3.3, Implicit Namespace Packages
    were introduced. These allow for the creation of a 
    package without any __init__.py file. 
    Of course, it can still be present if package 
    initialization is needed. But it is no longer 
    required.

==> Using 'from pkg import *':
    if the __init__.py file in the package directory 
    contains a list named '__all__', it is taken to be 
    a list of modules that should be imported when the 
    statement from <package_name> import * is encountered
    If __all__ is not present in the __init__.py, the statement
    'from pkg import *' will not import anything

"""

print(f'Invoking __init__.py for {__name__}')

__all__ = [
    'mod1',
    'mod2'
]