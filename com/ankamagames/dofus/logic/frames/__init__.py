from .iFrame import IFrame
from .authentificationFrame import AuthentificationFrame
from .serverLoginFrame import ServerLoginFrame
from .gameStartingFrame import GameStartingFrame
from .rolePlayMovementFrame import RolePlayMovementFrame
from .rolePlayInteractiveFrame import RolePlayInteractiveFrame
from .gameFightFrame import GameFightFrame
from .serverRandRequestsFrame import ServerRandRequestsFrame
from .fightStartingFrame import FightStartingFrame

_cls_frames:list[IFrame] = [
    AuthentificationFrame,
    ServerLoginFrame,
    RolePlayMovementFrame,
    RolePlayInteractiveFrame,
    GameStartingFrame,
    FightStartingFrame,
    GameFightFrame,
    ServerRandRequestsFrame
]