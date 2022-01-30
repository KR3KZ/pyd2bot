from com.ankamagames.dofus.network.messages.game.presets.PresetUseResultMessage import PresetUseResultMessage


class PresetUseResultWithMissingIdsMessage(PresetUseResultMessage):
    protocolId = 2217
    missingIds:int
    
