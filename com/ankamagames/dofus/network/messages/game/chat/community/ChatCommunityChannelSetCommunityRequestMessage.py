from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ChatCommunityChannelSetCommunityRequestMessage(INetworkMessage):
    protocolId = 9201
    communityId:int
    
    
