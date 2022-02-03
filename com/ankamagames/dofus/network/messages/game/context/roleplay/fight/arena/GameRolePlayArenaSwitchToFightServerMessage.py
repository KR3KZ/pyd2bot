from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayArenaSwitchToFightServerMessage(NetworkMessage):
    address:str
    ports:list[int]
    ticket:list[int]
    

    def init(self, address:str, ports:list[int], ticket:list[int]):
        self.address = address
        self.ports = ports
        self.ticket = ticket
        
        super().__init__()
    
    