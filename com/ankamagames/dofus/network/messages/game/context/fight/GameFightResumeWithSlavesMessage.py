from com.ankamagames.dofus.network.messages.game.context.fight.GameFightResumeMessage import GameFightResumeMessage
from com.ankamagames.dofus.network.types.game.context.fight.GameFightResumeSlaveInfo import GameFightResumeSlaveInfo


class GameFightResumeWithSlavesMessage(GameFightResumeMessage):
    protocolId = 6205
    slavesInfo:GameFightResumeSlaveInfo
    
    
