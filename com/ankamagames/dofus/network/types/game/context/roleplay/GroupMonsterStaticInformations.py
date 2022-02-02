from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterInGroupLightInformations import MonsterInGroupLightInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterInGroupInformations import MonsterInGroupInformations


@dataclass
class GroupMonsterStaticInformations(NetworkMessage):
    mainCreatureLightInfos:MonsterInGroupLightInformations
    underlings:list[MonsterInGroupInformations]
    
    
    def __post_init__(self):
        super().__init__()
    