from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterInGroupLightInformations import MonsterInGroupLightInformations


class AlternativeMonstersInGroupLightInformations(NetworkMessage):
    playerCount:int
    monsters:list[MonsterInGroupLightInformations]
    
    
