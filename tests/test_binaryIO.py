from com.ankamagames.jerakine.network.CustomDataWrapper import ByteArray


a = ByteArray(333) 

x = a[0:1]
y = a[1:]
assert x + y == a