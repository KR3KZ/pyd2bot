from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ServerSelectionMessage(INetworkMessage):
    protocolId = 214
    serverId:int
    
    
