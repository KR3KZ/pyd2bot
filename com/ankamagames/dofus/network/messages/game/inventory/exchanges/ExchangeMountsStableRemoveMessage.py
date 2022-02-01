from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeMountsStableRemoveMessage(NetworkMessage):
    mountsId:list[int]
    
    
