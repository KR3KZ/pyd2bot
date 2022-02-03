from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightTackledMessage(AbstractGameActionMessage):
    tacklersIds:list[int]
    

    def init(self, tacklersIds:list[int], actionId:int, sourceId:int):
        self.tacklersIds = tacklersIds
        
        super().__init__(actionId, sourceId)
    
    