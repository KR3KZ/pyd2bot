from com.ankamagames.dofus.network.types.game.context.roleplay.HumanOption import HumanOption


class HumanOptionOrnament(HumanOption):
    ornamentId:int
    level:int
    leagueId:int
    ladderPosition:int
    

    def init(self, ornamentId:int, level:int, leagueId:int, ladderPosition:int):
        self.ornamentId = ornamentId
        self.level = level
        self.leagueId = leagueId
        self.ladderPosition = ladderPosition
        
        super().__init__()
    
    