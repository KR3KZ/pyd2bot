from com.ankamagames.jerakine.types.positions.MapPoint import Point


class Rectangle:
    @property
    def bottom(self, get,set) -> float:
        pass
    @property
    def bottomRight(self, get,set) -> Point:
        pass
    height : float
    @property
    def left(self, get,set) -> float:
        pass
    @property
    def right(self, get,set) -> float:
        pass
    @property
    def size(self, get,set) -> Point:
        pass
    @property
    def top(self, get,set) -> float:
        pass
    @property
    def topLeft(self, get,set) -> Point:
        pass

    width : float
    x : float
    y : float

    def __init__(self, x : float = 0, y : float = 0, width : float = 0, height : float = 0):
        pass
    def clone(self) -> 'Rectangle':
        pass
    def __contains__(self, x : float, y : float) -> bool:
        pass
    def containsPoint(self, point : Point) -> bool:
        pass
    def containsRect(self, rect : 'Rectangle') -> bool:
        pass
    def copyFrom(self, sourceRect : 'Rectangle') :
        pass
    def __eq__(self, toCompare : 'Rectangle') -> bool:
        pass
    def get_bottom(self) -> float:
        pass
    def get_bottomRight(self) -> Point:
        pass
    def get_left(self) -> float:
        pass
    def get_right(self) -> float:
        pass
    def get_size(self) -> Point:
        pass
    def get_top(self) -> float:
        pass
    def get_topLeft(self) -> Point:
        pass
    def inflate(self, dx : float, dy : float) -> None:
        pass
    def inflatePoint(self, point : Point) -> None:
        pass
    def intersection(self, toIntersect : 'Rectangle') -> 'Rectangle':
        pass
    def intersects(self, toIntersect : 'Rectangle') -> bool:
        pass
    def isEmpty(self) -> bool:
        pass
    def offset(self, dx : float, dy : float) -> None:
        pass
    def offsetPoint(self, point : Point) -> None:
        pass
    def setEmpty(self) -> None:
        pass
    def setTo(self, xa : float, ya : float, widtha : float, heighta : float) -> None:
        pass
    def set_bottom(self, value : float) -> float:
        pass
    def set_bottomRight(self, value : Point) -> Point:
        pass
    def set_left(self, value : float) -> float:
        pass
    def set_right(self, value : float) -> float:
        pass
    def set_size(self, value : Point) -> Point:
        pass
    def set_top(self, value : float) -> float:
        pass
    def set_topLeft(self, value : Point) -> Point:
        pass
    def toString(self) -> str:
        pass
    def union(self, toUnion : 'Rectangle') -> 'Rectangle':
        pass
