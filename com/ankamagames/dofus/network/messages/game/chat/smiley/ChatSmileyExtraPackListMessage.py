from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ChatSmileyExtraPackListMessage(NetworkMessage):
    packIds:list[int]
    

    def init(self, packIds:list[int]):
        self.packIds = packIds
        
        super().__init__()
    
    