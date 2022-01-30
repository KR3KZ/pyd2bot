from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeMountsStableRemoveMessage(NetworkMessage):
    protocolId = 9668
    mountsId:list[int]
    
