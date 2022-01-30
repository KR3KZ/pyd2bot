from com.ankamagames.dofus.network.messages.game.actions.fight.AbstractGameActionFightTargetedAbilityMessage import AbstractGameActionFightTargetedAbilityMessage


class GameActionFightCloseCombatMessage(AbstractGameActionFightTargetedAbilityMessage):
    protocolId = 9973
    weaponGenericId:int
    
    
