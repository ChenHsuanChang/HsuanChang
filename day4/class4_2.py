# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 10:04:25 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
number = 10 
for i in range (8):
    for j in range(number):
        mc.spawnEntity(x,y,z,64)
    number = number *2
    mc.postToChat("生成了"+str(number)+"FISH")