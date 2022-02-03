from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightDispellMessage import GameActionFightDispellMessage


class GameActionFightDispellSpellMessage(GameActionFightDispellMessage):
    spellId:int
    

    def init(self, spellId:int, targetId:int, verboseCast:bool, actionId:int, sourceId:int):
        self.spellId = spellId
        
        super().__init__(targetId, verboseCast, actionId, sourceId)
    
    