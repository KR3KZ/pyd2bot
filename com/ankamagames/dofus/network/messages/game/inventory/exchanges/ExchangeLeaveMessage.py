from com.ankamagames.dofus.network.messages.game.dialog.LeaveDialogMessage import LeaveDialogMessage


class ExchangeLeaveMessage(LeaveDialogMessage):
    protocolId = 8813
    success:bool
    
