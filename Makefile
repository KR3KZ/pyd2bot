DOFUSINVOKER = $(LOCALAPPDATA)/Ankama/Dofus/DofusInvoker.swf
FFDEC = $(CURDIR)/FFDec/ffdec.bat
DOFUS_SRC = $(CURDIR)/protocolBuilder/sources
SELECTCLASS = com.ankamagames.dofus.BuildInfos,com.ankamagames.dofus.network.++,com.ankamagames.jerakine.network.++
KEYS_DIR = $(CURDIR)/binaryData

setup:
	@python ./setup.py

update: decompile gen-protocol gen-msgClasses gen-msgShuffle extract-keys unpack-maps

decompile:
	@$(FFDEC) -config parallelSpeedUp=true -selectclass $(SELECTCLASS) -export script $(DOFUS_SRC) $(DOFUSINVOKER)

extract-keys:
	@$(FFDEC) -config parallelSpeedUp=true -export binaryData $(KEYS_DIR) $(DOFUSINVOKER)
	
gen-protocol:
	@python protocolBuilder/protocolParser.py $(DOFUS_SRC)

gen-msgClasses:
	@python protocolBuilder/exportClasses.py

gen-msgShuffle:
	@python protocolBuilder/extractMsgShuffle.py $(DOFUS_SRC)/scripts/com/ankamagames/dofus/network/MessageReceiver.as

unpack-maps:
	@python scripts/unpack_maps.py $(DOFUS_SRC)

deps:
	@pip install -r requirements.txt

startSniffer:
	@python -m snifferApp 

venvActivate:
	shell source $(CURDIR)/.venv/Scripts/activate

createAccount:
	@python $(CURDIR)/hackedLauncher/CredsManager.py $(entryName) $(login) $(password)

createBot:
	@python $(CURDIR)/pyd2bot/BotsDataManager.py $(botName) $(account) $(serverId) $(charachterId)

genKeys:
	@ssh-keygen -t rsa -b 2056 -m PEM -f $(PASS_ENC_KEYS)/id_rsa

test:
	@python $(CURDIR)/pyd2bot/main.py $(botName)

