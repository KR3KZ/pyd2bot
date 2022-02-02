from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class AllianceVersatileInformations(NetworkMessage):
    allianceId:int
    nbGuilds:int
    nbMembers:int
    nbSubarea:int
    
    
    def __post_init__(self):
        super().__init__()
    