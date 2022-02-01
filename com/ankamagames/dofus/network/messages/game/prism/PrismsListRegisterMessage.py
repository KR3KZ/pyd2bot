from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class PrismsListRegisterMessage(INetworkMessage):
    protocolId = 4105
    listen:int
    
    
