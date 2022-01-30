from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterInGroupLightInformations import MonsterInGroupLightInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterInGroupInformations import MonsterInGroupInformations


class GroupMonsterStaticInformations(INetworkMessage):
    protocolId = 9226
    mainCreatureLightInfos:MonsterInGroupLightInformations
    underlings:MonsterInGroupInformations
    
    
