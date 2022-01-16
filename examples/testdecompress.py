from core import dofus, env

# compressed = 12514
# orientation = compressed >> 12 
# cellId =  compressed & 4095

# print(orientation, cellId)
cellId = 7
x, y = dofus.getCellCoords(cellId)
px, py = dofus.getCellPixelCenterCoords(x, y)
env.focusDofusWindow()
env.click(px,py)
