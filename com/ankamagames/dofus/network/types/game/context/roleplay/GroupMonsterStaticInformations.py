from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterInGroupLightInformations import MonsterInGroupLightInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterInGroupInformations import MonsterInGroupInformations


class GroupMonsterStaticInformations(NetworkMessage):
    mainCreatureLightInfos:MonsterInGroupLightInformations
    underlings:list[MonsterInGroupInformations]
    
    
