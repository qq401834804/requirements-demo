#-*- coding: utf-8 -*-
#
# Author:: Jonny
# Date:: 2018/4/26

import os

os.popen("pip freeze > requirements.txt.current").read()