from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect


class ObjectEffectDice(ObjectEffect):
    protocolId = 1048
    diceNum:int
    diceSide:int
    diceConst:int
    
    
