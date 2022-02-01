from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.presets.ItemForPreset import ItemForPreset


class ItemForPresetUpdateMessage(INetworkMessage):
    protocolId = 2377
    presetId:int
    presetItem:ItemForPreset
    
    
