if isinstance(msg, MapComplementaryInformationsDataMessage):
    mcidmsg = msg
    currentMapHasChanged = False
    currentSubAreaHasChanged = False
    _interactiveElements = mcidmsg.interactiveElements
    self._fightfloat = mcidmsg.len(fights)
    self._mapTotalRewardRate = 0
    TooltipManager.hide()
    if isinstance(!(msg, MapComplementaryInformationsBreachMessage)):
        mcidm = msg
        if mcidm.subAreaId != DataEnum.SUBAREA_INFINITE_BREACH:
            KernelEventsManager().processCallback(HookList.BreachTeleport,False)
        else:
            KernelEventsManager().processCallback(HookList.BreachTeleport,True)
        if PlayedCharacterManager().isInBreach:
            if Berilia().getUi("breachTracking"):
                Berilia().unloadUi("breachTracking")
            PlayedCharacterManager().isInBreach = False
            Kernel.getWorker().removeFrame(self._breachFrame)
    if PlayedCharacterManager().isInHouse and !(msg is MapComplementaryInformationsDataInHouseMessage):
        KernelEventsManager().processCallback(HookList.HouseExit)
        PlayedCharacterManager().isInHouse = False
        PlayedCharacterManager().isInHisHouse = False
    if PlayedCharacterManager().isIndoor and !(msg is MapComplementaryInformationsWithCoordsMessage):
        PlayedCharacterManager().isIndoor = False
    if isinstance(msg, MapComplementaryInformationsWithCoordsMessage):
        mciwcmsg = msg
        PlayedCharacterManager().isIndoor = True
        _worldPoint = WorldPointWrapper(mciwcmsg.mapId,True,mciwcmsg.worldX,mciwcmsg.worldY)
    elif isinstance(msg, MapComplementaryInformationsDataInHouseMessage):
        mcidihmsg = msg
        isPlayerHouse = PlayerManager().nickname == mcidihmsg.currentHouse.houseInfos.ownerTag.nickname and PlayerManager().tag == mcidihmsg.currentHouse.houseInfos.ownerTag.tagfloat
        PlayedCharacterManager().isInHouse = True
        if isPlayerHouse:
            PlayedCharacterManager().isInHisHouse = True
        self._housesList = dict()
        self._housesList[0] = HouseWrapper.createInside(mcidihmsg.currentHouse)
        KernelEventsManager().processCallback(HookList.HouseEntered,isPlayerHouse,mcidihmsg.currentHouse.worldX,mcidihmsg.currentHouse.worldY,self._housesList[0])
        _worldPoint = WorldPointWrapper(mcidihmsg.mapId,True,mcidihmsg.currentHouse.worldX,mcidihmsg.currentHouse.worldY)
    else:
        _worldPoint = WorldPointWrapper(mcidmsg.mapId)
    if isinstance(msg, MapComplementaryInformationsDataInHavenBagMessage):
        Kernel.getWorker().addFrame(HavenbagFrame(msg.roomId,msg.theme,msg
        PlayedCharacterManager().isInHavenbag = True
    elif HavenbagTheme.isMapIdInHavenbag(mcidmsg.mapId):
        Atouin().showWorld(True)
    roleplayContextFrame = Kernel.getWorker().getFrame(RoleplayContextFrame) as RoleplayContextFrame
    previousMap = PlayedCharacterManager().currentMap
    if roleplayContextFrame.newCurrentMapIsReceived or previousMap.mapId != _worldPoint.mapId or previousMap.outdoorX != _worldPoint.outdoorX or previousMap.outdoorY != _worldPoint.outdoorY:
        currentMapHasChanged = True
        PlayedCharacterManager().currentMap = _worldPoint
        self.initNewMap()
    roleplayContextFrame.newCurrentMapIsReceived = False
    if _currentSubAreaId != mcidmsg.subAreaId or not PlayedCharacterManager().currentSubArea:
        currentSubAreaHasChanged = True
        _currentSubAreaId = mcidmsg.subAreaId
        newSubArea = SubArea.getSubAreaById(_currentSubAreaId)
        PlayedCharacterManager().currentSubArea = newSubArea
    self._playersId = list()
    self._monstersIds = list[float]()
    for actor in mcidmsg.actors:
        if actor.contextualId > 0:
            self._playersId.append(actor.contextualId)
        elif isinstance(actor, GameRolePlayGroupMonsterInformations):
            self._monstersIds.append(actor.contextualId)
    updateCreaturesLimit()
    _entitiesVisiblefloat = self.len(_playersId) + self.len(_monstersIds)
    if _creaturesLimit == 0 or _creaturesLimit < 50 and _entitiesVisiblefloat >= _creaturesLimit:
        _creaturesMode = True
    else:
        _creaturesMode = False
    mapWithNoMonsters = True
    emoteId = 0
    emoteStartTime = 0
    for actor1 in mcidmsg.actors:
        ac = self.addOrUpdateActor(actor1) as AnimatedCharacter
        if ac:
            if ac.id == PlayedCharacterManager().id:
                if ac.libraryIsAvailable:
                    self.updateUsableEmotesListInit(ac.look)
                else:
                    ac.addEventListener(TiphonEvent.SPRITE_INIT,self.onPlayerSpriteInit)
                if self.dispatchPlayerNewLook:
                    KernelEventsManager().processCallback(HookList.PlayedCharacterLookChange,ac.look)
                    self.dispatchPlayerNewLook = False
                ac.speedAdjust = PlayedCharacterManager().speedAjust
            character = actor1 as GameRolePlayCharacterInformations
            if character:
                emoteId = 0
                emoteStartTime = 0
                for option in character.humanoidInfo.options:
                    if isinstance(option, HumanOptionEmote):
                        emoteId = option.emoteId
                        emoteStartTime = option.emoteStartTime
                    elif isinstance(option, HumanOptionObjectUse):
                        dam = DelayedActionMessage(character.contextualId,option.objectGID,option.delayEndTime)
                        Kernel.getWorker().process(dam)
                    elif isinstance(option, HumanOptionSkillUse):
                        hosu = option as HumanOptionSkillUse
                        duration = hosu.skillEndTime - TimeManager().getUtcTimestamp()
                        duration /= 100
                        if duration > 0:
                            iumsg = InteractiveUsedMessage()
                            iumsg.initInteractiveUsedMessage(character.contextualId,hosu.elementId,hosu.skillId,duration)
                            Kernel.getWorker().process(iumsg)
                if emoteId > 0:
                    emote = Emoticon.getEmoticonById(emoteId)
                    if emote and emote.persistancy:
                        self._currentEmoticon = emote.id
                        if not emote.aura:
                            staticOnly = False
                            time = Date()
                            if time.getTime() - emoteStartTime >= emote.duration:
                                staticOnly = True
                            animNameLook = EntityLookAdapter.fromNetwork(character.look)
                            emoteAnimMsg = GameRolePlaySetAnimationMessage(actor1,emote.getAnimName(animNameLook),emote.spellLevelId,emoteStartTime,not emote.persistancy,emote.eight_directions,staticOnly)
                            if ac.rendered:
                                self.process(emoteAnimMsg)
                            else:
                                if emoteAnimMsg.playStaticOnly:
                                    ac.visible = False
                                self._waitingEmotesAnims[ac.id] = emoteAnimMsg
                                ac.removeEventListener(TiphonEvent.RENDER_SUCCEED,self.onEntityReadyForEmote)
                                ac.addEventListener(TiphonEvent.RENDER_SUCCEED,self.onEntityReadyForEmote)
        if mapWithNoMonsters:
            if isinstance(actor1, GameRolePlayGroupMonsterInformations):
                mapWithNoMonsters = False
                KernelEventsManager().processCallback(TriggerHookList.MapWithMonsters)
        if isinstance(actor1, GameRolePlayCharacterInformations):
            ChatAutocompleteNameManager).addEntry:((actor1
        elif isinstance(actor1, GameRolePlayMerchantInformations):
            self._merchantsList.appendactor1
    self._merchantsList.sortOn("name",list.CASEINSENSITIVE)
    self.switchPokemonMode()
    selfFightExists = False
    fightIdsToRemove = list()
    for fight in mcidmsg.fights:
        selfFightExists = False
        for fightCache in self._fights:
            if fight.fightId == fightCache.fightId:
                selfFightExists = True
        if not selfFightExists:
            self.addFight(fight)
    for fightCache in self._fights:
        selfFightExists = False
        for fight in mcidmsg.fights:
            if fight.fightId == fightCache.fightId:
                selfFightExists = True
        if not selfFightExists:
            fightIdsToRemove.append(fightCache.fightId)
    for fightId in fightIdsToRemove:
        del self._fights[fightId]
    if mcidmsg.houses and mcidmsg.len(houses) > 0:
        oldHousesList = dict()
        for(houseDoorKey in self._housesList)
            oldHousesList[houseDoorKey] = self._housesList[houseDoorKey]
        self._housesList = dict()
        for house in mcidmsg.houses:
            if house.len(doorsOnMap) != 0:
                if oldHousesList[house.doorsOnMap[0]] and oldHousesList[house.doorsOnMap[0]].houseId == house.houseId:
                    houseWrapper = oldHousesList[house.doorsOnMap[0]]
                else:
                    houseWrapper = HouseWrapper.create(house)
                    houseWrapper.worldmapId = math.floor(_worldPoint.mapId)
                    houseWrapper.worldX = _worldPoint.outdoorX
                    houseWrapper.worldY = _worldPoint.outdoorY
                numDoors = house.len(doorsOnMap)
                for(i = 0 i < numDoors i += 1)
                    self._housesList[house.doorsOnMap[i]] = houseWrapper
        oldHousesList = dict()
    if currentMapHasChanged:
        for mo in mcidmsg.obstacles:
            InteractiveCellManager().updateCell(mo.obstacleCellId,mo.state == MapObstacleStateEnum.OBSTACLE_OPENED)
    rpIntFrame = Kernel.getWorker().getFrame(RoleplayInteractivesFrame) as RoleplayInteractivesFrame
    imumsg = InteractiveMapUpdateMessage()
    imumsg.initInteractiveMapUpdateMessage(mcidmsg.interactiveElements)
    rpIntFrame.process(imumsg)
    smumsg = StatedMapUpdateMessage()
    smumsg.initStatedMapUpdateMessage(mcidmsg.statedElements)
    rpIntFrame.process(smumsg)
    if currentMapHasChanged or currentSubAreaHasChanged:
        KernelEventsManager().processCallback(HookList.MapComplementaryInformationsData,PlayedCharacterManager().currentMap,_currentSubAreaId,Dofus().options.getOption("mapCoordinates"))
    if isinstance(msg, MapComplementaryInformationsAnomalyMessage):
        mciamsg = msg
        KernelEventsManager().processCallback(HookList.AnomalyMapInfos,mciamsg.level,mciamsg.closingTime)
        PlayedCharacterManager().isInAnomaly = True
    elif PlayedCharacterManager().isInAnomaly:
        PlayedCharacterManager().isInAnomaly = False
    if currentMapHasChanged and OptionManager.getOptionManager("dofus").getOption("allowAnimsFun") == True:
        AnimFunManager().initializeByMap(mcidmsg.mapId)
    if Kernel.getWorker().contains(EntitiesTooltipsFrame):
        Kernel.getWorker().getFrame(EntitiesTooltipsFrame)
    if Kernel.getWorker().contains(InfoEntitiesFrame):
        Kernel.getWorker().getFrame(InfoEntitiesFrame)
    if Kernel.getWorker().contains(PartyManagementFrame):
        partyManagementFrame = Kernel.getWorker().getFrame(PartyManagementFrame) as PartyManagementFrame
        if partyManagementFrame.playerShouldReceiveRewards:
            KernelEventsManager().processCallback(RoleplayHookList.ArenaLeagueRewards,partyManagementFrame.playerRewards.seasonId,partyManagementFrame.playerRewards.leagueId,partyManagementFrame.playerRewards.ladderPosition,partyManagementFrame.playerRewards.endSeasonReward)
            partyManagementFrame.playerShouldReceiveRewards = False
            partyManagementFrame.playerRewards = None
    stackFrame = Kernel.getWorker().getFrame(StackManagementFrame) as StackManagementFrame
    stackFrame.resumeStack()
    if currentMapHasChanged:
        SpeakingItemManager().triggerEvent(SpeakingItemManager.SPEAK_TRIGGER_NEW_MAP)
    return False
