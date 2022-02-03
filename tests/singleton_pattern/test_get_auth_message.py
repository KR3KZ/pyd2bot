from com.ankamagames.dofus.logic.common.managers.AuthentificationManager import AuthentificationManager

key = 
AuthentificationManager().setPublicKey(hcmsg.key)
AuthentificationManager().setSalt(hcmsg.salt)
AuthentificationManager().initAESKey()
iMsg = AuthentificationManager().getIdentificationMessage()