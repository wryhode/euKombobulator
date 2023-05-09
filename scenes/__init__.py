# Imports all scenes in "{project root}/scenes" directory

import os 
modules = []
filelist = os.listdir(os.getcwd()+"/scenes")
for f in filelist:
    if f.endswith(".py") and not f == "__init__.py":
        modules.append(f[:-3])
__all__ = modules
print(f"Imported scenes:")
for i in modules:
    print(f"\t{i}")