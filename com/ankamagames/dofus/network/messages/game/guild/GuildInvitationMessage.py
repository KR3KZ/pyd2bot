from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GuildInvitationMessage(INetworkMessage):
    protocolId = 2715
    targetId:int
    
    
