from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class AllianceInvitationMessage(INetworkMessage):
    protocolId = 235
    targetId:int
    
    
