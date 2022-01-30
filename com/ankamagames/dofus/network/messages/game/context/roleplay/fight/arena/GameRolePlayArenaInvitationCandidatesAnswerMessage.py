from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.fight.arena.LeagueFriendInformations import LeagueFriendInformations


class GameRolePlayArenaInvitationCandidatesAnswerMessage(NetworkMessage):
    protocolId = 4913
    candidates:list[LeagueFriendInformations]
    
