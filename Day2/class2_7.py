# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 15:48:27 2021

@author: USER
"""

from mcpi.minecraft import Minecraft as mc
mcs = mc.create()
userName = input ('What\'s your name?')
message = input ("What\'s your message?")
mcs.postToChat("["+userName+"]"+message)