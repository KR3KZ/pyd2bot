from com.ankamagames.dofus.network.types.game.character.debt.DebtInformation import DebtInformation


class KamaDebtInformation(DebtInformation):
    kamas:int
    

    def init(self, kamas:int, id:int, timestamp:int):
        self.kamas = kamas
        
        super().__init__(id, timestamp)
    
    