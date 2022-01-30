from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook


class PartyEntityBaseInformation(NetworkMessage):
    protocolId = 8087
    indexId:int
    entityModelId:int
    entityLook:EntityLook
    
