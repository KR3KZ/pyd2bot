from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.presets.Preset import Preset


class PresetsMessage(NetworkMessage):
    protocolId = 1706
    presets:Preset
    
