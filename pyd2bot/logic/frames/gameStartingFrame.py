from pyd2bot.logic.frames import IFrame


class GameStartingFrame(IFrame):

    def process(self, mtype, msg):

        if mtype == "CharacterLoadingCompleteMessage":
            self.bot.inGame.set()
            self.conn.send({'__type__': 'GameContextCreateRequestMessage'})
            self.done = True
            return True

        elif mtype == "GameContextRemoveElementMessage":
            self.bot.contextChanged.set()

        elif mtype == "GameContextCreateMessage":
            if msg['context'] == 2:
                self.bot.inGame.clear()
                self.bot.isInFight.set()
                
            elif msg['context'] == 1:
                self.bot.isInFight.clear()
                self.bot.inGame.set()

        return False
        
