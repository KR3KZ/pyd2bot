from com.ankamagames.dofus.network.messages.game.social.BulletinMessage import BulletinMessage


class AllianceBulletinMessage(BulletinMessage):
    

    def init(self, lastNotifiedTimestamp:int, content:str, timestamp:int, memberId:int, memberName:str):
        
        super().__init__(lastNotifiedTimestamp, content, timestamp, memberId, memberName)
    
    