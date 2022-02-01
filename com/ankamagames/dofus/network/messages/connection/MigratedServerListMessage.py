from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MigratedServerListMessage(NetworkMessage):
    migratedServerIds:list[int]
    
    
