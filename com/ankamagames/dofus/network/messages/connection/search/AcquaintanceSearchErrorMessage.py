from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class AcquaintanceSearchErrorMessage(INetworkMessage):
    protocolId = 6994
    reason:int
    
    
