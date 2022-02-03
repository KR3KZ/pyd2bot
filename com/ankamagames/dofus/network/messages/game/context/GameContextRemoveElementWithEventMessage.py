from com.ankamagames.dofus.network.messages.game.context.GameContextRemoveElementMessage import GameContextRemoveElementMessage


class GameContextRemoveElementWithEventMessage(GameContextRemoveElementMessage):
    elementEventId:int
    

    def init(self, elementEventId:int, id:int):
        self.elementEventId = elementEventId
        
        super().__init__(id)
    
    