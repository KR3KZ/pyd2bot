from com.ankamagames.dofus.network.types.game.interactive.InteractiveElementSkill import InteractiveElementSkill


class InteractiveElementNamedSkill(InteractiveElementSkill):
    nameId:int
    

    def init(self, nameId:int, skillId:int, skillInstanceUid:int):
        self.nameId = nameId
        
        super().__init__(skillId, skillInstanceUid)
    
    