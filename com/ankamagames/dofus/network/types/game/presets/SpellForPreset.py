from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class SpellForPreset(NetworkMessage):
    spellId:int
    shortcuts:list[int]
    

    def init(self, spellId:int, shortcuts:list[int]):
        self.spellId = spellId
        self.shortcuts = shortcuts
        
        super().__init__()
    
    