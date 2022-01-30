from com.ankamagames.dofus.network.types.game.presets.Preset import Preset


class IdolsPreset(Preset):
    protocolId = 6343
    iconId:int
    idolIds:list[int]
    
