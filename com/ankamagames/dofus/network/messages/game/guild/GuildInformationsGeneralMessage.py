from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildInformationsGeneralMessage(NetworkMessage):
    abandonnedPaddock:bool
    level:int
    expLevelFloor:int
    experience:int
    expNextLevelFloor:int
    creationDate:int
    nbTotalMembers:int
    nbConnectedMembers:int
    
    
