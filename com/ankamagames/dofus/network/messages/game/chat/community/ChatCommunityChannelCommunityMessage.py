from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ChatCommunityChannelCommunityMessage(INetworkMessage):
    protocolId = 9671
    communityId:int
    
    
