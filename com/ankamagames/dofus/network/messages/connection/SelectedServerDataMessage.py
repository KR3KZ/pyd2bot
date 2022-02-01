from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class SelectedServerDataMessage(INetworkMessage):
    protocolId = 3966
    serverId:int
    address:str
    ports:int
    canCreateNewCharacter:bool
    ticket:int
    
    
