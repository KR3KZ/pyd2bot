from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.actions.fight.AbstractGameActionFightTargetedAbilityMessage import AbstractGameActionFightTargetedAbilityMessage


@dataclass
class GameActionFightCloseCombatMessage(AbstractGameActionFightTargetedAbilityMessage):
    weaponGenericId:int
    
    
    def __post_init__(self):
        super().__init__()
    