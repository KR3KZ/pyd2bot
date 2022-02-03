from com.ankamagames.dofus.network.types.game.approach.ServerSessionConstant import ServerSessionConstant


class ServerSessionConstantLong(ServerSessionConstant):
    value:int
    

    def init(self, value:int, id:int):
        self.value = value
        
        super().__init__(id)
    
    