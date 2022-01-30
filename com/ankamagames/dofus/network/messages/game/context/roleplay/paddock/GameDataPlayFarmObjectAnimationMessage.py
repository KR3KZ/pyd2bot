from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameDataPlayFarmObjectAnimationMessage(INetworkMessage):
    protocolId = 7212
    cellId:int
    
    
