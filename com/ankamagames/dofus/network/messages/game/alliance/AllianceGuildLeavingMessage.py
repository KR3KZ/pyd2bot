from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AllianceGuildLeavingMessage(NetworkMessage):
    kicked:bool
    guildId:int
    
    
