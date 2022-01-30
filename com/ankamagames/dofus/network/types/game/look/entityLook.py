from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.look.SubEntity import SubEntity


class EntityLook(NetworkMessage):
    protocolId = 9546
    bonesId:int
    skins:int
    indexedColors:int
    scales:int
    subentities:SubEntity
    
    
