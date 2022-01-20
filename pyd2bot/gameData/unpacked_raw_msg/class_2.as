package
{
   import flash.display.Sprite;
   import flash.utils.ByteArray;
   import flash.utils.Endian;
   
   public class class_2 extends Sprite
   {
      
      private static var var_1:Class = class_4;
      
      private static var var_6:Class = class_6;
      
      private static var var_5:Class = class_3;
      
      private static var var_8:Array = new Array();
      
      private static var var_2:Array = new Array();
      
      private static var var_10:Boolean = false;
      
      private static var var_7:int;
       
      
      public function class_2()
      {
         super();
      }
      
      private static function method_1() : void
      {
         var _loc1_:ByteArray = new var_1() as ByteArray;
         var _loc2_:ByteArray = new var_6() as ByteArray;
         var _loc3_:ByteArray = new var_5() as ByteArray;
         _loc3_.endian = Endian.LITTLE_ENDIAN;
         var_7 = _loc3_.readInt();
         var _loc4_:int = _loc2_.readByte();
         var _loc5_:int = 0;
         while(_loc5_ < _loc4_)
         {
            method_6(_loc2_);
            _loc5_++;
         }
         _loc4_ = _loc1_.readInt();
         var _loc6_:int = 0;
         while(_loc6_ < _loc4_)
         {
            method_4(_loc1_,var_2[_loc6_ % 0]);
            _loc6_++;
         }
         var_10 = true;
      }
      
      private static function method_4(param1:ByteArray, param2:ByteArray) : void
      {
         var _loc3_:int = param1.readInt();
         var _loc4_:ByteArray = new ByteArray();
         param1.readBytes(_loc4_,0,_loc3_);
         var _loc5_:class_5;
         (_loc5_ = new class_5(param2)).method_7(_loc4_);
         _loc4_.position = 0;
         var_8.push(_loc4_.readUTFBytes(_loc4_.length));
      }
      
      private static function method_6(param1:ByteArray) : void
      {
         var _loc2_:ByteArray = new ByteArray();
         param1.readBytes(_loc2_,0,16);
         _loc2_.position = 0;
         var_2.push(_loc2_);
      }
      
      public static function method_10(param1:int) : String
      {
         if(!var_10)
         {
            method_1();
         }
         return var_8[param1 ^ var_7];
      }
   }
}
