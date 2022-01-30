from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class AllianceVersatileInformations(NetworkMessage):
    protocolId = 1207
    allianceId:int
    nbGuilds:int
    nbMembers:int
    nbSubarea:int
    
    
