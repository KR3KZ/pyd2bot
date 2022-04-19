DOFUSINVOKER = $(LOCALAPPDATA)/Ankama/Dofus/DofusInvoker.swf
FFDEC = $(CURDIR)/FFDec/ffdec.bat
DOFUS_SRC = $(CURDIR)/protocolBuilder/sources
SELECTCLASS = com.ankamagames.dofus.BuildInfos,com.ankamagames.dofus.network.++,com.ankamagames.jerakine.network.++
KEYS_DIR = $(CURDIR)/binaryData

setup:
	@python ./setup.py

update: decompile gen-protocol gen-msgClasses gen-msgShuffle extract-keys

decompile:
	@$(FFDEC) -config parallelSpeedUp=false -selectclass $(SELECTCLASS) -export script $(DOFUS_SRC) $(DOFUSINVOKER)

extract-keys:
	@$(FFDEC) -config parallelSpeedUp=true -export binaryData $(KEYS_DIR) $(DOFUSINVOKER)
	
gen-protocol:
	@python protocolBuilder/protocolParser.py $(DOFUS_SRC)

gen-msgClasses:
	@python protocolBuilder/exportClasses.py

gen-msgShuffle:
	@python protocolBuilder/extractMsgShuffle.py $(DOFUS_SRC)/scripts/com/ankamagames/dofus/network/MessageReceiver.as

deps:
	@pip install -r requirements.txt

startSniffer:
	@python3 -m snifferApp 

venvActivate:
	@$(CURDIR)/.venv/Scripts/activate.ps1

createAccount:
	@python3 $(CURDIR)/hackedLauncher/CredsManager.py $(entryName) $(login) $(password)

createBot:
	@python3 $(CURDIR)/pyd2bot/BotsDataManager.py $(botName) $(account) $(serverId) $(charachterId)

genRsaKeyPair:
	@ssh-keygen -t rsa -b 2056 -m PEM -f $(dst-dir)/id_rsa

test:
	@python $(CURDIR)/pyd2bot/main.py $(botName)
