from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeSetCraftRecipeMessage(INetworkMessage):
    protocolId = 1333
    objectGID:int
    
    
