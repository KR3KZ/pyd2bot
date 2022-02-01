from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.presets.ItemForPreset import ItemForPreset


class ItemForPresetUpdateMessage(NetworkMessage):
    presetId:int
    presetItem:ItemForPreset
    
    
