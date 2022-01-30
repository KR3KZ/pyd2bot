from com.ankamagames.dofus.network.messages.game.character.choice.CharacterSelectionMessage import CharacterSelectionMessage


class CharacterFirstSelectionMessage(CharacterSelectionMessage):
    protocolId = 3196
    doTutorial:bool
    
    
