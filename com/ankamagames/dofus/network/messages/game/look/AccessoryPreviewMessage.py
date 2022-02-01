from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook


class AccessoryPreviewMessage(INetworkMessage):
    protocolId = 5355
    look:EntityLook
    
    
