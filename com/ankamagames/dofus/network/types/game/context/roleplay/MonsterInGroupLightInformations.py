from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MonsterInGroupLightInformations(NetworkMessage):
    genericId:int
    grade:int
    level:int
    

    def init(self, genericId:int, grade:int, level:int):
        self.genericId = genericId
        self.grade = grade
        self.level = level
        
        super().__init__()
    
    