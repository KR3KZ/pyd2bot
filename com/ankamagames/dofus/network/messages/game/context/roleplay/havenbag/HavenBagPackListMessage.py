from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class HavenBagPackListMessage(INetworkMessage):
    protocolId = 268
    packIds:int
    
    
