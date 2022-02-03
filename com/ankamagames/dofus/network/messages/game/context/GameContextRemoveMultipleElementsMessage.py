from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameContextRemoveMultipleElementsMessage(NetworkMessage):
    elementsIds:list[int]
    

    def init(self, elementsIds:list[int]):
        self.elementsIds = elementsIds
        
        super().__init__()
    
    