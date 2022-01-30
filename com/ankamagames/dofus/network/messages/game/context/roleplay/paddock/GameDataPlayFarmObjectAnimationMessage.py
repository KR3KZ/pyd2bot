from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameDataPlayFarmObjectAnimationMessage(NetworkMessage):
    protocolId = 7212
    cellId:list[int]
    
