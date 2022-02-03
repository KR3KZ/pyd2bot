from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class RefreshFollowedQuestsOrderRequestMessage(NetworkMessage):
    quests:list[int]
    

    def init(self, quests:list[int]):
        self.quests = quests
        
        super().__init__()
    
    