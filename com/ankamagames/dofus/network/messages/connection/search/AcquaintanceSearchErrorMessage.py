from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class AcquaintanceSearchErrorMessage(INetworkMessage):
    protocolId = 6994
    reason:int
    
    
