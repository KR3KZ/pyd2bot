from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ChatCommunityChannelSetCommunityRequestMessage(NetworkMessage):
    protocolId = 9201
    communityId:int
    
    
