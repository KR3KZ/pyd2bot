from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class DebtsDeleteMessage(NetworkMessage):
    reason:int
    debts:list[int]
    
    
