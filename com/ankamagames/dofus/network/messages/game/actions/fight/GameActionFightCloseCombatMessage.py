from com.ankamagames.dofus.network.messages.game.actions.fight.AbstractGameActionFightTargetedAbilityMessage import AbstractGameActionFightTargetedAbilityMessage


class GameActionFightCloseCombatMessage(AbstractGameActionFightTargetedAbilityMessage):
    weaponGenericId:int
    

    def init(self, weaponGenericId:int, targetId:int, destinationCellId:int, critical:int, actionId:int, sourceId:int):
        self.weaponGenericId = weaponGenericId
        
        super().__init__(targetId, destinationCellId, critical, actionId, sourceId)
    
    