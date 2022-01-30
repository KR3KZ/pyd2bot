from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class AcquaintanceSearchErrorMessage(NetworkMessage):
    protocolId = 6994
    reason:int
    
