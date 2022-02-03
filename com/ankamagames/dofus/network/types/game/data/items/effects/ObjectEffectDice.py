from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect


class ObjectEffectDice(ObjectEffect):
    diceNum:int
    diceSide:int
    diceConst:int
    

    def init(self, diceNum:int, diceSide:int, diceConst:int, actionId:int):
        self.diceNum = diceNum
        self.diceSide = diceSide
        self.diceConst = diceConst
        
        super().__init__(actionId)
    
    