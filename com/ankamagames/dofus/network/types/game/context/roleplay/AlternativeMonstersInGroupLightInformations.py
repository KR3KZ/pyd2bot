from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterInGroupLightInformations import MonsterInGroupLightInformations


class AlternativeMonstersInGroupLightInformations(INetworkMessage):
    protocolId = 1183
    playerCount:int
    monsters:MonsterInGroupLightInformations
    
    
