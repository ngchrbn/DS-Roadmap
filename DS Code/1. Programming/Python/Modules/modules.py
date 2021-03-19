"""
Modular programming refers to the process of breaking
a large, unwieldy programming task into separate, smaller,
more manageable subtasks or modules.
Individual modules can then be cobbled together
like building blocks to create a larger application.

==> A module is accessed by: 'import module_name'
                            'import module_name as x'
                            'from module_name import function1'
                            'from module_name import *'
                            'from module_name import function1 as fx'
==> To create a module just create .py file with the code inside
==> __all__ is used by both packages and modules to 
    control what is imported when import * is specified.
    But the default behavior differs:
    --> For a package, when __all__ is not defined, 
        import * does not import anything.
    --> For a module, when __all__ is not defined, 
        import * imports everything (except—you guessed 
        it—names starting with an underscore).

==> Packages can have subpackages:
    --> Importing still works the same as shown previously
    --> a module in one subpackage can reference objects
        in a sibling subpackage (in the event that the 
        sibling contains some functionality that you need):
        * You can use absolute import (ex: from pkg.sub_pkg1.mod import foo)
        * Or Use relative import (ex: from ..sub_pkg1..mod import foo)
            --> Where '..' refers to the package one level up.
"""

import mod
import sys
print(mod.__file__)