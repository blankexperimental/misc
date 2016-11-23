import members
print members.importall()

import inspect
print inspect.getmembers(members.member1, inspect.isclass)