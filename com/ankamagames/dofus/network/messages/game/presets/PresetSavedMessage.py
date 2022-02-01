from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.presets.Preset import Preset


class PresetSavedMessage(NetworkMessage):
    presetId:int
    preset:Preset
    
    
