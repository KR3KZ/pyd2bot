from com.ankamagames.dofus.network.messages.game.interactive.InteractiveUseRequestMessage import InteractiveUseRequestMessage


class InteractiveUseWithParamRequestMessage(InteractiveUseRequestMessage):
    id:int
    

    def init(self, id:int, elemId:int, skillInstanceUid:int):
        self.id = id
        
        super().__init__(elemId, skillInstanceUid)
    
    