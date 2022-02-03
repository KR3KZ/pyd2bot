from com.ankamagames.dofus.network.types.game.approach.ServerSessionConstant import ServerSessionConstant


class ServerSessionConstantString(ServerSessionConstant):
    value:str
    

    def init(self, value:str, id:int):
        self.value = value
        
        super().__init__(id)
    
    