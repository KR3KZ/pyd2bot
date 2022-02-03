from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class SystemMessageDisplayMessage(NetworkMessage):
    hangUp:bool
    msgId:int
    parameters:list[str]
    

    def init(self, hangUp:bool, msgId:int, parameters:list[str]):
        self.hangUp = hangUp
        self.msgId = msgId
        self.parameters = parameters
        
        super().__init__()
    
    