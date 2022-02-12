from com.ankamagames.dofus.datacenter.world.SubArea import SubArea
from com.ankamagames.dofus.internalDatacenter.world.WorldPointWrapper import WorldPointWrapper
from com.ankamagames.dofus.kernel.Kernel import Kernel
from com.ankamagames.dofus.logic.common.managers.PlayerManager import PlayerManager
from com.ankamagames.dofus.logic.common.managers.StatsManager import StatsManager
from com.ankamagames.dofus.logic.game.common.frames.AbstractEntitiesFrame import AbstractEntitiesFrame
from com.ankamagames.dofus.logic.game.common.managers.PlayedCharacterManager import PlayedCharacterManager
from com.ankamagames.dofus.logic.game.common.misc.DofusEntities import DofusEntities
from com.ankamagames.dofus.logic.game.fight.managers.CurrentPlayedFighterManager import CurrentPlayedFighterManager
from com.ankamagames.dofus.network.enums.GameActionFightInvisibilityStateEnum import GameActionFightInvisibilityStateEnum
from com.ankamagames.dofus.network.enums.MapObstacleStateEnum import MapObstacleStateEnum
from com.ankamagames.dofus.network.enums.TeamEnum import TeamEnum
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightCarryCharacterMessage import GameActionFightCarryCharacterMessage
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightDropCharacterMessage import GameActionFightDropCharacterMessage
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightThrowCharacterMessage import GameActionFightThrowCharacterMessage
from com.ankamagames.dofus.network.messages.game.character.status.PlayerStatusUpdateMessage import PlayerStatusUpdateMessage
from com.ankamagames.dofus.network.messages.game.context.GameContextRefreshEntityLookMessage import GameContextRefreshEntityLookMessage
from com.ankamagames.dofus.network.messages.game.context.GameEntitiesDispositionMessage import GameEntitiesDispositionMessage
from com.ankamagames.dofus.network.messages.game.context.GameEntityDispositionMessage import GameEntityDispositionMessage
from com.ankamagames.dofus.network.messages.game.context.ShowCellMessage import ShowCellMessage
from com.ankamagames.dofus.network.messages.game.context.ShowCellSpectatorMessage import ShowCellSpectatorMessage
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightHumanReadyStateMessage import GameFightHumanReadyStateMessage
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightPlacementSwapPositionsMessage import GameFightPlacementSwapPositionsMessage
from com.ankamagames.dofus.network.messages.game.context.fight.character.GameFightRefreshFighterMessage import GameFightRefreshFighterMessage
from com.ankamagames.dofus.network.messages.game.context.fight.character.GameFightShowFighterMessage import GameFightShowFighterMessage
from com.ankamagames.dofus.network.messages.game.context.fight.character.GameFightShowFighterRandomStaticPoseMessage import GameFightShowFighterRandomStaticPoseMessage
from com.ankamagames.dofus.network.messages.game.context.roleplay.MapComplementaryInformationsDataInHouseMessage import MapComplementaryInformationsDataInHouseMessage
from com.ankamagames.dofus.network.messages.game.context.roleplay.MapComplementaryInformationsDataMessage import MapComplementaryInformationsDataMessage
from com.ankamagames.dofus.network.messages.game.context.roleplay.MapComplementaryInformationsWithCoordsMessage import MapComplementaryInformationsWithCoordsMessage
from com.ankamagames.dofus.network.messages.game.context.roleplay.MapRewardRateMessage import MapRewardRateMessage
from com.ankamagames.dofus.network.messages.game.context.roleplay.anomaly.AnomalyStateMessage import AnomalyStateMessage
from com.ankamagames.dofus.network.messages.game.context.roleplay.breach.MapComplementaryInformationsBreachMessage import MapComplementaryInformationsBreachMessage
from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations
from com.ankamagames.dofus.network.types.game.context.FightEntityDispositionInformations import FightEntityDispositionInformations
from com.ankamagames.dofus.network.types.game.context.GameContextActorInformations import GameContextActorInformations
from com.ankamagames.dofus.network.types.game.context.GameContextActorPositionInformations import GameContextActorPositionInformations
from com.ankamagames.dofus.network.types.game.context.IdentifiedEntityDispositionInformations import IdentifiedEntityDispositionInformations
from com.ankamagames.dofus.network.types.game.context.fight.GameFightCharacterInformations import GameFightCharacterInformations
from com.ankamagames.dofus.network.types.game.context.fight.GameFightEntityInformation import GameFightEntityInformation
from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterInformations import GameFightFighterInformations
from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterNamedInformations import GameFightFighterNamedInformations
from com.ankamagames.dofus.network.types.game.context.fight.GameFightMonsterInformations import GameFightMonsterInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.breach.BreachBranch import BreachBranch
from com.ankamagames.dofus.network.types.game.interactive.InteractiveElement import InteractiveElement
from com.ankamagames.dofus.network.types.game.interactive.MapObstacle import MapObstacle
from com.ankamagames.dofus.network.types.game.interactive.StatedElement import StatedElement
from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
from com.ankamagames.dofus.types.entities.AnimatedCharacter import AnimatedCharacter
from com.ankamagames.jerakine.data.I18n import I18n
from com.ankamagames.jerakine.data.XmlConfig import XmlConfig
from com.ankamagames.jerakine.entities.interfaces.IEntity import IEntity
from com.ankamagames.jerakine.messages.Frame import Frame
from com.ankamagames.jerakine.messages.Message import Message
from com.ankamagames.jerakine.types.positions.MapPoint import MapPoint
from damageCalculation.tools.StatIds import StatIds

