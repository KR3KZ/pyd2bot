from .__IFrame import IFrame
from .connection.frames.authentificationFrame import AuthentificationFrame
from .connection.frames.serverLoginFrame import ServerLoginFrame
from .connection.frames.gameStartingFrame import GameStartingFrame
from .game.roleplay.frames.rolePlayMovementFrame import RolePlayMovementFrame
from .game.roleplay.frames.rolePlayInteractiveFrame import RolePlayInteractiveFrame
_cls_frames:list[IFrame] = [
    AuthentificationFrame,
    ServerLoginFrame,
    RolePlayMovementFrame,
    RolePlayInteractiveFrame,
    GameStartingFrame
]