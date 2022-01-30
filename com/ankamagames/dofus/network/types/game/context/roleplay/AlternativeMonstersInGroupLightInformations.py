from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterInGroupLightInformations import MonsterInGroupLightInformations


class AlternativeMonstersInGroupLightInformations(NetworkMessage):
    protocolId = 1183
    playerCount:int
    monsters:MonsterInGroupLightInformations
    
