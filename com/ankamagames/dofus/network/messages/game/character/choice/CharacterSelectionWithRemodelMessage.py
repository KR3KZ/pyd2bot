from com.ankamagames.dofus.network.messages.game.character.choice.CharacterSelectionMessage import CharacterSelectionMessage
from com.ankamagames.dofus.network.types.game.character.choice.RemodelingInformation import RemodelingInformation


class CharacterSelectionWithRemodelMessage(CharacterSelectionMessage):
    protocolId = 2652
    remodel:RemodelingInformation
    
    
