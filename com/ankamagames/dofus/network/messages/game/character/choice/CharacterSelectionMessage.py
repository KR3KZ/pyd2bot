from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class CharacterSelectionMessage(INetworkMessage):
    protocolId = 3123
    id:int
    
    
