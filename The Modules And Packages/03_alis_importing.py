'''
In this example we are importing math_module.py and string_module.py
but there is a problem both these modules have same function name add()
so we can't import both of them at the same time.

To solve this problem we can use alias in importing module. This is why alias is important
when we are importing a module which has same function name.
'''
from math_module import add as m_add
from string_module import add as s_add

print(m_add(10, 20)) # prints 30
print(s_add("Wasiq", "Afnan")) # prints 30