# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 15:57:37 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()