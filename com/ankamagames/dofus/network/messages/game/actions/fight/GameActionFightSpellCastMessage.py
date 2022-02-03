from com.ankamagames.dofus.network.messages.game.actions.fight.AbstractGameActionFightTargetedAbilityMessage import AbstractGameActionFightTargetedAbilityMessage


class GameActionFightSpellCastMessage(AbstractGameActionFightTargetedAbilityMessage):
    spellId:int
    spellLevel:int
    portalsIds:list[int]
    

    def init(self, spellId:int, spellLevel:int, portalsIds:list[int], targetId:int, destinationCellId:int, critical:int, actionId:int, sourceId:int):
        self.spellId = spellId
        self.spellLevel = spellLevel
        self.portalsIds = portalsIds
        
        super().__init__(targetId, destinationCellId, critical, actionId, sourceId)
    
    