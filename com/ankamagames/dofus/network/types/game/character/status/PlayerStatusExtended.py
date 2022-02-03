from com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus


class PlayerStatusExtended(PlayerStatus):
    message:str
    

    def init(self, message:str, statusId:int):
        self.message = message
        
        super().__init__(statusId)
    
    