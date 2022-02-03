from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightSpellCooldown(NetworkMessage):
    spellId:int
    cooldown:int
    

    def init(self, spellId:int, cooldown:int):
        self.spellId = spellId
        self.cooldown = cooldown
        
        super().__init__()
    
    