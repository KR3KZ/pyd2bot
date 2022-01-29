from threading import Event
from com.ankamagames.jerakine.metaclasses.singleton import Singleton
from com.ankamagames.jerakine.utils.displays.EnterFrameConst import EnterFrameConst
from com.ankamagames.jerakine.utils.displays.EnterFrameDispatcher import EnterFrameDispatcher


class FrameIdManager(metaclass=Singleton):
    
    
    def __init__(self):
        self._init:bool = False
        self._frameId:int = 0
        EnterFrameDispatcher().addEventListener(self.onEnterFrame, EnterFrameConst.FRAME_ID_MANAGER)
    
    @property
    def frameId(self) -> int:
        return self._frameId
    
    def onEnterFrame(self, e:Event) -> None:
        self._frameId += 1
