from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.presets.ItemForPreset import ItemForPreset


class ItemForPresetUpdateMessage(NetworkMessage):
    protocolId = 2377
    presetId:int
    presetItem:ItemForPreset
    
    
