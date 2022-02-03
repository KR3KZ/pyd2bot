from com.ankamagames.dofus.network.messages.game.context.roleplay.CurrentMapMessage import CurrentMapMessage


class CurrentMapInstanceMessage(CurrentMapMessage):
    instantiatedMapId:int
    

    def init(self, instantiatedMapId:int, mapId:int, mapKey:str):
        self.instantiatedMapId = instantiatedMapId
        
        super().__init__(mapId, mapKey)
    
    