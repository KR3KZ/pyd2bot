from com.ankamagames.dofus.logic.game.roleplay.frames.RoleplayEntitiesFrame import (
    RoleplayEntitiesFrame,
)
from com.ankamagames.dofus.logic.game.roleplay.frames.RoleplayMovementFrame import (
    RoleplayMovementFrame,
)
from com.ankamagames.dofus.network.types.game.interactive.InteractiveElement import (
    InteractiveElement,
)
from com.ankamagames.dofus.network.types.game.interactive.InteractiveElementSkill import (
    InteractiveElementSkill,
)
from com.ankamagames.dofus.network.types.game.interactive.StatedElement import (
    StatedElement,
)
import com.ankamagames.dofus.kernel.Kernel as krnl
from com.ankamagames.jerakine.logger.Logger import Logger

logger = Logger(__name__)


class farmAPI:
    def canCollect(
        self, ie: InteractiveElement, se: StatedElement = None
    ) -> InteractiveElementSkill:
        logger.debug(f"Checking if elem {ie.elementId} can be collected")
        if se is not None and (
            ie.onCurrentMap and se.elementState == 0 and ie.enabledSkills
        ):
            return ie.enabledSkills[0]
        return None

    def collectElement(self, elementId, skill):
        roleplayEntitiesFrame: RoleplayEntitiesFrame = (
            krnl.Kernel().getWorker().getFrame(RoleplayEntitiesFrame)
        )
        selem = roleplayEntitiesFrame.currMapStatedElems[elementId]
        cellId = selem["elementCellId"]
        cellNode = self.cpf.getNodeFromId(cellId)
        neighbors = self.cpf.getAccessibleNeighbours(cellNode)
        for ncid in neighbors:
            if self.walkToCell(ncid):
                hash = bytes(random.getrandbits(8) for _ in range(48))
                self.conn.send(
                    {
                        "__type__": "InteractiveUseRequestMessage",
                        "elemId": elementId,
                        "hash_function": hash,
                        "skillInstanceUid": skill["skillInstanceUid"],
                    }
                )
                if self.conn.waitMsg("InteractiveUsedMessage"):
                    logger.info(f"Collecting elem {elementId} ...")
                    if self.conn.waitMsg("InteractiveUseEndedMessage"):
                        logger.info(f"Element {elementId} collected")
                        break
                if self._kill.is_set():
                    return

    def harvest(self):
        roleplayEntitiesFrame: RoleplayEntitiesFrame = (
            krnl.Kernel().getWorker().getFrame(RoleplayEntitiesFrame)
        )
        logger.info("Looking for collectable resources")
        for ie in roleplayEntitiesFrame.interactiveElements:
            enabledSkill = self.canCollect(ie)
            if enabledSkill is not None:
                self.collectElement(id, enabledSkill)
                if self._kill.is_set():
                    return
