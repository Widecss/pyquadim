import os

from wheel.vendored.packaging.tags import sys_tags

tag = next(sys_tags())
whl_list = os.walk("./dist")
for whl in whl_list:
    if whl.endswith("linux_x86_64.whl"):
        new = whl.replace("linux_x86_64.whl", f"{tag.platform}.whl")
        os.rename(f"./dist/{whl}", f"./dist/{new}")
