from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeMountsStableRemoveMessage(NetworkMessage):
    mountsId:list[int]
    

    def init(self, mountsId:list[int]):
        self.mountsId = mountsId
        
        super().__init__()
    
    