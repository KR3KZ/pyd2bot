from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class DebtsDeleteMessage(NetworkMessage):
    protocolId = 5619
    reason:int
    debts:int
    
