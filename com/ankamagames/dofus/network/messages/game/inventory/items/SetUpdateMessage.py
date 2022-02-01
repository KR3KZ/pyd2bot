from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect


class SetUpdateMessage(INetworkMessage):
    protocolId = 2982
    setId:int
    setObjects:int
    setEffects:ObjectEffect
    
    
