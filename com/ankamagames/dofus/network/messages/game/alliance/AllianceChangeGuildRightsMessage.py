from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AllianceChangeGuildRightsMessage(NetworkMessage):
    guildId:int
    rights:int
    
    
