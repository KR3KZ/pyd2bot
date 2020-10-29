from core import env
from core.grid import Grid


grid = Grid(env.COMBAT_R, env.VCELLS, env.HCELLS)
grid.parse()
