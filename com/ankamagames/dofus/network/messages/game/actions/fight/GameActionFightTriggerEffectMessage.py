from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightDispellEffectMessage import GameActionFightDispellEffectMessage


class GameActionFightTriggerEffectMessage(GameActionFightDispellEffectMessage):
    

    def init(self, boostUID:int, targetId:int, verboseCast:bool, actionId:int, sourceId:int):
        
        super().__init__(boostUID, targetId, verboseCast, actionId, sourceId)
    
    