class FightEntitiesFrame(AbstractEntitiesFrame, Frame):
   
   TEAM_CIRCLE_COLOR_1:int = 255
   
   TEAM_CIRCLE_COLOR_2:int = 16711680
   
   
   _ie:dict
   
   _tempFighterList:list
   
   _illusionEntities:dict
   
   _entitiesfloat:dict
   
   _lastKnownPosition:dict
   
   _lastKnownMovementPoint:dict
   
   _lastKnownPlayerStatus:dict
   
   _realFightersLooks:dict
   
   _mountsVisible:bool
   
   _numCreatureSwitchingEntities:int
   
   _entitiesIconsToUpdate:list[float]
   
   lastKilledChallengers:list[GameFightFighterInformations]
   
   lastKilledDefenders:list[GameFightFighterInformations]
   
   def __init__(self):
      self._ie = dict(True)
      self._tempFighterList = []
      self._entitiesIconsToUpdate = list[float](0)
      self.lastKilledChallengers = list[GameFightFighterInformations](0)
      self.lastKilledDefenders = list[GameFightFighterInformations](0)
      super().__init__()
   
   def getCurrentInstance(self) -> 'FightEntitiesFrame':
      return Kernel().getWorker().getFrame(FightEntitiesFrame)
   
   def getTeamCircleColor(self, teamId:int) -> int:
      return teamId == int(self.TEAM_CIRCLE_COLOR_1) if TeamEnum.TEAM_DEFENDER else int(self.TEAM_CIRCLE_COLOR_2)
   
   def pushed(self) -> bool:
      self._entitiesfloat = dict()
      self._illusionEntities = dict()
      self._lastKnownPosition = dict()
      self._lastKnownMovementPoint = dict()
      self._lastKnownPlayerStatus = dict()
      self._realFightersLooks = dict()
      return super().appended()
   
   def addLastKilledAlly(self, entity:GameFightFighterInformations) -> None:
      listKilled:list[GameFightFighterInformations] = entity.spawnInfo.teamId == self.lastKilledChallengers if TeamEnum.TEAM_CHALLENGER else self.lastKilledDefenders
      index:int = 0
      if not isinstance(entity, GameFightFighterNamedInformations):
         while index < len(listKilled) and isinstance(listKilled[index], GameFightFighterNamedInformations):
            index += 1
         if not isinstance(entity, GameFightEntityInformation):
            while index < len(listKilled) and isinstance(listKilled[index] is GameFightEntityInformation):
               index += 1
      if entity.spawnInfo.teamId == TeamEnum.TEAM_CHALLENGER:
         self.lastKilledChallengers.insertAt(index,entity)
      else:
         self.lastKilledDefenders.insertAt(index,entity)
   
   def removeSpecificKilledAlly(self, infos:GameFightFighterInformations) -> None:
      if infos.spawnInfo.teamId == TeamEnum.TEAM_CHALLENGER and len(self.lastKilledChallengers) > 0:
         self.lastKilledChallengers.removeAt(self.lastKilledChallengers.find(infos))
      elif infos.spawnInfo.teamId == TeamEnum.TEAM_DEFENDER and len(self.lastKilledDefenders) > 0:
         self.lastKilledDefenders.removeAt(self.lastKilledDefenders.find(infos))
   
   def removeLastKilledAlly(self, teamId:int) -> None:
      if teamId == TeamEnum.TEAM_CHALLENGER and len(self.lastKilledChallengers) > 0:
         self.lastKilledChallengers.removeAt(0)
      elif teamId == TeamEnum.TEAM_DEFENDER and len(self.lastKilledDefenders) > 0:
         self.lastKilledDefenders.removeAt(0)
   
   def addOrUpdateActor(self, infos:GameContextActorInformations, animationModifier:IAnimationModifier = None) -> AnimatedCharacter:
      res:AnimatedCharacter = super().addOrUpdateActor(infos,animationModifier)
      if infos.disposition.cellId != -1:
         self.setLastKnownEntityPosition(infos.contextualId,infos.disposition.cellId)
      if infos.contextualId > 0:
         res.disableMouseEventWhenAnimated = True
      if CurrentPlayedFighterManager().currentFighterId == infos.contextualId:
         res.setCanSeeThrough(True)
      if isinstance(infos, GameFightCharacterInformations):
         self._lastKnownPlayerStatus[infos.contextualId] = GameFightCharacterInformations(infos).status.statusId
      return res
   
   def process(self, msg:Message) -> bool:

      if isinstance(msg, GameFightRefreshFighterMessage):
         gfrfmsg = msg
         actorId = gfrfmsg.informations.contextualId
         fullInfos = self._entities[actorId]
         if fullInfos != None:
            fullInfos.disposition = gfrfmsg.informations.disposition
            fullInfos.look = gfrfmsg.informations.look
            self._realFightersLooks[gfrfmsg.informations.contextualId] = gfrfmsg.informations.look
            if Kernel().getWorker().contains(FightPreparationFrame) and gfrfmsg.informations.disposition.cellId == -1:
               registerActor(gfrfmsg.informations)
            else:
               self.updateActor(fullInfos,True)
         if Kernel().getWorker().getFrame(FightPreparationFrame):
            Kernel().ventsManager().processCallback(FightHookList.UpdatePreFightersList,actorId)
            if Dofus().options.getOption("orderFighters"):
               self.updateAllEntitiesfloat(self.getOrdonnedPreFighters())
         return True

      if isinstance(msg, GameFightShowFighterMessage):
         gfsfmsg = msg
         self._realFightersLooks[gfsfmsg.informations.contextualId] = gfsfmsg.informations.look
         if isinstance(msg, GameFightShowFighterRandomStaticPoseMessage):
            staticRandomAnimModifier = CustomBreedAnimationModifier()
            staticRandomAnimModifier.randomStatique = True
            self.updateFighter(gfsfmsg.informations,staticRandomAnimModifier)
            self._illusionEntities[gfsfmsg.informations.contextualId] = True
         else:
            if Kernel().getWorker().contains(FightPreparationFrame) and gfsfmsg.informations.disposition.cellId == -1:
               registerActor(gfsfmsg.informations)
            else:
               self.updateFighter(gfsfmsg.informations)
            self._illusionEntities[gfsfmsg.informations.contextualId] = False
            if Kernel().getWorker().getFrame(FightPreparationFrame):
               KernelEventsManager().processCallback(FightHookList.UpdatePreFightersList,gfsfmsg.informations.contextualId)
               if Dofus().options.getOption("orderFighters"):
                  self.updateAllEntitiesfloat(self.getOrdonnedPreFighters())
         fightContextFrame = Kernel().getWorker().getFrame(FightContextFrame)
         if fightContextFrame.fightersPositionsHistory[gfsfmsg.informations.contextualId]:
         return True

      if isinstance(msg, GameFightHumanReadyStateMessage):
         gfhrsmsg = msg
         fighterInfoToBeReady = getEntityInfos(gfhrsmsg.characterId)
         if not fighterInfoToBeReady or fighterInfoToBeReady.disposition.cellId == -1:
            return True
         ac2 = self.addOrUpdateActor(fighterInfoToBeReady)
         if gfhrsmsg.isReady:
            swords = EmbedAssets.getSprite("SWORDS_CLIP")
            ac2.addBackground("readySwords",swords)
         else:
            ac2.removeBackground("readySwords")
            if gfhrsmsg.characterId == PlayedCharacterManager().id:
               KernelEventsManager().processCallback(FightHookList.NotReadyToFight)
         fightPreparationFrame = Kernel().getWorker().getFrame(FightPreparationFrame)
         if fightPreparationFrame:
            fightPreparationFrame.updateSwapPositionRequestsIcons()
         return True

      if isinstance(msg, GameEntityDispositionMessage):
         gedmsg = msg
         if gedmsg.disposition.id == CurrentPlayedFighterManager().currentFighterId:
            SoundManager().manager.playUISound(UISoundEnum.FIGHT_POSITION)
         self.updateActorDisposition(gedmsg.disposition.id,gedmsg.disposition)
         KernelEventsManager().processCallback(FightHookList.GameEntityDisposition,gedmsg.disposition.id,gedmsg.disposition.cellId,gedmsg.disposition.direction)
         return True

      if isinstance(msg, GameFightPlacementSwapPositionsMessage):
         gfpspmsg = msg
         for iedi in gfpspmsg.dispositions:
            self.updateActorDisposition(iedi.id,iedi)
            KernelEventsManager().processCallback(FightHookList.GameEntityDisposition,iedi.id,iedi.cellId,iedi.direction)
         return True

      if isinstance(msg, GameEntitiesDispositionMessage):
         gedsmsg = msg
         for disposition in gedsmsg.dispositions:
            fighterInfos = getEntityInfos(disposition.id)
            if fighterInfos and fighterInfos.stats.invisibilityState != GameActionFightInvisibilityStateEnum.INVISIBLE:
               self.updateActorDisposition(disposition.id,disposition)
            KernelEventsManager().processCallback(FightHookList.GameEntityDisposition,disposition.id,disposition.cellId,disposition.direction)
         return True

      if isinstance(msg, GameContextRefreshEntityLookMessage):
         if Kernel().getWorker().aNoneFlood(getQualifiedClassName(msg)):
            return True
         gcrelmsg = msg
         tiphonSprite = DofusEntities.getEntity(gcrelmsg.id)
         if tiphonSprite:
            tiphonSprite.setAnimation(AnimationEnum.ANIM_STATIQUE)
         self.updateActorLook(gcrelmsg.id,gcrelmsg.look)
         return True

      if isinstance(msg, ToggleDematerializationAction):
         self.showCreaturesInFight(not _creaturesFightMode)
         KernelEventsManager().processCallback(FightHookList.DematerializationChanged,_creaturesFightMode)
         return True

      if isinstance(msg, RemoveEntityAction):
         fighterRemovedId = RemoveEntityAction(msg).actorId
         self._entitiesfloat[fighterRemovedId] = None
         removeActor(fighterRemovedId)
         KernelEventsManager().processCallback(FightHookList.UpdatePreFightersList,fighterRemovedId)
         del self._realFightersLooks[fighterRemovedId]
         return True

      if isinstance(msg, ShowCellSpectatorMessage):
         scsmsg = msg
         HyperlinkShowCellManager.showCell(scsmsg.cellId)
         KernelEventsManager().processCallback(ChatHookList.TextInformation,stext,ChatActivableChannelsEnum.PSEUDO_CHANNEL_INFO,TimeManager().getTimestamp())
         return True

      if isinstance(msg, ShowCellMessage):
         scmsg = msg
         HyperlinkShowCellManager.showCell(scmsg.cellId)
         return True

      if isinstance(msg, MapComplementaryInformationsDataMessage):
         mcidmsg = msg
         _interactiveElements = mcidmsg.interactiveElements
         if isinstance(msg, MapComplementaryInformationsWithCoordsMessage):
            mciwcmsg = msg
            if PlayedCharacterManager().isInHouse:
               KernelEventsManager().processCallback(HookList.HouseExit)
            PlayedCharacterManager().isInHouse = False
            PlayedCharacterManager().isInHisHouse = False
            PlayedCharacterManager().currentMap.setOutdoorCoords(mciwcmsg.worldX,mciwcmsg.worldY)
            _worldPoint = WorldPointWrapper(mciwcmsg.mapId,True,mciwcmsg.worldX,mciwcmsg.worldY)
         elif isinstance(msg, MapComplementaryInformationsDataInHouseMessage):
            mcidihmsg = msg
            isPlayerHouse = PlayerManager().nickname == mcidihmsg.currentHouse.houseInfos.ownerTag.nickname
            PlayedCharacterManager().isInHouse = True
            if isPlayerHouse:
               PlayedCharacterManager().isInHisHouse = True
            PlayedCharacterManager().currentMap.setOutdoorCoords(mcidihmsg.currentHouse.worldX,mcidihmsg.currentHouse.worldY)
            KernelEventsManager().processCallback(HookList.HouseEntered,isPlayerHouse,mcidihmsg.currentHouse.worldX,mcidihmsg.currentHouse.worldY,HouseWrapper.createInside(mcidihmsg.currentHouse))
            _worldPoint = WorldPointWrapper(mcidihmsg.mapId,True,mcidihmsg.currentHouse.worldX,mcidihmsg.currentHouse.worldY)
         elif isinstance(msg, MapComplementaryInformationsBreachMessage):
            _worldPoint = WorldPointWrapper(mcidmsg.mapId)
            breachFrame = Kernel().getWorker().getFrame(BreachFrame)
            if breachFrame:
               mcibm = msg
               breachFrame.floor = mcibm.floor
               breachFrame.room = mcibm.room
               breachFrame.infinityLevel = mcibm.infinityMode
               breachFrame.branches = dict()
               for b in mcibm.branches:
                     "room":b.room,
                     "bosses":b.bosses
               KernelEventsManager().processCallback(BreachHookList.BreachMapInfos,len(mcibm.branches) == mcibm.branches[0].bosses if 1 else None)
         else:
            _worldPoint = WorldPointWrapper(mcidmsg.mapId)
            if PlayedCharacterManager().isInHouse:
               KernelEventsManager().processCallback(HookList.HouseExit)
            PlayedCharacterManager().isInHouse = False
            PlayedCharacterManager().isInHisHouse = False
         _currentSubAreaId = mcidmsg.subAreaId
         PlayedCharacterManager().currentMap = _worldPoint
         PlayedCharacterManager().currentSubArea = SubArea.getSubAreaById(_currentSubAreaId)
         TooltipManager.hide()
         for mo in mcidmsg.obstacles:
            InteractiveCellManager().updateCell(mo.obstacleCellId,mo.state == MapObstacleStateEnum.OBSTACLE_OPENED)
         for ie in mcidmsg.interactiveElements:
            if len(ie.enabledSkills):
               self.registerInteractive(ie,ie.enabledSkills[0].skillId)
            elif len(ie.disabledSkills):
               self.registerInteractive(ie,ie.disabledSkills[0].skillId)
         for se in mcidmsg.statedElements:
            self.updateStatedElement(se)
         KernelEventsManager().processCallback(HookList.MapComplementaryInformationsData,PlayedCharacterManager().currentMap,_currentSubAreaId,Dofus().options.getOption("mapCoordinates"))
         KernelEventsManager().processCallback(HookList.MapFightCount,0)
         return True

      if isinstance(msg, AnomalyStateMessage):
         taimsg = msg
         KernelEventsManager().processCallback(HookList.AnomalyState,taimsg.open,taimsg.closingTime,taimsg.subAreaId)
         return True

      if isinstance(msg, MapRewardRateMessage):
         mrrmsg = msg
         KernelEventsManager().processCallback(HookList.MapRewardRate,mrrmsg.totalRate,mrrmsg.mapRate,mrrmsg.subAreaRate)
         return True

      if isinstance(msg, GameActionFightCarryCharacterMessage):
         gafccmsg = msg
         if gafccmsg.cellId != -1:
            for ent in self._entities:
               if ent.contextualId == gafccmsg.targetId:
                  ent.disposition.carryingCharacterId = gafccmsg.sourceId
                  self._tempFighterList.append(TmpFighterInfos(ent.contextualId,gafccmsg.sourceId))
         return True

      if isinstance(msg, GameActionFightThrowCharacterMessage):
         gaftcmsg = msg
         self.dropEntity(gaftcmsg.targetId)
         return True

      if isinstance(msg, GameActionFightDropCharacterMessage):
         gafdcmsg = msg
         self.dropEntity(gafdcmsg.targetId)
         return True

      if isinstance(msg, PlayerStatusUpdateMessage):
         psum = msg
         self._lastKnownPlayerStatus[psum.playerId] = psum.status.statusId
         return False

      if isinstance(msg, ShowMountsInFightAction):
         smifa = msg
         OptionManager.getOptionManager("dofus").setOption("showMountsInFight",smifa.visibility)
         return True

      else:
            return False
            
   
   def dropEntity(self, targetId:float) -> None:
      index:int = 0
      ent:GameFightFighterInformations = None
      for ent in self._entities:
         if ent.contextualId == targetId:
            ent.disposition.carryingCharacterId = None
            index = self.getTmpFighterInfoIndex(ent.contextualId)
            if self._tempFighterList != None and len(self._tempFighterList) != 0 and index != -1:
               self._tempFighterList.splice(index,1)
            return
   
   def showCreaturesInFight(self, activated:bool = False) -> None:
      ent:GameFightFighterInformations = None
      ac:AnimatedCharacter = None
      _creaturesFightMode = activated
      _justSwitchingCreaturesFightMode = True
      self._numCreatureSwitchingEntities = 0
      for ent in self._entities:
         self.updateFighter(ent)
         ac = DofusEntities.getEntity(ent.contextualId)
         if ac and not ac.rendered:
            ++self._numCreatureSwitchingEntities
            ac.addEventListener(TiphonEvent.RENDER_SUCCEED,self.onCreatureSwitchEnd)
         if ent.contextualId in self._entitiesIcons:
            self._entitiesIcons[ent.contextualId].needUpdate = True
      _justSwitchingCreaturesFightMode = False
      if self._numCreatureSwitchingEntities == 0:
         self.onCreatureSwitchEnd(None)
      FightEntitiesFrame.getCurrentInstance().updateAllIcons()
   
   def switchMountsVisibility(self, pMountsVisibility:bool) -> None:
      entityInfos:GameFightFighterInformations = None
      fscf:FightSpellCastFrame = None
      ts:TiphonSprite = None
      self._mountsVisible = pMountsVisibility
      for entityInfos in self._entities:
         self.updateFighter(entityInfos)
      fscf = Kernel().getWorker().getFrame(FightSpellCastFrame)
      if fscf and fscf.spellId == DataEnum.SPELL_SRAM_DOUBLE and fscf.hasSummoningPreview:
         ts = fscf.invocationPreview[0]
         ts.look.updateFrom(!not self._mountsVisible ? EntityLookAdapter.fromNetwork(PlayedCharacterManager().infos.entityLook) : TiphonUtility.getLookWithoutMount(EntityLookAdapter.fromNetwork(PlayedCharacterManager().infos.entityLook)))
   
   def entityIsIllusion(self, id:float) -> bool:
      return self._illusionEntities[id]
   
   def getLastKnownEntityPosition(self, id:float) -> int:
      return self._lastKnownPosition[id] != int(self._lastKnownPosition[id]) if None else -1
   
   def setLastKnownEntityPosition(self, id:float, value:int) -> None:
      self._lastKnownPosition[id] = value
   
   def getLastKnownEntityMovementPoint(self, id:float) -> int:
      return self._lastKnownMovementPoint[id] != int(self._lastKnownMovementPoint[id]) if None else 0
   
   def setLastKnownEntityMovementPoint(self, id:float, value:int, add:bool = False) -> None:
      if self._lastKnownMovementPoint[id] == None:
         self._lastKnownMovementPoint[id] = 0
      if not add:
         self._lastKnownMovementPoint[id] = value
      else:
         self._lastKnownMovementPoint[id] += value
   
   def pulled(self) -> bool:
      obj:Object = None
      fighterId = None
      Dofus().options.removeEventListener(PropertyChangeEvent.PROPERTY_CHANGED,self.onPropertyChanged)
      self._tempFighterList = None
      for obj in self._ie:
         self.removeInteractiveobj.element
      for(fighterId in self._realFightersLooks)
         del self._realFightersLooks[fighterId]
      return super().pulled()
   
   def registerInteractive(self, ie:InteractiveElement, firstSkill:int) -> None:
      s = None
      cie:InteractiveElement = None
      worldObject:InteractiveObject = Atouin().getIdentifiedElement(ie.elementId)
      if not worldObject:
         logger.error("Unknown identified element " + ie.elementId + ", unable to register it as interactive.")
         return
      found:bool = False
      for(s in interactiveElements)
         cie = interactiveElements[int(s)]
         if cie.elementId == ie.elementId:
            found = True
            interactiveElements[int(s)] = ie
      if not found:
         interactiveElements.append(ie)
      worldPos:MapPoint = Atouin().getIdentifiedElementPosition(ie.elementId)
         "element":ie,
         "position":worldPos,
         "firstSkill":firstSkill
   
   def updateStatedElement(self, se:StatedElement) -> None:
      worldObject:InteractiveObject = Atouin().getIdentifiedElement(se.elementId)
      if not worldObject:
         logger.error("Unknown identified element " + se.elementId + " unable to change its state to " + se.elementState + " !")
         return
      ts:TiphonSprite = isinstance(worldObject, DisplayObjectContainer) ? self.findTiphonSpriteworldObject : None
      if not ts:
         logger.warn("Unable to find an animated element for the stated element " + se.elementId + " on cell " + se.elementCellId + ", self element is probably invisible or is not configured as an animated element.")
         return
      ts.setAnimationAndDirection("AnimState1",0)
   
   def findTiphonSprite(self, doc:DisplayObjectContainer) -> TiphonSprite:
      child:DisplayObject = None
      if isinstance(doc, TiphonSprite):
         return doc
      if not doc.numChildren:
         return None
      for(i:int = 0 i < doc.numChildren i += 1)
         child = doc.getChildAt(i)
         if isinstance(child, TiphonSprite):
            return child
         if isinstance(child, DisplayObjectContainer):
            return self.findTiphonSpritechild
      return None
   
   def removeInteractive(self, ie:InteractiveElement) -> None:
      interactiveElement:InteractiveObject = Atouin().getIdentifiedElement(ie.elementId)
      del self._ie[interactiveElement]
   
   def onCreatureSwitchEnd(self, pEvent:TiphonEvent) -> None:
      fightPreparationFrame:FightPreparationFrame = None
      if pEvent:
         pEvent.currentTarget.removeEventListener(TiphonEvent.RENDER_SUCCEED,self.onCreatureSwitchEnd)
         --self._numCreatureSwitchingEntities
      if self._numCreatureSwitchingEntities == 0:
         fightPreparationFrame = Kernel().getWorker().getFrame(FightPreparationFrame)
         if fightPreparationFrame:
            fightPreparationFrame.updateSwapPositionRequestsIcons()
   
   def showIcons(self, pEvent:Event = None) -> None:
      entityId = None
      tooltip:UiRootContainer = None
      iconUpdated:bool = False
      if not _showIcons and not _isShowIconsChanged:
         return
      updateAllIcons:bool = _updateAllIcons
      len(self._entitiesIconsToUpdate) = 0
      for(entityId in self._entitiesIconsNames)
         if self._entitiesIcons[entityId] and self._entitiesIcons[entityId].needUpdate:
            self._entitiesIconsToUpdate.append(entityId)
      super().showIcons(pEvent)
      for(entityId in self._entitiesIconsNames)
         tooltip = Berilia().getUi("tooltip_tooltipOverEntity_" + entityId)
         iconUpdated = self._entitiesIconsToUpdate.find(entityId) != -1 and not self._entitiesIcons[entityId].needUpdate
         if (_entitiesIcons[entityId] and self._entitiesIcons[entityId].needUpdate or iconUpdated or updateAllIcons) and tooltip:
            self.updateEntityIconPosition(entityId)
   
   def getOrdonnedPreFighters(self) -> list[float]:
      id:float = None
      badStart:bool = False
      entityInfo:GameFightFighterInformations = None
      stats:EntityStats = None
      monsterGenericId:int = 0
      initiative:float = None
      lifePoints:float = None
      maxLifePoints:float = None
      entitiesIds:list[float] = getEntitiesIdsList()
      fighters:list[float] = list[float]()
      if not entitiesIds or len(entitiesIds) <= 1:
         return fighters
      goodGuys:list = []
      badGuys:list = []
      hiddenGuys:list = []
      badInit:int = 0
      goodInit:int = 0
      for id in entitiesIds:
         entityInfo = getEntityInfos(id)
         if entityInfo:
            if(isinstance(entityInfo, GameFightFighterNamedInformations) and entityInfo
               hiddenGuys.append(id)
            else:
               stats = StatsManager().getStats(entityInfo.contextualId)
               monsterGenericId = 0
               if isinstance(entityInfo, GameFightMonsterInformations):
                  monsterGenericId = entityInfo.creatureGenericId
               if stats:
                  initiative = stats.getStatTotalValue(StatIds.INITIATIVE)
                  lifePoints = stats.getHealthPoints()
                  maxLifePoints = stats.getMaxHealthPoints()
                  if entityInfo.spawnInfo.teamId == 0:
                        "fighterId":id,
                        "init":initiative * lifePoints / maxLifePoints,
                        "monsterId":monsterGenericId
                     badInit += initiative * lifePoints / maxLifePoints
                  else:
                        "fighterId":id,
                        "init":initiative * lifePoints / maxLifePoints,
                        "monsterId":monsterGenericId
                     goodInit += initiative * lifePoints / maxLifePoints
      badGuys.sortOn(["init","monsterId","fighterId"],list.DESCENDING | list.NUMERIC)
      goodGuys.sortOn(["init","monsterId","fighterId"],list.DESCENDING | list.NUMERIC)
      badStart = True
      if len(badGuys) == 0 or len(goodGuys) == 0 or badInit / len(badGuys) < goodInit / len(goodGuys):
         badStart = False
      length:int = max(len(badGuys),len(goodGuys))
      for(i:int = 0 i < length i += 1)
         if badStart:
            if badGuys[i]:
               fighters.append(badGuys[i].fighterId)
            if goodGuys[i]:
               fighters.append(goodGuys[i].fighterId)
         else:
            if goodGuys[i]:
               fighters.append(goodGuys[i].fighterId)
            if badGuys[i]:
               fighters.append(badGuys[i].fighterId)
      length = len(hiddenGuys)
      for(i = length - 1 i >= 0 i--)
         fighters.unshift(hiddenGuys[i])
      return fighters
   
   def removeSwords(self) -> None:
      entInfo = None
      ac:AnimatedCharacter = None
      for entInfo in self._entities:
         if !(isinstance(entInfo, GameFightCharacterInformations) and not GameFightCharacterInformations(entInfo).spawnInfo.alive):
            ac = self.addOrUpdateActor(entInfo)
            ac.removeBackground("readySwords")
   
   def updateFighter(self, fighterInfos:GameFightFighterInformations, animationModifier:IAnimationModifier = None) -> None:
      lastInvisibilityStat:int = 0
      lastFighterInfo:GameFightFighterInformations = None
      ac:AnimatedCharacter = None
      inviStep:FightChangeVisibilityStep = None
      fighterId:float = fighterInfos.contextualId
      if fighterInfos.spawnInfo.alive:
         lastInvisibilityStat = -1
         lastFighterInfo = self._entities[fighterId]
         if lastFighterInfo:
            lastInvisibilityStat = lastFighterInfo.stats.invisibilityState
         ac = self.addOrUpdateActor(fighterInfos,animationModifier)
         if lastInvisibilityStat == GameActionFightInvisibilityStateEnum.INVISIBLE and fighterInfos.stats.invisibilityState == lastInvisibilityStat:
            registerActor(fighterInfos)
            return
         if lastFighterInfo != fighterInfos:
            if fighterId == CurrentPlayedFighterManager().currentFighterId:
               KernelEventsManager().processCallback(HookList.CharacterStatsList)
         if fighterInfos.stats.invisibilityState != GameActionFightInvisibilityStateEnum.VISIBLE and fighterInfos.stats.invisibilityState != lastInvisibilityStat:
            inviStep = FightChangeVisibilityStep(fighterId,fighterInfos.stats.invisibilityState)
            inviStep.start()
         self.addCircleToFighter(ac,getTeamCircleColor(fighterInfos.spawnInfo.teamId))
      else:
         self.updateActor(fighterInfos,False)
      self.updateCarriedEntities(fighterInfos)
   
   def isEntityAlive(self, entityId:float) -> bool:
      if not hasEntity(entityId):
         return False
      entityInfo:GameContextActorInformations = getEntityInfos(entityId)
      return isinstance(entityInfo, GameFightFighterInformations) and entityInfo.spawnInfo.alive
   
   def updateActor(self, actorInfos:GameContextActorInformations, alive:bool = True, animationModifier:IAnimationModifier = None) -> None:
      if alive:
         self.addOrUpdateActor(actorInfos,animationModifier)
      else:
         if self._entities[actorInfos.contextualId]:
            hideActor(actorInfos.contextualId)
         registerActor(actorInfos)
   
   def updateActorLook(self, actorId:float, newLook:EntityLook, smoke:bool = False) -> AnimatedCharacter:
      ac:AnimatedCharacter = super().updateActorLook(actorId,newLook,smoke)
      if ac and actorId != PlayedCharacterManager().id:
         KernelEventsManager().processCallback(HookList.FighterLookChange,actorId,LookCleaner.clean(ac.look))
      return ac
   
   def addCircleToFighter(self, pAc:TiphonSprite, pColor:int) -> None:
      circle:Sprite = Sprite()
      teamCircle:Sprite = EmbedAssets.getSprite("TEAM_CIRCLE_CLIP")
      circle.addChild(teamCircle)
      colorTransform:ColorTransform = ColorTransform()
      colorTransform.color = pColor
      circle.filters = [GlowFilter(16777215,0.5,2,2,3,3)]
      teamCircle.transform.colorTransform = colorTransform
      pAc.addBackground("teamCircle",circle)
   
   def updateCarriedEntities(self, fighterInfos:GameContextActorInformations) -> None:
      infos:TmpFighterInfos = None
      carryingCharacterId:float = None
      fedi:FightEntityDispositionInformations = None
      carryingEntity:IEntity = None
      carriedEntity:IEntity = None
      hasCarryingModifier:bool = False
      carryingTs:TiphonSprite = None
      modifier:IAnimationModifier = None
      fighterId:float = fighterInfos.contextualId
      num:int = len(self._tempFighterList)
      i:int = 0
      while(i < num)
         infos = self._tempFighterList[i]
         carryingCharacterId = infos.carryingCharacterId
         if fighterId == carryingCharacterId:
            self._tempFighterList.splice(i,1)
            self.startCarryStep(carryingCharacterId,infos.contextualId)
         i += 1
      if isinstance(fighterInfos.disposition, FightEntityDispositionInformations):
         fedi = fighterInfos.disposition
         if fedi.carryingCharacterId:
            carryingEntity = DofusEntities.getEntity(fedi.carryingCharacterId)
            if not carryingEntity:
               self._tempFighterList.append(TmpFighterInfos(fighterInfos.contextualId,fedi.carryingCharacterId))
            else:
               carriedEntity = DofusEntities.getEntity(fighterInfos.contextualId)
               if carriedEntity:
                  hasCarryingModifier = False
                  if(carryingEntity
                     carryingTs = carryingEntity
                  else:
                     carryingTs = carryingEntity
                  if carryingTs:
                     carryingTs.removeAnimationModifierByClass(CustomBreedAnimationModifier)
                     for modifier in carryingTs.animationModifiers:
                        if isinstance(modifier, CarrierAnimationModifier):
                           hasCarryingModifier = True
                     if not hasCarryingModifier:
                        carryingTs.addAnimationModifier(CarrierAnimationModifier())
                  if not hasCarryingModifier or !(isinstance(carryingEntity, TiphonSprite) and isinstance(carriedEntity, TiphonSprite) and TiphonSprite(carriedEntity).parentSprite == carryingEntity):
                     self.startCarryStep(fedi.carryingCharacterId,fighterInfos.contextualId)
   
   def startCarryStep(self, fighterId:float, carriedId:float) -> None:
      step:FightCarryCharacterStep = FightCarryCharacterStep(fighterId,carriedId,-1,True)
      step.start()
      FightEventsHelper.sendAllFightEvent()
   
   def updateAllEntitiesfloat(self, ids:list[float]) -> None:
      id:float = None
      num:int = 1
      for id in ids:
         if self._entities[id] and self._entities[id].spawnInfo.alive:
            self.updateEntityfloat(id,num)
            num += 1
   
   def updateEntityfloat(self, id:float, num:int) -> None:
      number:Sprite = None
      lbl_number:Label = None
      ac:AnimatedCharacter = None
      if self._entities[id] and (not isinstance(self._entities[id], GameFightCharacterInformations) or GameFightCharacterInformations(self._entities[id]).spawnInfo.alive):
         if not self._entitiesfloat[id] or self._entitiesfloat[id] == None:
            number = Sprite()
            lbl_number = Label()
            lbl_number.width = 30
            lbl_number.height = 20
            lbl_number.x = -45
            lbl_number.y = -15
            lbl_number.css = Uri(XmlConfig().getEntry:("config.ui.skin") + "css/normal.css")
            lbl_number.text = str(num)
            number.addChild(lbl_number)
            number.filters = [GlowFilter(XmlConfig().getEntry:("colors.text.glow"),1,4,4,6,3)]
            self._entitiesfloat[id] = lbl_number
            ac = DofusEntities.getEntity(id)
            if ac:
               ac.addBackground("fighterfloat",number)
         else:
            self._entitiesfloat[id].text = str(num)
   
   def updateRemovedEntity(self, idEntity:float) -> None:
      num:int = 0
      fightBFrame:FightBattleFrame = None
      entId:float = None
      self._entitiesfloat[idEntity] = None
      if Dofus().options.getOption("orderFighters"):
         num = 1
         fightBFrame = Kernel().getWorker().getFrame(FightBattleFrame)
         for entId in fightBFrame.fightersList:
            if entId != idEntity and getEntityInfos(entId:
               self.updateEntityfloat(entId,num)
               num += 1
   
   def updateEntityIconPosition(self, pEntityId:float) -> None:
      tooltip:UiRootContainer = None
      bounds:IRectangle = None
      entity:AnimatedCharacter = DofusEntities.getEntity(pEntityId)
      if entity and entity.parent and entity.displayed and hasIcon(pEntityId):
         tooltip = Berilia().getUi("tooltip_tooltipOverEntity_" + pEntityId)
         bounds = not tooltip ? getIconEntityBoundsDofusEntities.getEntity(pEntityId) : Rectangle2(tooltip.x,tooltip.y,tooltip.width,tooltip.height)
         getIcon(pEntityId).place(bounds)
   
   def onPropertyChanged(self, e:PropertyChangeEvent) -> None:
      id = None
      ac:AnimatedCharacter = None
      num:int = 0
      fightBFrame:FightBattleFrame = None
      entId:float = None
      if not _worldPoint:
         _worldPoint = PlayedCharacterManager().currentMap
      if not _currentSubAreaId:
         _currentSubAreaId = PlayedCharacterManager().currentSubArea.id
      super().onPropertyChanged(e)
      if e.propertyName == "cellSelectionOnly":
         untargetableEntities = e.propertyValue or Kernel().getWorker().getFrame(FightPreparationFrame)
      elif e.propertyName == "orderFighters":
         if not e.propertyValue:
            for(id in self._entitiesfloat)
               if self._entitiesfloat[float(id)]:
                  self._entitiesfloat[float(id)] = None
                  ac = DofusEntities.getEntity(float(id))
                  if ac:
                     ac.removeBackground("fighterfloat")
         else:
            num = 1
            fightBFrame = Kernel().getWorker().getFrame(FightBattleFrame)
            if fightBFrame:
               for entId in fightBFrame.fightersList:
                  if getEntityInfos(entId:
                     self.updateEntityfloat(entId,num)
                     num += 1
      elif e.propertyName == "showMountsInFight":
         self.switchMountsVisibility(e.propertyValue)
   
   @cellSelectionOnly.setter
   def cellSelectionOnly(self, enabled:bool) -> None:
      infos:GameContextActorInformations = None
      entity:AnimatedCharacter = None
      for infos in self._entities:
         entity = DofusEntities.getEntity(infos.contextualId)
         if entity:
            entity.mouseEnabled = not enabled
   
   @property
   def dematerialization(self) -> bool:
      return _creaturesFightMode
   
   @property
   def lastKnownPlayerStatus(self) -> dict:
      return self._lastKnownPlayerStatus
   
   def getRealFighterLook(self, pFighterId:float) -> EntityLook:
      return self._realFightersLooks[pFighterId]
   
   def setRealFighterLook(self, pFighterId:float, pEntityLook:EntityLook) -> None:
      self._realFightersLooks[pFighterId] = pEntityLook
   
   @property
   def charactersMountsVisible(self) -> bool:
      return self._mountsVisible
   
   def getEntityTeamId(self, entityId:float) -> float:
      if !(entityId in self._entities) or not isinstance(self._entities[entityId], GameFightFighterInformations):
         return -1
      entitiesInfo:GameContextActorPositionInformations = self._entities[entityId]
      if isinstance(!(entitiesInfo, GameFightFighterInformations)):
         return -1
      return entitiesInfo.spawnInfo.teamId
   
   def getEntityIdsWithTeamId(self, teamId:float) -> list[float]:
      entityInfo:GameFightFighterInformations = None
      entityIds:list[float] = list[float](0)
      if teamId < 0:
         return entityIds
      for entityInfo in self._entities:
         if entityInfo is not None and entityInfo.spawnInfo.teamId == teamId:
            entityIds.append(entityInfo.contextualId)
      return entityIds
   
   def updateActorDisposition(self, actorId:float, newDisposition:EntityDispositionInformations) -> None:
      actor:IEntity = None
      super().updateActorDisposition(actorId,newDisposition)
      if newDisposition.cellId == -1:
         actor = DofusEntities.getEntity(actorId)
         if actor:
            FightEntitiesHolder().holdEntity(actor)
      else:
         FightEntitiesHolder().unholdEntity(actorId)
   
   def getTmpFighterInfoIndex(self, pId:float) -> float:
      infos:TmpFighterInfos = None
      for infos in self._tempFighterList:
         if infos.contextualId == pId:
            return self._tempFighterList.find(infos)
      return -1

class TmpFighterInfos:


contextualId:float

carryingCharacterId:float

def __init__(self, pId:float, pCarryindId:float):
   super().__init__()
   self.contextualId = pId
   self.carryingCharacterId = pCarryindId
