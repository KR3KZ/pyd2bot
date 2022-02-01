from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildMemberLeavingMessage(NetworkMessage):
    kicked:bool
    memberId:int
    
    
