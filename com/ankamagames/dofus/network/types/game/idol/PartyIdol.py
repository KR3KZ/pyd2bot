from com.ankamagames.dofus.network.types.game.idol.Idol import Idol


class PartyIdol(Idol):
    ownersIds:list[int]
    

    def init(self, ownersIds:list[int], id:int, xpBonusPercent:int, dropBonusPercent:int):
        self.ownersIds = ownersIds
        
        super().__init__(id, xpBonusPercent, dropBonusPercent)
    
    