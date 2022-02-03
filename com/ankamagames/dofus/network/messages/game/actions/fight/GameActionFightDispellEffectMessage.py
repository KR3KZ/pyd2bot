from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightDispellMessage import GameActionFightDispellMessage


class GameActionFightDispellEffectMessage(GameActionFightDispellMessage):
    boostUID:int
    

    def init(self, boostUID:int, targetId:int, verboseCast:bool, actionId:int, sourceId:int):
        self.boostUID = boostUID
        
        super().__init__(targetId, verboseCast, actionId, sourceId)
    
    