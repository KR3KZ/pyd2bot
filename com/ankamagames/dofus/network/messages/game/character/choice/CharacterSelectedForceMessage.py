from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class CharacterSelectedForceMessage(INetworkMessage):
    protocolId = 6158
    id:int
    
    
