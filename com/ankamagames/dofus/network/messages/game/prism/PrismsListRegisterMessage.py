from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class PrismsListRegisterMessage(NetworkMessage):
    protocolId = 4105
    listen:int
    
