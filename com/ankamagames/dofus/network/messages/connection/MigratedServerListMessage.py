from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class MigratedServerListMessage(NetworkMessage):
    protocolId = 970
    migratedServerIds:int
    
