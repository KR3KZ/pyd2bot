from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GuildInformationsGeneralMessage(NetworkMessage):
    protocolId = 8015
    abandonnedPaddock:bool
    level:int
    expLevelFloor:int
    experience:int
    expNextLevelFloor:int
    creationDate:int
    nbTotalMembers:int
    nbConnectedMembers:int
    
    
