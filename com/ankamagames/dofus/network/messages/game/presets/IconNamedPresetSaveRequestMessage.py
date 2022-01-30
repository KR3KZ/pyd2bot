from com.ankamagames.dofus.network.messages.game.presets.IconPresetSaveRequestMessage import IconPresetSaveRequestMessage


class IconNamedPresetSaveRequestMessage(IconPresetSaveRequestMessage):
    protocolId = 8129
    name:str
    type:int
    
    
