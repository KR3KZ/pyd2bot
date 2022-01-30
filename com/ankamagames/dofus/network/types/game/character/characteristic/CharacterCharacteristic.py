from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class CharacterCharacteristic(INetworkMessage):
    protocolId = 4565
    characteristicId:int
    
    
