from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class MigratedServerListMessage(INetworkMessage):
    protocolId = 970
    migratedServerIds:int
    
    
