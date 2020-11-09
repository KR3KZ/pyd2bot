class ParseGridFailed(TimeoutError):
    def __init__(self, grid):
        msg = ""
        if len(grid.unknown) > 1:
            msg = "While parsing combat grid encountered more thant one unknown cell.\n"
            msg += "List of unknown cells and their colors: \n"
            for cell in grid.unknown:
                msg += f"({cell.i}, {cell.j}), {str(cell.color)}\n"
        if not grid.bot:
            msg += "Failed to parse bot position in the grid.\n"
        if not grid.mobs:
            msg += "Failed to parse any mob positions in the grid."
        if not msg:
            msg = "Parse grid failed for unknown reason!!!"
        super(ParseGridFailed, self).__init__(msg)


class FindPathFailed(Exception):
    def __init__(self, grid):
        super(FindPathFailed, self).__init__("Enable to find valid path to a target!")
        self.grid = grid


class ChangeMapFailed(Exception):
    def __init__(self, msg, coords):
        super(ChangeMapFailed, self).__init__(msg)
        self.coords = coords


class MoveToCellFailed(TimeoutError):
    def __init__(self, cell):
        super(MoveToCellFailed, self).__init__("Move to cell failed!")
        self.cell = cell


class UseSpellFailed(TimeoutError):
    def __init__(self, tgtCell):
        super(UseSpellFailed, self).__init__("Use spell timeout!")
        self.tgt = tgtCell


class BotDied(Exception):
    pass


class ParseMapCoordsFailed(Exception):
    pass
