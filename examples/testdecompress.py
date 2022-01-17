from core import dofus, env
# how to decompress keymovement info

compressed = 12514
orientation = compressed >> 12 
cellId =  compressed & 4095
print(orientation, cellId)
x, y = dofus.getCellCoords(cellId)
px, py = dofus.getCellPixelCenterCoords(x, y)
env.focusDofusWindow()
env.move(px,py)
