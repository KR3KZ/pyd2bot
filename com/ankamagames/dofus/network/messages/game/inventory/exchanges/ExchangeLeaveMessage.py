from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.dialog.LeaveDialogMessage import LeaveDialogMessage


@dataclass
class ExchangeLeaveMessage(LeaveDialogMessage):
    success:bool
    
    
    def __post_init__(self):
        super().__init__()
    