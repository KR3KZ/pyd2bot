from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class PrismFightAttackerRemoveMessage(NetworkMessage):
    protocolId = 300
    subAreaId:int
    fightId:int
    fighterToRemoveId:float
    
