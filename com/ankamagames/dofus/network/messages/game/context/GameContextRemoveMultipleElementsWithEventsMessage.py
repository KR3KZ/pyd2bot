from com.ankamagames.dofus.network.messages.game.context.GameContextRemoveMultipleElementsMessage import GameContextRemoveMultipleElementsMessage


class GameContextRemoveMultipleElementsWithEventsMessage(GameContextRemoveMultipleElementsMessage):
    elementEventIds:list[int]
    
    
