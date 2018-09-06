# -*- coding: utf-8 -*-
#
# Author:: Jonny
# Date:: 2018/4/26

import os

from requirements.lib import get_pip_list_dict, get_requirements_dict

pip_list_dict = get_pip_list_dict()

requir_dcit = get_requirements_dict("requirements.txt")

# uninstall
for item in pip_list_dict.keys():
    if item == "pip" or item == "setuptools":
        continue
    if item not in requir_dcit:
        cmd = "pip uninstall %s -y" % item
        print(cmd)
        os.popen(cmd)

# install
# os.popen("pip install -r requirements.txt").read()

for k, v in requir_dcit.items():
    os.popen("pip install %s==%s" % (k, v))
