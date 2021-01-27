# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 16:07:22 2021

@author: USER
"""

from mcpi.minecraft import Minecraft as mc
mcs = mc.create()
x,y,z=mcs.player.getTilePos()
mcs.setSign(x,y,z,68,0,"I Love","Minecraft","and Python")