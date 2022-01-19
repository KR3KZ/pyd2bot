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


class WaitTurnTimedOut(Exception):
    pass


class BotDied(Exception):
    pass


class ParseMapCoordsFailed(Exception):
    pass
