from com.ankamagames.dofus.network.messages.game.context.GameContextRemoveMultipleElementsMessage import GameContextRemoveMultipleElementsMessage


class GameContextRemoveMultipleElementsWithEventsMessage(GameContextRemoveMultipleElementsMessage):
    protocolId = 7428
    elementEventIds:int
    
