from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterInGroupLightInformations import MonsterInGroupLightInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterInGroupLightInformations import MonsterInGroupLightInformations


class BreachBranch(INetworkMessage):
    protocolId = 5320
    room:int
    element:int
    bosses:MonsterInGroupLightInformations
    map:int
    score:int
    relativeScore:int
    monsters:MonsterInGroupLightInformations
    
    
