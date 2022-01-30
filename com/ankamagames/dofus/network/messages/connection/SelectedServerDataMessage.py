from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class SelectedServerDataMessage(INetworkMessage):
    protocolId = 3966
    serverId:int
    address:str
    ports:int
    canCreateNewCharacter:bool
    ticket:int
    
    
