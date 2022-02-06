
from com.ankamagames.atouin.messages.EntityMovementCompleteMessage import EntityMovementCompleteMessage
from com.ankamagames.atouin.messages.EntityMovementStoppedMessage import EntityMovementStoppedMessage
from com.ankamagames.atouin.utils.DataMapProvider import DataMapProvider
from com.ankamagames.dofus.kernel.Kernel import Kernel
from com.ankamagames.dofus.kernel.net.ConnectionsHandler import ConnectionsHandler
from com.ankamagames.dofus.logic.game.common.managers.MapMovementAdapter import MapMovementAdapter
from com.ankamagames.dofus.logic.game.common.managers.PlayedCharacterManager import PlayedCharacterManager
from com.ankamagames.dofus.logic.game.common.misc.DofusEntities import DofusEntities
from com.ankamagames.dofus.network.enums.PlayerLifeStatusEnum import PlayerLifeStatusEnum
from com.ankamagames.dofus.network.messages.game.context.GameCautiousMapMovementMessage import GameCautiousMapMovementMessage
from com.ankamagames.dofus.network.messages.game.context.GameCautiousMapMovementRequestMessage import GameCautiousMapMovementRequestMessage
from com.ankamagames.dofus.network.messages.game.context.GameMapMovementCancelMessage import GameMapMovementCancelMessage
from com.ankamagames.dofus.network.messages.game.context.GameMapMovementConfirmMessage import GameMapMovementConfirmMessage
from com.ankamagames.dofus.network.messages.game.context.GameMapMovementMessage import GameMapMovementMessage
from com.ankamagames.dofus.network.messages.game.context.GameMapMovementRequestMessage import GameMapMovementRequestMessage
from com.ankamagames.dofus.network.messages.game.context.GameMapNoMovementMessage import GameMapNoMovementMessage
from com.ankamagames.dofus.network.messages.game.context.roleplay.ChangeMapMessage import ChangeMapMessage
from com.ankamagames.dofus.network.messages.game.context.roleplay.MapComplementaryInformationsDataMessage import MapComplementaryInformationsDataMessage
from com.ankamagames.dofus.network.messages.game.context.roleplay.TeleportOnSameMapMessage import TeleportOnSameMapMessage
from com.ankamagames.dofus.network.messages.game.context.roleplay.delay.GameRolePlayDelayedActionFinishedMessage import GameRolePlayDelayedActionFinishedMessage
from com.ankamagames.dofus.network.messages.game.context.roleplay.fight.GameRolePlayAttackMonsterRequestMessage import GameRolePlayAttackMonsterRequestMessage
from com.ankamagames.dofus.network.messages.game.context.roleplay.fight.GameRolePlayFightRequestCanceledMessage import GameRolePlayFightRequestCanceledMessage
from com.ankamagames.dofus.network.messages.game.context.roleplay.havenbag.EditHavenBagFinishedMessage import EditHavenBagFinishedMessage
from com.ankamagames.dofus.network.messages.game.dialog.LeaveDialogMessage import LeaveDialogMessage
from com.ankamagames.dofus.network.messages.game.guild.tax.GuildFightPlayersHelpersLeaveMessage import GuildFightPlayersHelpersLeaveMessage
from com.ankamagames.dofus.network.messages.game.interactive.InteractiveUseEndedMessage import InteractiveUseEndedMessage
from com.ankamagames.dofus.network.messages.game.interactive.InteractiveUseErrorMessage import InteractiveUseErrorMessage
from com.ankamagames.dofus.network.messages.game.interactive.InteractiveUseRequestMessage import InteractiveUseRequestMessage
from com.ankamagames.dofus.network.messages.game.interactive.InteractiveUsedMessage import InteractiveUsedMessage
from com.ankamagames.dofus.network.messages.game.interactive.skill.InteractiveUseWithParamRequestMessage import InteractiveUseWithParamRequestMessage
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeLeaveMessage import ExchangeLeaveMessage
from com.ankamagames.dofus.network.messages.game.prism.PrismFightDefenderLeaveMessage import PrismFightDefenderLeaveMessage
from com.ankamagames.dofus.network.types.game.interactive.InteractiveElement import InteractiveElement
from com.ankamagames.dofus.types.entities.animatedCharacter import AnimatedCharacter
from com.ankamagames.jerakine.entities.interfaces.IEntity import IEntity
from com.ankamagames.jerakine.handlers.messages.Action import Action
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.messages.Frame import Frame
from com.ankamagames.jerakine.messages.Message import Message
from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.jerakine.types.enums.Priority import Priority
from com.ankamagames.jerakine.types.positions.MapPoint import MapPoint
from com.ankamagames.jerakine.types.positions.MouvementPath import MovementPath


