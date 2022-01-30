from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterInGroupLightInformations import MonsterInGroupLightInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterInGroupInformations import MonsterInGroupInformations


class GroupMonsterStaticInformations(NetworkMessage):
    protocolId = 9226
    mainCreatureLightInfos:MonsterInGroupLightInformations
    underlings:list[MonsterInGroupInformations]
    
