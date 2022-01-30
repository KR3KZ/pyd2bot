from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ChatCommunityChannelCommunityMessage(NetworkMessage):
    protocolId = 9671
    communityId:int
    
