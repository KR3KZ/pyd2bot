# pyd2bot

## Setup DEV Env

### Install node js

Install node js. It's needed to run the simulated launcher.

### Make fresh new venv

`python3 -m venv .venv`

### Add the project sources to the python site-packages

`make setup`
!!! If make is not recognised as a command, look how to install make for windows if you are under windows like me.)

### Install dependencies

`make deps`

### Fetch data from Dofus Invoker(protocol, keys, version, msgClasses)

make update
!!! This process takes quite some time.

## Create bot data (account and creds)

### Create rsa keys to encrypt your account credentials

Crate a folder outside the repository for example c:/my_passEnc_keys
then add that folder to your environment variables under a vraiable named 'PASS_ENC_KEYS'. Don't make an error in the var name.
Then run :
`make genRsaKeyPair dst-dir=$PASS_ENC_KEYS`
!!! You may have to restart your terminal for the new variable to be added to env.

### Create an entry for your bot credentials

Example:
`make createAccount entryName=grinder login="myAccountAwsomeLogin" password='keepThisOneSafe'`
!!! Make sure to put the password inside single quotes to avoid having problems with special chars.

### Create an entry for the bot charachter infos

Example:
`make createBot botName='myBotName' account='grinder' charachterId=290210840786 serverId=210`

Here 'account' arg should correspond to the entryName you chose for your account creds.

!!! If you don't know how to get your server ID and character Id. Start the sniffer 'make startSniffer', go to page localhost:8888 and login manually. Then look for serverSelectionMessage.

### Launch the bot

`make test botName='myBotName'`
