from com.ankamagames.dofus.network.types.game.context.roleplay.HumanOption import HumanOption


class HumanOptionTitle(HumanOption):
    titleId:int
    titleParam:str
    

    def init(self, titleId:int, titleParam:str):
        self.titleId = titleId
        self.titleParam = titleParam
        
        super().__init__()
    
    