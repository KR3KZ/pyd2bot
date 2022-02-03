from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations


class FightEntityDispositionInformations(EntityDispositionInformations):
    carryingCharacterId:int
    

    def init(self, carryingCharacterId:int, cellId:int, direction:int):
        self.carryingCharacterId = carryingCharacterId
        
        super().__init__(cellId, direction)
    
    