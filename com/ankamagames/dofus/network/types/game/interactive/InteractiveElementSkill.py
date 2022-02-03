from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class InteractiveElementSkill(NetworkMessage):
    skillId:int
    skillInstanceUid:int
    

    def init(self, skillId:int, skillInstanceUid:int):
        self.skillId = skillId
        self.skillInstanceUid = skillInstanceUid
        
        super().__init__()
    
    