from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GuildInformationsGeneralMessage(INetworkMessage):
    protocolId = 8015
    abandonnedPaddock:bool
    level:int
    expLevelFloor:int
    experience:int
    expNextLevelFloor:int
    creationDate:int
    nbTotalMembers:int
    nbConnectedMembers:int
    
    
