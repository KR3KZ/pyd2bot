from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeSetCraftRecipeMessage(NetworkMessage):
    protocolId = 1333
    objectGID:int
    
    
