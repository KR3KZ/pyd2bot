from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.presets.Preset import Preset


class PresetsMessage(INetworkMessage):
    protocolId = 1706
    presets:Preset
    
    
