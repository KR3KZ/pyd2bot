from com.ankamagames.dofus.network.messages.game.actions.fight.AbstractGameActionFightTargetedAbilityMessage import AbstractGameActionFightTargetedAbilityMessage


class GameActionFightSpellCastMessage(AbstractGameActionFightTargetedAbilityMessage):
    protocolId = 2648
    spellId:int
    spellLevel:int
    portalsIds:int
    
