from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class CharacterSelectionMessage(INetworkMessage):
    protocolId = 3123
    id:int
    
    
