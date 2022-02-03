from com.ankamagames.dofus.network.messages.game.character.choice.CharacterSelectionMessage import CharacterSelectionMessage


class CharacterFirstSelectionMessage(CharacterSelectionMessage):
    doTutorial:bool
    

    def init(self, doTutorial:bool, id:int):
        self.doTutorial = doTutorial
        
        super().__init__(id)
    
    