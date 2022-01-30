from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class AllianceVersatileInformations(INetworkMessage):
    protocolId = 1207
    allianceId:int
    nbGuilds:int
    nbMembers:int
    nbSubarea:int
    
    
