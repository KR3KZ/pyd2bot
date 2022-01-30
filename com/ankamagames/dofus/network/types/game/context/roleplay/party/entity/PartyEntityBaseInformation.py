from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook


class PartyEntityBaseInformation(INetworkMessage):
    protocolId = 8087
    indexId:int
    entityModelId:int
    entityLook:EntityLook
    
    
