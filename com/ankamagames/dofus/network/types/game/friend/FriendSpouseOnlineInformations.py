from com.ankamagames.dofus.network.types.game.friend.FriendSpouseInformations import FriendSpouseInformations


class FriendSpouseOnlineInformations(FriendSpouseInformations):
    protocolId = 1910
    mapId:int
    subAreaId:int
    inFight:bool
    followSpouse:bool
    
    
