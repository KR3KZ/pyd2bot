from com.ankamagames.dofus.network.types.game.actions.fight.AbstractFightDispellableEffect import AbstractFightDispellableEffect


class FightTemporarySpellImmunityEffect(AbstractFightDispellableEffect):
    protocolId = 4141
    immuneSpellId:int
    
    