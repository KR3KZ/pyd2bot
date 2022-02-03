from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeMountsPaddockRemoveMessage(NetworkMessage):
    mountsId:list[int]
    

    def init(self, mountsId:list[int]):
        self.mountsId = mountsId
        
        super().__init__()
    
    