class RoleplayMovementFrame(Frame):
   
   logger = Logger(__name__)
   
   CONSECUTIVE_MOVEMENT_DELAY:int = 250
   
   
   _wantToChangeMap:float = -1
   
   _changeMapByAutoTrip:bool = False
   
   _followingMove:MapPoint
   
   _followingIe:object
   
   _followingMonsterGroup:object
   
   _followingMessage
   
   _isRequestingMovement:bool
   
   _latestMovementRequest:int
   
   _destinationPoint:int
   
   _nextMovementBehavior:int
   
   _lastPlayerValidatedPosition:MapPoint
   
   _lastMoveEndCellId:int
   
   _canMove:bool = True
   
   _mapHasAggressiveMonsters:bool = False
   
   def __init__(self):
      super().__init__()
   
   @property
   def priority(self) -> int:
      return Priority.NORMAL
   
   @property
   def isRequestingMovement(self) -> bool:
      return self._isRequestingMovement
   
   def pushed(self) -> bool:
      self._wantToChangeMap = -1
      self._changeMapByAutoTrip = False
      self._followingIe = None
      self._followingMonsterGroup = None
      self._followingMove = None
      self._isRequestingMovement = False
      self._latestMovementRequest = 0
      return True
   
   def process(self, msg:Message) -> bool:

      if isinstance(msg, GameMapNoMovementMessage):
         self._isRequestingMovement = False
         if self._followingIe:
            self.activateSkill(self._followingIe.skillInstanceId, self._followingIe.ie, self._followingIe.additionalParam)
            self._followingIe = None
         if self._followingMonsterGroup:
            self.requestMonsterFight(self._followingMonsterGroup.id)
            self._followingMonsterGroup = None
         else:
            gmnmm = msg
            newPos = MapPoint.fromCoords(gmnmm.cellX,gmnmm.cellY)
            player = AnimatedCharacter(DofusEntities.getEntity(PlayedCharacterManager().id))
            if not player:
               return True
            if player.isMoving:
               player.stop(True)
               player.setAnimation("AnimStatique")
            player.position = newPos
            player.jump(newPos)
         return True

      if isinstance(msg, GameMapMovementMessage):
         gmmmsg = msg
         if gmmmsg.actorId != PlayedCharacterManager().id:
            self.applyGameMapMovement(gmmmsg.actorId, MapMovementAdapter.getClientMovement(gmmmsg.keyMovements), msg is GameCautiousMapMovementMessage)
         else:
            self._lastPlayerValidatedPosition = MapMovementAdapter.getClientMovement(gmmmsg.keyMovements).end
            if self._lastMoveEndCellId != self._lastPlayerValidatedPosition.cellId:
               playerEntity = DofusEntities.getEntity(PlayedCharacterManager().id) as AnimatedCharacter
               requestedPath = Pathfinding.findPath(DataMapProvider(),playerEntity.position,self._lastPlayerValidatedPosition,not playerEntity.cantWalk8Directions,True)
               self.applyGameMapMovement(gmmmsg.actorId,requestedPath,msg is GameCautiousMapMovementMessage)
         return True

      if isinstance(msg, EntityMovementCompleteMessage):
         emcmsg = msg
         if emcmsg.entity.id == PlayedCharacterManager().id:
            gmmcmsg = GameMapMovementConfirmMessage()
            gmmcmsg.initGameMapMovementConfirmMessage()
            ConnectionsHandler.getConnection().send(gmmcmsg)
            if self._wantToChangeMap >= 0 and emcmsg.entity.position.cellId == self._destinationPoint:
               self.askMapChange()
               self._isRequestingMovement = False
            if self._followingIe:
               self.activateSkill(self._followingIe.skillInstanceId,self._followingIe.ie,self._followingIe.additionalParam)
               self._followingIe = None
            if self._followingMonsterGroup:
               self.requestMonsterFight(self._followingMonsterGroup.id)
               self._followingMonsterGroup = None
            Kernel.getWorker().processImmediately(CharacterMovementStoppedMessage())
         return True

      if isinstance(msg, EntityMovementStoppedMessage):

            emsmsg = msg
            if emsmsg.entity.id == PlayedCharacterManager().id:
               canceledMoveMessage = GameMapMovementCancelMessage()
               canceledMoveMessage.initGameMapMovementCancelMessage(emsmsg.entity.position.cellId)
               ConnectionsHandler.getConnection().send(canceledMoveMessage)
               self._isRequestingMovement = False
               if self._followingMove and self._canMove:
                  self.askMoveTo(self._followingMove)
                  stackFrame = Kernel.getWorker().getFrame(StackManagementFrame) as StackManagementFrame
                  if stackFrame.len(stackOutputMessage) > 0:
                     moveBehavior = stackFrame.stackOutputMessage[0] as MoveBehavior
                     if moveBehavior and moveBehavior.position.cellId != self._followingMove.cellId:
                        Kernel.getWorker().process(EmptyStackAction.create())
                  self._followingMove = None
               if self._followingMessage:
                  if isinstance(self._followingMessage, PlayerFightRequestAction):

                        Kernel.getWorker().process(self._followingMessage)
                     default:
                        ConnectionsHandler.getConnection().send(self._followingMessage)
                  self._followingMessage = None
            return True
      if isinstance(msg, TeleportOnSameMapMessage):

            tosmmsg = msg
            teleportedEntity = DofusEntities.getEntity(tosmmsg.targetId)
            if teleportedEntity:
               if isinstance(teleportedEntity, IMovable):
                  if IMovable(teleportedEntity).isMoving:
                     IMovable(teleportedEntity).stop(True)
                  teleportedEntity
               else:
                  logger.warn("Cannot teleport a non IMovable entity. WTF ?")
            else:
               logger.warn("Received a teleportation request for a non-existing entity. Aborting.")
            return True
      if isinstance(msg, InteractiveUsedMessage):

            if InteractiveUsedMessage(msg).entityId == PlayedCharacterManager().id:
               self._canMove = InteractiveUsedMessage(msg).canMove
            return True
      if isinstance(msg, InteractiveUseEndedMessage):

            self._canMove = True
            return True
      if isinstance(msg, InteractiveUseErrorMessage):

            self._canMove = True
            return True
      if isinstance(msg, LeaveDialogMessage):

            self._canMove = True
            return False
      if isinstance(msg, ExchangeLeaveMessage):

            self._canMove = True
            return False
      if isinstance(msg, EditHavenBagFinishedMessage):

            self._canMove = True
            return False
      if isinstance(msg, GameRolePlayDelayedActionFinishedMessage):

            if GameRolePlayDelayedActionFinishedMessage(msg).delayedCharacterId == PlayedCharacterManager().id:
               self._canMove = True
            return False
      if isinstance(msg, GuildFightPlayersHelpersLeaveMessage):

            if GuildFightPlayersHelpersLeaveMessage(msg).playerId == PlayedCharacterManager().id:
               self._canMove = True
            return False
      if isinstance(msg, PrismFightDefenderLeaveMessage):

            if PrismFightDefenderLeaveMessage(msg).fighterToRemoveId == PlayedCharacterManager().id:
               self._canMove = True
            return False
      if isinstance(msg, GameRolePlayFightRequestCanceledMessage):

            if GameRolePlayFightRequestCanceledMessage(msg).targetId == PlayedCharacterManager().id or GameRolePlayFightRequestCanceledMessage(msg).sourceId == PlayedCharacterManager().id:
               self._canMove = True
            return False
      if isinstance(msg, MapComplementaryInformationsDataMessage):

            self._mapHasAggressiveMonsters = MapComplementaryInformationsDataMessage(msg).hasAggressiveMonsters
            return False
         default:
            return False
   
   def pulled(self) -> bool:
      return True
   
   def setNextMoveMapChange(self, mapId:float, autoTrip:bool = False) -> None:
      self._wantToChangeMap = mapId
      self._changeMapByAutoTrip = autoTrip
   
   def resetNextMoveMapChange(self) -> None:
      self._wantToChangeMap = -1
      self._changeMapByAutoTrip = False
   
   def setFollowingInteraction(self, interaction:Object) -> None:
      self._followingIe = interaction
   
   def setFollowingMonsterFight(self, monsterGroup:Object) -> None:
      self._followingMonsterGroup = monsterGroup
   
   def setFollowingMessage(self, message) -> None:
      if !(message is INetworkMessage or message is Action):
         raise Exception("The message is neither INetworkMessage or Action")
      self._followingMessage = message
   
   def forceNextMovementBehavior(self, pValue:int) -> None:
      self._nextMovementBehavior = pValue
   
   def askMoveTo(self, cell:MapPoint) -> bool:
      if not self._canMove or PlayedCharacterManager().state == PlayerLifeStatusEnum.STATUS_TOMBSTONE:
         return False
      if self._isRequestingMovement:
         return False
      stackFrame:StackManagementFrame = Kernel.getWorker().getFrame(StackManagementFrame) as StackManagementFrame
      stackMoveBehavior:MoveBehavior = stackFrame.len(stackOutputMessage) > 0 ? stackFrame.stackOutputMessage[0] as MoveBehavior : None
      now:int = perf_counter()
      if self._latestMovementRequest + CONSECUTIVE_MOVEMENT_DELAY > now and (not stackMoveBehavior or not stackMoveBehavior.getMapPoint().equals(cell)):
         return False
      self._isRequestingMovement = True
      playerEntity:AnimatedCharacter = DofusEntities.getEntity(PlayedCharacterManager().id) as AnimatedCharacter
      if not playerEntity:
         logger.warn("The player tried to move before its character was added to the scene. Aborting.")
         self._isRequestingMovement = False
         return False
      self._destinationPoint = cell.cellId
      if IMovable(playerEntity).isMoving:
         IMovable(playerEntity).stop()
         self._followingMove = cell
         return False
      playerEntity.visibleAura = False
      self.sendPath(Pathfinding.findPath(DataMapProvider(),playerEntity.position,cell,not playerEntity.cantWalk8Directions,True))
      return True
   
   def sendPath(self, path:MovementPath) -> None:
      gcmmrmsg:GameCautiousMapMovementRequestMessage = None
      gmmrmsg:GameMapMovementRequestMessage = None
      originalPath:MovementPath = path.clone()
      if path.start.cellId == path.end.cellId:
         logger.warn("Discarding a movement path that begins and ends on the same cell (" + path.start.cellId + ").")
         self._isRequestingMovement = False
         if self._followingIe:
            self.activateSkill(self._followingIe.skillInstanceId,self._followingIe.ie,self._followingIe.additionalParam)
            self._followingIe = None
         if self._followingMonsterGroup:
            self.requestMonsterFight(self._followingMonsterGroup.id)
            self._followingMonsterGroup = None
         return
      forceWalk:bool = False
      if OptionManager.getOptionManager("dofus").getOption("enableForceWalk") == True and (self._nextMovementBehavior == AtouinConstants.MOVEMENT_WALK or self._nextMovementBehavior == 0 and (ShortcutsFrame.ctrlKeyDown or SystemManager.getSingleton().os == OperatingSystem.MAC_OS and ShortcutsFrame.altKeyDown)) and not MountAutoTripManager().isTravelling:
         gcmmrmsg = GameCautiousMapMovementRequestMessage()
         gcmmrmsg.initGameCautiousMapMovementRequestMessage(MapMovementAdapter.getServerMovement(path),PlayedCharacterManager().currentMap.mapId)
         ConnectionsHandler.getConnection().send(gcmmrmsg)
         forceWalk = True
      else:
         gmmrmsg = GameMapMovementRequestMessage()
         gmmrmsg.initGameMapMovementRequestMessage(MapMovementAdapter.getServerMovement(path),PlayedCharacterManager().currentMap.mapId)
         ConnectionsHandler.getConnection().send(gmmrmsg)
      self.applyGameMapMovement(PlayedCharacterManager().id,originalPath,forceWalk)
      self._nextMovementBehavior = 0
      self._latestMovementRequest = perf_counter()
   
   def applyGameMapMovement(self, actorId:float, movement:MovementPath, forceWalking:bool = False) -> None:
      SpeakingItemManager().triggerEvent(SpeakingItemManager.SPEAK_TRIGGER_MOVE)
      movedEntity:IEntity = DofusEntities.getEntity(actorId)
      if not movedEntity:
         logger.warn("The entity " + actorId + " moved before it was added to the scene. Aborting movement.")
         return
      self._lastMoveEndCellId = movement.end.cellId
      rpEntitiesFrame:RoleplayEntitiesFrame = Kernel.getWorker().getFrame(RoleplayEntitiesFrame) as RoleplayEntitiesFrame
      tiphonSpr:TiphonSprite = movedEntity as TiphonSprite
      if tiphonSpr and not rpEntitiesFrame.isCreatureMode and tiphonSpr.getSubEntitySlot(SubEntityBindingPointCategoryEnum.HOOK_POINT_CATEGORY_MOUNT_DRIVER,0) and not tiphonSpr.getSubEntityBehavior(SubEntityBindingPointCategoryEnum.HOOK_POINT_CATEGORY_MOUNT_DRIVER):
         tiphonSpr.setSubEntityBehaviour(SubEntityBindingPointCategoryEnum.HOOK_POINT_CATEGORY_MOUNT_DRIVER,RiderBehavior())
      del rpEntitiesFrame.lastStaticAnimations[actorId]
      TooltipManager.hide("smiley" + actorId)
      TooltipManager.hide("msg" + actorId)
      if movedEntity.id == PlayedCharacterManager().id:
         self._isRequestingMovement = False
         KernelEventsManager().processCallback(TriggerHookList.PlayerMove)
      if OptionManager.getOptionManager("dofus").getOption("allowAnimsFun") == True:
         AnimFunManager().cancelAnim(actorId)
      movedEntity.move(movement,None,!not forceWalking ? WalkingMovementBehavior() : None)
   
   def askMapChange(self) -> None:
      cmmsg:ChangeMapMessage = ChangeMapMessage()
      cmmsg.initChangeMapMessage(self._wantToChangeMap,self._changeMapByAutoTrip)
      ConnectionsHandler.getConnection().send(cmmsg)
      self._wantToChangeMap = -1
      self._changeMapByAutoTrip = False
   
   def activateSkill(self, skillInstanceId:int, ie:InteractiveElement, additionalParam:int) -> None:
      iurmsg:InteractiveUseRequestMessage = None
      iuwprmsg:InteractiveUseWithParamRequestMessage = None
      rpInteractivesFrame:RoleplayInteractivesFrame = Kernel.getWorker().getFrame(RoleplayInteractivesFrame) as RoleplayInteractivesFrame
      if rpInteractivesFrame and rpInteractivesFrame.currentRequestedElementId != ie.elementId and not rpInteractivesFrame.usingInteractive and not rpInteractivesFrame.isElementChangingState(ie.elementId):
         rpInteractivesFrame.currentRequestedElementId = ie.elementId
         if additionalParam == 0:
            iurmsg = InteractiveUseRequestMessage()
            iurmsg.initInteractiveUseRequestMessage(ie.elementId,skillInstanceId)
            ConnectionsHandler.getConnection().send(iurmsg)
         else:
            iuwprmsg = InteractiveUseWithParamRequestMessage()
            iuwprmsg.initInteractiveUseWithParamRequestMessage(ie.elementId,skillInstanceId,additionalParam)
            ConnectionsHandler.getConnection().send(iuwprmsg)
         self._canMove = False
   
   def requestMonsterFight(self, monsterGroupId:int) -> None:
      grpamrmsg:GameRolePlayAttackMonsterRequestMessage = GameRolePlayAttackMonsterRequestMessage()
      grpamrmsg.initGameRolePlayAttackMonsterRequestMessage(monsterGroupId)
      ConnectionsHandler.getConnection().send(grpamrmsg)
