# pyd2bot
Un bot dofus 2 en full socket entièrement en python.

## Setup DEV Env

### Install node js

Install node js. It's needed to run the simulated launcher.
Install make if you are under Windows. In windows i reccommend using git bash.

### Setup dev env

`make setup`

### Fetch data from Dofus Invoker(protocol, keys, version, msgClasses)

`make update`

> :warning: This process takes quite some time.

## Create bot data (account and creds)

### Create rsa keys to encrypt your account credentials

Crate a folder outside the repository for example `C:/my_passEnc_keys`. Add a new env variable to your env pointing to this folder you just created. Name this variable `PASS_ENC_KEYS`. Don't make an error in the variable name because the launcher searches for it in the env to find the key used to encrypt your passwords before saving them.
Then run :

`make genKeys`

> :warning: You may have to restart your terminal for the new variable to be added to env.

### Create an entry for your bot credentials

Example:

`make createAccount entryName=grinder login="myAccountAwsomeLogin" password='keepThisOneSafe'`

> :warning: Make sure to put the password inside single quotes to avoid having problems with special chars.

### Create an entry for the bot charachter infos

Example:

`make createBot botName='myBotName' account='grinder' charachterId=290210840786 serverId=210`

Here 'account' arg should correspond to the entryName you chose for your account creds.

> :warning: If you don't know how to get your server ID and character Id. Start the sniffer 'make startSniffer', go to page localhost:8888 and login manually. Then look for serverSelectionMessage.

### Launch the bot

`make test bot='myBotName'`
