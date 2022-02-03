from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MountEmoteIconUsedOkMessage(NetworkMessage):
    mountId:int
    reactionType:int
    

    def init(self, mountId:int, reactionType:int):
        self.mountId = mountId
        self.reactionType = reactionType
        
        super().__init__()
    
    