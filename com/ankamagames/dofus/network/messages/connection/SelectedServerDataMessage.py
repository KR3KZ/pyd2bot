from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class SelectedServerDataMessage(NetworkMessage):
    protocolId = 3966
    serverId:int
    address:str
    ports:list[int]
    canCreateNewCharacter:bool
    ticket:list[int]
    
