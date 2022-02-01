from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ChatCommunityChannelSetCommunityRequestMessage(INetworkMessage):
    protocolId = 9201
    communityId:int
    
    
