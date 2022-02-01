from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.look.SubEntity import SubEntity


class EntityLook(NetworkMessage):
    bonesId:int
    skins:list[int]
    indexedColors:list[int]
    scales:list[int]
    subentities:list[SubEntity]
    
    
