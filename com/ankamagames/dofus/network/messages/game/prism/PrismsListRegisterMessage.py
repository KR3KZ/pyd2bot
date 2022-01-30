from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class PrismsListRegisterMessage(INetworkMessage):
    protocolId = 4105
    listen:int
    
    
