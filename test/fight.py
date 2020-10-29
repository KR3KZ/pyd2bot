from core import env
from core.grid import Grid


grid = Grid(env.Region.COMBAT_R, env.VCELLS, env.HCELLS)
grid.parse()
