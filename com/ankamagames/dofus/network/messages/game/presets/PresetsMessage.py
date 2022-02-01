from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.presets.Preset import Preset


class PresetsMessage(INetworkMessage):
    protocolId = 1706
    presets:Preset
    
    
