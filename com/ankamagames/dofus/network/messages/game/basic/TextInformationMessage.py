from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TextInformationMessage(NetworkMessage):
    msgType:int
    msgId:int
    parameters:list[str]
    

    def init(self, msgType:int, msgId:int, parameters:list[str]):
        self.msgType = msgType
        self.msgId = msgId
        self.parameters = parameters
        
        super().__init__()
    
    