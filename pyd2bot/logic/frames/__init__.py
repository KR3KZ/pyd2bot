from .iFrame import IFrame
from .authentificationFrame import AuthentificationFrame
from .serverLoginFrame import ServerLoginFrame
from .gameStartingFrame import GameStartingFrame
from .rolePlayMovementFrame import RolePlayMovementFrame
from .rolePlayInteractiveFrame import RolePlayInteractiveFrame


_cls_frames:list[IFrame] = [
    AuthentificationFrame,
    ServerLoginFrame,
    RolePlayMovementFrame,
    RolePlayInteractiveFrame,
    GameStartingFrame
]