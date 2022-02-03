from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.look.SubEntity import SubEntity
    


class EntityLook(NetworkMessage):
    bonesId:int
    skins:list[int]
    indexedColors:list[int]
    scales:list[int]
    subentities:list['SubEntity']
    

    def init(self, bonesId:int, skins:list[int], indexedColors:list[int], scales:list[int], subentities:list['SubEntity']):
        self.bonesId = bonesId
        self.skins = skins
        self.indexedColors = indexedColors
        self.scales = scales
        self.subentities = subentities
        
        super().__init__()
    
    