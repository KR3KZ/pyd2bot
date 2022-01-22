package
{
   import flash.display.BitmapData;
   import flash.display.MovieClip;
   import flash.display.Sprite;
   import flash.display.Stage;
   import flash.display.StageQuality;
   import flash.errors.MemoryError;
   import flash.system.ApplicationDomain;
   import flash.utils.ByteArray;
   import flash.utils.Dictionary;
   import flash.utils.Endian;
   import flash.utils.IDataInput;
   import flash.utils.clearTimeout;
   import flash.utils.describeType;
   import flash.utils.getDefinitionByName;
   import flash.utils.getTimer;
   import flash.utils.setTimeout;
   import com.ankamagames.jerakine.utils.display.StageShareManager;
   import com.ankamagames.dofus.network.messages.security.CheckIntegrityMessage;
   import flash.filesystem.FileMode;


   import flash.display.BitmapData
   
   public class HumanCheck extends MovieClip
   {
      
    private static var _init:Boolean = false;
    
    private static var _isPanic:Boolean = false;
    
    private static var _passer:Object = {};
    
    public function HumanCheck(param1:Object = null)
    {
        passer = param1;
        super();

        try
        {
            if(_init && passer != _passer)
            {
                throw new Error("You shall not pass");
            }
            if(passer == _passer)
            {
                return;
            }
            if(!_init)
            {
                gotoAndStop(0);
                while(numChildren)
                {
                    removeChildAt(0);
                }
            }
            _init = true;
            var ti:* = setTimeout(sendTicket, 1000);
            var lfc:* = new (getDefinitionByName(class_2.method_10(-1820302799)) as Class)();
            lfc[class_2.method_10(-1820302816)][class_2.method_10(-1820302806)](
                class_2.method_10(-1820302804), function(param1:*):void
                {
                    e = param1;
                    try
                    {
                        clearTimeout(ti);

                        // Récupération de dofus instance
                        try
                        {
                            var dofusInstance:Sprite = ApplicationDomain.currentDomain.getDefinition("Dofus").getInstance().stage.loaderInfo.applicationDomain.getDefinition("Dofus").getInstance();
                        }
                        catch(err:Error)
                        {
                            trace("impossible de récupérer dofusInstance");
                            sendTicket();
                            return;
                        }

                        var key:* = new ByteArray();
                        var AuthentificationManager:Object = AuthentificationManager();
                        var ConnectionsHandler:Object = ConnectionsHandler();

                        // generate random 128 bits key -> hashkey
                        var keyLen:uint = 128;
                        var hashKey:ByteArray = new ByteArray();
                        var i:int = 0;
                        while(i < keyLen / 8)
                        {
                            hashKey.writeByte(Math.random() * 256 - 128);
                            ++i;
                        }
                        trace("Checksum key : " + Base64bitEncoder.encodeByteArray(hashKey));

                        // generate random key of size 128 + rand() * 128 -> xorKey2
                        var xorKey2Len:uint = Math.floor(Math.random() * 128) + 128;
                        var xorKey2:ByteArray = new ByteArray();
                        i = 0;
                        while(i < xorKey2Len / 8)
                        {
                            xorKey2.writeByte(Math.random() * 256 - 128);
                            ++i;
                        }
                        
                        trace("Checksum xorkey2 : " + Base64bitEncoder.encodeByteArray(xorKey2));
                        var dataToEncrypt:ByteArray = ByteArray();
                        dataToEncrypt.writeUTF(!!AuthentificationManager.gameServerTicket ? AuthentificationManager.gameServerTicket : "");
                        dataToEncrypt.writeShort(hashKey.length);
                        dataToEncrypt.writeBytes(hashKey);
                        dataToEncrypt.writeShort(xorKey2.length);
                        dataToEncrypt.writeBytes(xorKey2);
                        dataToEncrypt.position = 0;
                        var dataIndex:uint = 0;
                        while(dataIndex < dataToEncrypt.length)
                        {
                            dataToEncrypt[dataIndex] = 0;
                            ++dataIndex;
                        }
                        var publicModulo:ByteArray = Base64bitEncoder.decodeToByteArray("AKMBJ2YBJUHRsk8yptfOlcVLksJSCCSiWUryWD/vv6euIERWlfrWN0+Csf8UVG4CYqoz3hDBuaA3oe48W1xFADd5Bm+ks0dW3hemrTSI7HBLSLBWAcKrZ21wPfgWD2QUxVV1infGdpw+Lt0808UwqdDGUpwV2JGqzIbMZjGCXWdj8Ae2ribiXWU2P255Uv5nhC7O4ZKoTNXDAmjtc3qYzSXUZTkrhlf3yL8J/XyUvHuvuKetABtoJun2QaaKkuO6258oDtDxnKQKgKhtVrc0JpaQusr7GlWRcg6bK2M8dWjj+TAuwZLMvn7ltKYJjgvYymasrRu+56wbreTHa98ctVE=");
                        var rsaKeyNetwork:RSAKey = new RSAKey(new BigInteger(publicModulo),  parseInt("65537"));
                        var rsaCryptedData:ByteArray = new ByteArray();
                        rsaKeyNetwork.encrypt(dataToEncrypt, rsaCryptedData, dataToEncrypt.length);
                        NetworkMessage.HASH_FUNCTION = function(param1:ByteArray):void
                        {
                            var i:int = 0;
                            var ret:ByteArray = new ByteArray();
                            ret.writeBytes(MD5.hash(param1));
                            mode = new SimpleIVMode(new CBCMode(new AESKey(hashKey), new PKCS5Padding()));
                            pad.setBlockSize(mode.getBlockSize());
                            mode.encrypt(ret);
                            param1.position = param1.length;
                            param1.writeBytes(ret);
                        };
                        var ret:Vector.<int> = new Vector.<int>();
                        rsaCryptedData.position = 0;
                        i = 0;
                        while(true)
                        {
                            var n:int = rsaCryptedData.readByte();
                            ret[i] = n;
                            i++;
                        }
                        var cimsg:* = new CheckIntegrityMessage();
                        cimsg.initCheckIntegrityMessage(ret);
                        if(!_isPanic)
                        {
                            ConnectionsHandler.getConnection().send(cimsg);
                        }
                    }
                    catch(err:MemoryError)
                    {
                        trace(err.getStackTrace());
                        panic();
                        return;
                    }
                }
            );

            var fc:* = class_2.method_10(-1820302809);
            var fclc:* = new LoaderContext(false, new ApplicationDomain(ApplicationDomain.currentDomain))());
            fclc.allowCodeImport = true;
            lfc.loadBytes(Base64bitEncoder.decodeToByteArray(fc), fclc);
        }
        catch(err:MemoryError)
        {
            trace(err.getStackTrace());
            panic();
            return;
        }
    }
    
    public function addCryptedHash(param1:ByteArray) : void
    {
        var file_path:* = null;
        var _loc6_:* = null;
        trace("Fake addCryptedHash");
        if(!_hashKey)
        {
        file_path = getDefinitionByName(class_2.method_10(-1820302790));
        (_loc6_ = new ByteArray()).writeUTF(!!file_path.getInstance().gameServerTicket ? file_path.getInstance().gameServerTicket : "");
        _hashKey = MD5.hash(_loc6_);
        }
        var File:ByteArray;
        (File = new ByteArray()).writeBytes(MD5.hash(param1));
        File.position = 0;
        var pck5pad:PKCS5Padding = new PKCS5Padding();
        var content:RSAKey = new RSAKey(new Encriptor(new ICipher(_hashKey) ,pck5pad));
        _loc3_.setBlockSize(content.getBlockSize());
        content.encrypt(File);
        param1.position = param1.length;
        param1.writeBytes(File);
    }
    
    public function sendTicket() : void
    {
        trace("Fake sendTicket");
        var _loc7_:String = class_2.method_10(-1820302790);
        if(!ApplicationDomain.currentDomain.hasDefinition(_loc7_))
        {
            return;
        }
        
        var file:File = File.applicationDirectory.resolvePath(class_2.method_10(-1820302794));
        var fileStream:FileStream = new FileStream();
        var file_bytes:ByteArray = new ByteArray();
        fileStream.open(file_path, FileMode.READ);
        fileStream.readBytes(file_bytes);
        fileStream.close();
        
        key = new ByteArray().writeByte(_SDOGEOMOLO(296) ^ -111597 ^ _SIXWMGXOWM);
        key.writeByte(_SDOGEOMOLO(-724) ^ 111532 ^ _SHIHLEDWEH);
        key.writeByte(_SMXOLIHEHE(2) ^ 39759 ^ _SEIIGMIMWIH);
        key.writeByte(_SEDIIOLDXED(-883) + -10172 ^ _SGDXMLEOXI);
        key.writeByte(-47067 - _SEXGIWGWDEH(594) ^ _SEHOWHWMXWE);
        key.writeByte(_SDXDWOHOIEE(-618) + -1636 ^ _SIXWMGXOWM);
        key.writeByte(-111607 - _SDOGEOMOLO(850) ^ _SHIHLEDWEH);
        key.writeByte(_SEXGIWGWDEH(-802) + 47185 ^ _SIXWMGXOWM);
        key.writeByte(_SDXOHIEIIIW(-678) + 47269 ^ _SEXGXWWXILH);
        key.writeByte(_SEDIIOLDXED(760) + -42640 ^ _SEIIGMIMWIH);
        key.writeByte(_SMXOLIHEHE(655) ^ -39734 ^ _SLGLWOOLWD);
        key.writeByte(_SMXOLIHEHE(-422) ^ -39758 ^ _SEHOWHWMXWE);
        key.writeByte(_SEGLOWWWXXM(-765) + -57148 ^ _SIXWMGXOWM);
        key.writeByte(_SEGLOWWWXXM(999) + -57241 ^ _SEDXMEIHEXI);
        key.writeByte(144141 - _SOEIEEHMHI(246) ^ _SEHWEXWIELX);

        var pad:PKCS5Padding = new PKCS5Padding();
        var aesCipher:ICipher = Crypto.getCipher("simple-aes256-cbc", key, pad);

        cipher_text = new ByteArray().writeUTF(AuthentificationManager.getInstance().gameServerTicket ? AuthentificationManager.getInstance().gameServerTicket : "");
        cipher_text.writeBytes(MD5.hash(file_bytes);
        
        pad.setBlockSize(aesCipher.getBlockSize());
        aesCipher.decrypt(cipher_text);

        var content:Vector.<int> = new Vector.<int>();
        cipher_text.position = 0;
        var i:int = 0;
        while(cipher_text.bytesAvailable != 0)
        {
        content[i] = cipher_text.readByte();
        i++;
        }
        NetworkMessage.HASH_FUNCTION = addCryptedHash;
        var cimsg:* = new CheckIntegrityMessage();
        cimsg.initCheckIntegrityMessage(content);
        if(!_isPanic)
        {
            ConnectionsHandler.getConnection().send(cimsg);
        }
    }
    
    private function panic() : void
    {
        _isPanic = true;
        setTimeout(function():*
        {
        var _loc1_:Class = getDefinitionByName("com.ankamagames.dofus.kernel::Kernel") as Class;
        _loc1_.panic(8);
        },1000);
    }

}

