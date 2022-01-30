from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.fight.arena.LeagueFriendInformations import LeagueFriendInformations


class GameRolePlayArenaInvitationCandidatesAnswerMessage(INetworkMessage):
    protocolId = 4913
    candidates:LeagueFriendInformations
    
    
