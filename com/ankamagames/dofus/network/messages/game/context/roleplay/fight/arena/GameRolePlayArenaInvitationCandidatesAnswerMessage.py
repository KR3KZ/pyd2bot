from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.fight.arena.LeagueFriendInformations import LeagueFriendInformations


@dataclass
class GameRolePlayArenaInvitationCandidatesAnswerMessage(NetworkMessage):
    candidates:list[LeagueFriendInformations]
    
    
    def __post_init__(self):
        super().__init__()
    