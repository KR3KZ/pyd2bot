from pyd2bot.logic import IFrame


class GameStartingFrame(IFrame):

    def process(self, msg):
        mtype = msg["__type__"]

        if self._done:
            return False

        if mtype == "CharacterLoadingCompleteMessage":
            self.bot.inGame.set()
            self.conn.send({'__type__': 'GameContextCreateRequestMessage'})
            self.done = True
            return True
        
        return False
        
