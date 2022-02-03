from com.ankamagames.dofus.network.messages.game.dialog.LeaveDialogMessage import LeaveDialogMessage


class ExchangeLeaveMessage(LeaveDialogMessage):
    success:bool
    

    def init(self, success:bool, dialogType:int):
        self.success = success
        
        super().__init__(dialogType)
    
    