from com.ankamagames.dofus.network.messages.game.context.GameContextRemoveElementMessage import GameContextRemoveElementMessage


class GameContextRemoveElementWithEventMessage(GameContextRemoveElementMessage):
    protocolId = 9473
    elementEventId:int
    
