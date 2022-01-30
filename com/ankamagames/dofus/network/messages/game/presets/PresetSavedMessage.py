from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.presets.Preset import Preset


class PresetSavedMessage(NetworkMessage):
    protocolId = 4820
    presetId:int
    preset:Preset
    
    
