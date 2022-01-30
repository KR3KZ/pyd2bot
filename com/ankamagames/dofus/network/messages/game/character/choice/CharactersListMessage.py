from com.ankamagames.dofus.network.messages.game.character.choice.BasicCharactersListMessage import BasicCharactersListMessage


class CharactersListMessage(BasicCharactersListMessage):
    protocolId = 269
    hasStartupActions:bool
    
    
