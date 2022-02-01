from com.ankamagames.dofus.network.messages.game.presets.PresetUseResultMessage import PresetUseResultMessage


class PresetUseResultWithMissingIdsMessage(PresetUseResultMessage):
    missingIds:list[int]
    
    
