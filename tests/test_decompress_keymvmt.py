# [8488, 4507]
compressed = 8488
orientation = compressed >> 12 
cellId =  compressed & 4095
print(cellId, orientation)
# compressed2 = orientation << 12 + cellId & 4095
# assert compressed == compressed2