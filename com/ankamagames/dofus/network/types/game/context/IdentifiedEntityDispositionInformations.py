from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations


class IdentifiedEntityDispositionInformations(EntityDispositionInformations):
    id:int
    

    def init(self, id:int, cellId:int, direction:int):
        self.id = id
        
        super().__init__(cellId, direction)
    
    