from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect


class SetUpdateMessage(NetworkMessage):
    protocolId = 2982
    setId:int
    setObjects:list[int]
    setEffects:list[ObjectEffect]
    
