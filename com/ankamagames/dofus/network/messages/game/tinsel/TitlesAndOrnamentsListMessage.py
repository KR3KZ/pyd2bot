from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TitlesAndOrnamentsListMessage(NetworkMessage):
    titles:list[int]
    ornaments:list[int]
    activeTitle:int
    activeOrnament:int
    

    def init(self, titles:list[int], ornaments:list[int], activeTitle:int, activeOrnament:int):
        self.titles = titles
        self.ornaments = ornaments
        self.activeTitle = activeTitle
        self.activeOrnament = activeOrnament
        
        super().__init__()
    
    