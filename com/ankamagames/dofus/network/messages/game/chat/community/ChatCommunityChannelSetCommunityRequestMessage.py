from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ChatCommunityChannelSetCommunityRequestMessage(NetworkMessage):
    communityId:int
    

    def init(self, communityId:int):
        self.communityId = communityId
        
        super().__init__()
    
    