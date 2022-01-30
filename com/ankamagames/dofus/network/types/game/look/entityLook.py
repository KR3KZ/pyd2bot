from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.look.SubEntity import SubEntity


class EntityLook(INetworkMessage):
    protocolId = 9546
    bonesId:int
    skins:int
    indexedColors:int
    scales:int
    subentities:SubEntity
    
    
