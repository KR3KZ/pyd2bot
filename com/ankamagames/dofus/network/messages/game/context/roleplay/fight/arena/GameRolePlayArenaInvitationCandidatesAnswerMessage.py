from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.fight.arena.LeagueFriendInformations import LeagueFriendInformations


class GameRolePlayArenaInvitationCandidatesAnswerMessage(NetworkMessage):
    candidates:list[LeagueFriendInformations]
    
    
