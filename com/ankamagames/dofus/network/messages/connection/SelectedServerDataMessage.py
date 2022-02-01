from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class SelectedServerDataMessage(NetworkMessage):
    serverId:int
    address:str
    ports:list[int]
    canCreateNewCharacter:bool
    ticket:list[int]
    
    
