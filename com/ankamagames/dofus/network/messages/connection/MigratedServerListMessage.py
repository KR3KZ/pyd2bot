from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class MigratedServerListMessage(INetworkMessage):
    protocolId = 970
    migratedServerIds:int
    
    
