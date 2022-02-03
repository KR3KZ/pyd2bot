from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class SelectedServerDataMessage(NetworkMessage):
    serverId:int
    address:str
    ports:list[int]
    canCreateNewCharacter:bool
    ticket:list[int]
    

    def init(self, serverId:int, address:str, ports:list[int], canCreateNewCharacter:bool, ticket:list[int]):
        self.serverId = serverId
        self.address = address
        self.ports = ports
        self.canCreateNewCharacter = canCreateNewCharacter
        self.ticket = ticket
        
        super().__init__()
    
    