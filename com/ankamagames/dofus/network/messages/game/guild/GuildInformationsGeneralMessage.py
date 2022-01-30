from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GuildInformationsGeneralMessage(NetworkMessage):
    protocolId = 8015
    abandonnedPaddock:bool
    level:int
    expLevelFloor:float
    experience:float
    expNextLevelFloor:float
    creationDate:int
    nbTotalMembers:int
    nbConnectedMembers:int
    
