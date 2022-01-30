from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook


class AccessoryPreviewMessage(NetworkMessage):
    protocolId = 5355
    look:EntityLook
    
