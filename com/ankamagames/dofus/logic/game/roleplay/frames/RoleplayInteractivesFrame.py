from com.ankamagames.atouin.Atouin import Atouin
from com.ankamagames.atouin.managers.AlwaysAnimatedElementManager import (
    AlwaysAnimatedElementManager,
)
from com.ankamagames.atouin.managers.InteractiveCellManager import (
    InteractiveCellManager,
)
from com.ankamagames.atouin.managers.MapDisplayManager import MapDisplayManager
from com.ankamagames.berilia.factories.MenusFactory import MenusFactory
from com.ankamagames.berilia.frames.ShortcutsFrame import ShortcutsFrame
from com.ankamagames.berilia.managers.KernelEventsManager import KernelEventsManager
from com.ankamagames.berilia.managers.TooltipManager import TooltipManager
from com.ankamagames.berilia.managers.UiModuleManager import UiModuleManager
from com.ankamagames.dofus.datacenter.interactives.Interactive import Interactive
from com.ankamagames.dofus.datacenter.jobs.Skill import Skill
from com.ankamagames.dofus.kernel.Kernel import Kernel
from com.ankamagames.dofus.logic.common.actions.ChangeWorldInteractionAction import (
    ChangeWorldInteractionAction,
)
from com.ankamagames.dofus.logic.game.common.frames.ChatFrame import ChatFrame
from com.ankamagames.dofus.logic.game.common.managers.PlayedCharacterManager import (
    PlayedCharacterManager,
)
from com.ankamagames.dofus.logic.game.common.misc.DofusEntities import DofusEntities
from com.ankamagames.dofus.logic.game.roleplay.actions.HighlightInteractiveElementsAction import (
    HighlightInteractiveElementsAction,
)
from com.ankamagames.dofus.logic.game.roleplay.frames.RoleplayEntitiesFrame import (
    RoleplayEntitiesFrame,
)
from com.ankamagames.dofus.logic.game.roleplay.managers.SkillManager import SkillManager
from com.ankamagames.dofus.logic.game.roleplay.messages.InteractiveElementActivationMessage import (
    InteractiveElementActivationMessage,
)
from com.ankamagames.dofus.logic.game.roleplay.messages.InteractiveElementMouseOutMessage import (
    InteractiveElementMouseOutMessage,
)
from com.ankamagames.dofus.logic.game.roleplay.messages.InteractiveElementMouseOverMessage import (
    InteractiveElementMouseOverMessage,
)
from com.ankamagames.dofus.misc.lists.ChatHookList import ChatHookList
from com.ankamagames.dofus.misc.lists.HookList import HookList
from com.ankamagames.dofus.network.enums.MapObstacleStateEnum import (
    MapObstacleStateEnum,
)
from com.ankamagames.dofus.network.enums.PlayerLifeStatusEnum import (
    PlayerLifeStatusEnum,
)
from com.ankamagames.dofus.network.messages.game.context.GameContextDestroyMessage import (
    GameContextDestroyMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.MapObstacleUpdateMessage import (
    MapObstacleUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.interactive.InteractiveElementUpdatedMessage import (
    InteractiveElementUpdatedMessage,
)
from com.ankamagames.dofus.network.messages.game.interactive.InteractiveMapUpdateMessage import (
    InteractiveMapUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.interactive.InteractiveUseEndedMessage import (
    InteractiveUseEndedMessage,
)
from com.ankamagames.dofus.network.messages.game.interactive.InteractiveUseErrorMessage import (
    InteractiveUseErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.interactive.InteractiveUsedMessage import (
    InteractiveUsedMessage,
)
from com.ankamagames.dofus.network.messages.game.interactive.StatedElementUpdatedMessage import (
    StatedElementUpdatedMessage,
)
from com.ankamagames.dofus.network.messages.game.interactive.StatedMapUpdateMessage import (
    StatedMapUpdateMessage,
)
from com.ankamagames.dofus.network.types.game.interactive.InteractiveElement import (
    InteractiveElement,
)
from com.ankamagames.dofus.network.types.game.interactive.InteractiveElementSkill import (
    InteractiveElementSkill,
)
from com.ankamagames.dofus.network.types.game.interactive.MapObstacle import MapObstacle
from com.ankamagames.dofus.network.types.game.interactive.StatedElement import (
    StatedElement,
)
from com.ankamagames.dofus.types.entities.AnimatedCharacter import AnimatedCharacter
from com.ankamagames.dofus.uiApi.JobsApi import JobsApi
from com.ankamagames.jerakine.benchmark.BenchmarkTimer import BenchmarkTimer
from com.ankamagames.jerakine.data.I18n import I18n
from com.ankamagames.jerakine.entities.interfaces.IEntity import IEntity
from com.ankamagames.jerakine.enum.OperatingSystem import OperatingSystem
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.managers.FiltersManager import FiltersManager
from com.ankamagames.jerakine.managers.OptionManager import OptionManager
from com.ankamagames.jerakine.messages.Frame import Frame
from com.ankamagames.jerakine.messages.Message import Message
from com.ankamagames.jerakine.types.enums.Priority import Priority
from com.ankamagames.jerakine.types.positions.MapPoint import MapPoint
from com.ankamagames.jerakine.utils.system.SystemManager import SystemManager

logger = Logger(__name__)


class RoleplayInteractivesFrame(Frame):

    INTERACTIVE_CURSOR_DISABLED_INDEX: int = 999

    INTERACTIVE_CURSOR_WAIT_INDEX: int = 1000

    cursorList: list = list()

    cursorClassList: list

    INTERACTIVE_CURSOR_NAME: str = "interactiveCursor"

    LUMINOSITY_FACTOR: float = 1.2

    ALPHA_MODIFICATOR: float = 0.2

    COLLECTABLE_COLLECTING_STATE_ID: int = 2

    COLLECTABLE_CUT_STATE_ID: int = 1

    ACTION_COLLECTABLE_RESOURCES: int = 1

    _highlightInteractiveElements: bool
    _modContextMenu: object

    _ie: dict

    _currentUsages: list

    _baseAlpha: float

    i: int

    _entities: dict

    _usingInteractive: bool = False

    _nextInteractiveUsed: object

    _interactiveActionTimers: dict

    _enableWorldInteraction: bool = True

    _collectableSpritesToBeStopped: dict

    _currentRequestedElementId: int = -1

    _currentUsedElementId: int = -1

    _statedElementsTargetAnimation: dict

    _mouseDown: bool

    dirmov: int = 666

    def __init__(self):
        self._ie = dict(True)
        self._currentUsages = list()
        self._entities = dict()
        self._interactiveActionTimers = dict(True)
        self._collectableSpritesToBeStopped = dict(True)
        self._statedElementsTargetAnimation = dict(True)
        super().__init__()
        self._modContextMenu = (
            UiModuleManager().getModule("Ankama_ContextMenu").mainClass
        )

    @property
    def priority(self) -> int:
        return Priority.HIGH

    @property
    def roleplayContextFrame(self) -> RoleplayContextFrame:
        return Kernel.getWorker().getFrame(RoleplayContextFrame)

    @property
    def roleplayWorldFrame(self) -> RoleplayWorldFrame:
        return Kernel.getWorker().getFrame(RoleplayWorldFrame)

    @property
    def currentRequestedElementId(self) -> int:
        return self._currentRequestedElementId

    @currentRequestedElementId.setter
    def currentRequestedElementId(self, pElementId: int) -> None:
        self._currentRequestedElementId = pElementId

    @property
    def usingInteractive(self) -> bool:
        return self._usingInteractive

    @property
    def nextInteractiveUsed(self) -> object:
        return self._nextInteractiveUsed

    @nextInteractiveUsed.setter
    def nextInteractiveUsed(self, object: object) -> None:
        self._nextInteractiveUsed = object

    @property
    def worldInteractionIsEnable(self) -> bool:
        return self._enableWorldInteraction

    def pushed(self) -> bool:
        return True

    def process(self, msg: Message) -> bool:
        skills: list[InteractiveElementSkill] = None
        if isinstance(msg, InteractiveMapUpdateMessage):
            imumsg = msg
            self.clear()
            for ie in imumsg.interactiveElements:
                if len(ie.enabledSkills):
                    self.registerInteractive(ie, ie.enabledSkills[0].skillId)
                elif len(ie.disabledSkills):
                    self.registerInteractive(ie, ie.disabledSkills[0].skillId)
            return True

        if isinstance(msg, InteractiveElementUpdatedMessage):
            ieumsg = msg
            if len(ieumsg.interactiveElement.enabledSkills):
                self.registerInteractive(
                    ieumsg.interactiveElement,
                    ieumsg.interactiveElement.enabledSkills[0].skillId,
                )
            elif len(ieumsg.interactiveElement.disabledSkills):
                self.registerInteractive(
                    ieumsg.interactiveElement,
                    ieumsg.interactiveElement.disabledSkills[0].skillId,
                )
            else:
                self.removeInteractive(ieumsg.interactiveElement)
            return True

        if isinstance(msg, InteractiveUsedMessage):
            iumsg = msg
            if PlayedCharacterManager().id == iumsg.entityId and iumsg.duration > 0:
                self._currentUsedElementId = iumsg.elemId
            if self._currentRequestedElementId == iumsg.elemId:
                self._currentRequestedElementId = -1
            if iumsg.duration > 0:
                if PlayedCharacterManager().id == iumsg.entityId:
                    self._usingInteractive = True
                    rwf = self.roleplayWorldFrame
                    if rwf:
                        rwf.cellClickEnabled = False
                self._entities[iumsg.elemId] = iumsg.entityId
            return False

        if isinstance(msg, InteractiveUseErrorMessage):
            iuem = msg
            if iuem.elemId == self._currentRequestedElementId:
                self._currentRequestedElementId = -1
                # TODO: Send error message to player
            return False

        if isinstance(msg, StatedMapUpdateMessage):
            smumsg = msg
            self._usingInteractive = False
            for se in smumsg.statedElements:
                self.updateStatedElement(se, True)
            return True

        if isinstance(msg, StatedElementUpdatedMessage):
            seumsg = msg
            self.updateStatedElement(seumsg.statedElement)
            return True

        if isinstance(msg, MapObstacleUpdateMessage):
            moumsg = msg
            for mo in moumsg.obstacles:
                InteractiveCellManager().updateCell(
                    mo.obstacleCellId, mo.state == MapObstacleStateEnum.OBSTACLE_OPENED
                )
            return True

        if isinstance(msg, InteractiveUseEndedMessage):
            iuemsg = InteractiveUseEndedMessage(msg)
            self.interactiveUsageFinished(
                self._entities[iuemsg.elemId], iuemsg.elemId, iuemsg.skillId
            )
            del self._entities[iuemsg.elemId]
            return False

        if isinstance(msg, GameContextDestroyMessage):
            return False

        return False

    def pulled(self) -> bool:
        self._entities = dict()
        self._ie = dict(True)
        self._modContextMenu = None
        self._currentUsages = list()
        self._nextInteractiveUsed = None
        self._interactiveActionTimers = dict(True)
        return True

    def enableWorldInteraction(self, pEnable: bool) -> None:
        self._enableWorldInteraction = pEnable

    def clear(self) -> None:
        timeout: int = 0
        ieObj = None
        for timeout in self._currentUsages:
            clearTimeout(timeout)
        for ieObj in self._ie:
            self.removeInteractive(self._ie[ieObj].element)

    def getInteractiveElementsCells(self) -> list[int]:
        cells: list[int] = list[int]()
        for cellObj in self._ie:
            if cellObj is not None:
                cells.append(cellObj.position.cellId)
        return cells

    def getInteractiveActionTimer(self, pUser) -> BenchmarkTimer:
        return self._interactiveActionTimers[pUser]

    def isElementChangingState(self, pElementId: int) -> bool:
        changing: bool = False
        for animData in self._statedElementsTargetAnimation:
            if animData.elemId == pElementId:
                changing = True
        return changing

    def enableInteractiveElements(self, enabled: bool) -> None:
        worldObject = None
        for worldObject in self._ie:
            worldObject.mouseEnabled = enabled
            worldObject.useHandCursor = enabled
            worldObject.buttonMode = enabled

    def getInteractiveElement(self, pObject: DisplayObject) -> InteractiveElement:
        return self._ie.get(pObject)

    def registerInteractive(self, ie: InteractiveElement, firstSkill: int) -> None:
        worldObject: InteractiveObject = Atouin().getIdentifiedElement(ie.elementId)
        if not worldObject:
            logger.error(
                "Unknown identified element "
                + str(ie.elementId)
                + ", unable to register it as interactive."
            )
            return
        entitiesFrame: RoleplayEntitiesFrame = (
            Kernel().getWorker().getFrame(RoleplayEntitiesFrame)
        )
        if entitiesFrame:
            found = False
            for s, cie in enumerate(entitiesFrame.interactiveElements):
                if cie.elementId == ie.elementId:
                    found = True
                    entitiesFrame.interactiveElements[int(s)] = ie
            if not found:
                entitiesFrame.interactiveElements.append(ie)
        worldPos: MapPoint = Atouin().getIdentifiedElementPosition(ie.elementId)
        self._ie[worldObject] = {
            "element": ie,
            "position": worldPos,
            "firstSkill": firstSkill,
        }

    def removeInteractive(self, ie: InteractiveElement) -> None:
        interactiveElement: InteractiveObject = Atouin().getIdentifiedElement(
            ie.elementId
        )
        del self._ie[interactiveElement]

    def updateStatedElement(self, se: StatedElement, globalv: bool = False) -> None:
        worldObject: InteractiveObject = Atouin().getIdentifiedElement(se.elementId)
        if not worldObject:
            logger.error(
                "Unknown identified element "
                + str(se.elementId)
                + " unable to change its state to "
                + str(se.elementState)
                + " !"
            )
            return
        if se.elementId == self._currentUsedElementId:
            self._usingInteractive = True
        if (
            self._ie.get(worldObject)
            and self._ie[worldObject].element
            and self._ie[worldObject].element.elementId == se.elementId
        ):
            interactive = Interactive.getInteractiveById(
                self._ie[worldObject].element.elementTypeId
            )
            if interactive:
                isCollectable = False
                for interactiveSkill in self._ie[worldObject].element.enabledSkills:
                    skill = Skill.getSkillById(interactiveSkill.skillId)
                    if skill.elementActionId == self.ACTION_COLLECTABLE_RESOURCES:
                        isCollectable = True
                if not isCollectable:
                    for interactiveSkill in self._ie[
                        worldObject
                    ].element.disabledSkills:
                        skill = Skill.getSkillById(interactiveSkill.skillId)
                        if skill.elementActionId == self.ACTION_COLLECTABLE_RESOURCES:
                            isCollectable = True

    def skillClicked(self, ie: object, skillInstanceId: int) -> None:
        msg: InteractiveElementActivationMessage = InteractiveElementActivationMessage(
            ie.element, ie.position, skillInstanceId
        )
        Kernel.getWorker().process(msg)

    def interactiveUsageFinished(
        self, entityId: float, elementId: int, skillId: int
    ) -> None:
        if entityId == PlayedCharacterManager().id:
            Kernel.getWorker().process(ChangeWorldInteractionAction.create(True))
            if self.roleplayWorldFrame:
                self.roleplayWorldFrame.cellClickEnabled = True
            self._usingInteractive = False
            self._currentUsedElementId = -1
            if self._nextInteractiveUsed:
                ieamsg = InteractiveElementActivationMessage(
                    self._nextInteractiveUsed.ie,
                    self._nextInteractiveUsed.position,
                    self._nextInteractiveUsed.skillInstanceId,
                )
                self._nextInteractiveUsed = None
                Kernel().getWorker().process(ieamsg)
