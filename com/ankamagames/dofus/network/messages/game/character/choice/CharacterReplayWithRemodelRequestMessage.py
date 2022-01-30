from com.ankamagames.dofus.network.messages.game.character.replay.CharacterReplayRequestMessage import CharacterReplayRequestMessage
from com.ankamagames.dofus.network.types.game.character.choice.RemodelingInformation import RemodelingInformation


class CharacterReplayWithRemodelRequestMessage(CharacterReplayRequestMessage):
    protocolId = 3832
    remodel:RemodelingInformation
    
