from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class HavenBagPackListMessage(NetworkMessage):
    protocolId = 268
    packIds:int
    
    
