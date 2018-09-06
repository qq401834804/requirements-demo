#-*- coding: utf-8 -*-
#
# Author:: Jonny
# Date:: 2018/4/26

import os

from requirements.lib import get_requirements_dict

requir_dcit = get_requirements_dict("requirements.txt")

for k,v in requir_dcit.items():
    cmd = "pip install %s==%s"%(k,v)
    print(cmd)
    os.popen(cmd)
