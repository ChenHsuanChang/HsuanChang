# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 15:55:33 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
from time import sleep
import random
mc = Minecraft.create()
myID = mc.getPlayerEntityId("APE_52")
mineral = [14,15,56,73,129]
while True:
    sleep(0.5)
    r = random.choice(mineral)
    x,y,z = mc.entity.getTilePos(myID)
    mc.setBlocks(x+1,y,z+1,x-1,y+3,z-1,r)