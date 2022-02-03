from com.ankamagames.dofus.network.messages.game.context.GameContextRemoveMultipleElementsMessage import GameContextRemoveMultipleElementsMessage


class GameContextRemoveMultipleElementsWithEventsMessage(GameContextRemoveMultipleElementsMessage):
    elementEventIds:list[int]
    

    def init(self, elementEventIds:list[int], elementsIds:list[int]):
        self.elementEventIds = elementEventIds
        
        super().__init__(elementsIds)
    
    