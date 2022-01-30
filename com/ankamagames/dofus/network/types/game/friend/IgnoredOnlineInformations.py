from com.ankamagames.dofus.network.types.game.friend.IgnoredInformations import IgnoredInformations


class IgnoredOnlineInformations(IgnoredInformations):
    protocolId = 7223
    playerId:float
    playerName:str
    breed:int
    sex:bool
    
