class ParseCellFailed(Exception):
    pass


class ParseGridFailed(Exception):
    pass


class FindPathFailed(Exception):
    pass


class ChangeMapFailed(Exception):
    def __init__(self, msg, coords):
        super(ChangeMapFailed, self).__init__(msg)
        self.coords = coords


class BotDied(Exception):
    pass


class ParseMapCoordsFailed(Exception):
    pass
