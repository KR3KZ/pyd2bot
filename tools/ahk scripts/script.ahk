#NoEnv 
#Warn 
SendMode Input 
SetWorkingDir %A_ScriptDir% 

#SingleInstance force 

#Persistent 

settimer start1, 0 

return

start1:

if !GetKeyState("capslock","T") 

 {

 tooltip 

 }
 else
 { 

 CoordMode, Mouse, Screen ; makes mouse coordinates to be relative to screen.

 MouseGetPos xx, yy ; get mouse x and y position, store as %xx% and %yy%

 F1::FileAppend,0`,%xx%`,%yy%`n,%A_ScriptDir%\Test.txt
 F2::FileAppend,1`,%xx%`,%yy%`n,%A_ScriptDir%\Test.txt
 F3::FileAppend,2`,%xx%`,%yy%`n,%A_ScriptDir%\Test.txt
 F4::FileAppend,3`,%xx%`,%yy%`n,%A_ScriptDir%\Test.txt
 F5::FileAppend,*`,%xx%`,%yy%`n,%A_ScriptDir%\Test.txt
 return

 }

return

Esc::ExitApp