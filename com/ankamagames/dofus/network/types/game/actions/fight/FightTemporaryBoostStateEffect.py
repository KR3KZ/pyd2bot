from com.ankamagames.dofus.network.types.game.actions.fight.FightTemporaryBoostEffect import (
    FightTemporaryBoostEffect,
)


class FightTemporaryBoostStateEffect(FightTemporaryBoostEffect):
    stateId: int

    def init(
        self,
        stateId_: int,
        delta_: int,
        uid_: int,
        targetId_: int,
        turnDuration_: int,
        dispelable_: int,
        spellId_: int,
        effectId_: int,
        parentBoostUid_: int,
    ):
        self.stateId = stateId_

        super().__init__(
            delta_,
            uid_,
            targetId_,
            turnDuration_,
            dispelable_,
            spellId_,
            effectId_,
            parentBoostUid_,
        )
