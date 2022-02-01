from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.presets.Preset import Preset


class PresetSavedMessage(INetworkMessage):
    protocolId = 4820
    presetId:int
    preset:Preset
    
    
