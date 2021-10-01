dim speechobject
set speechobject=createobject("sapi.spvoice")
Set speechobject.Voice = speechobject.GetVoices.Item(1)
speechobject.Volume = 100
speechobject.speak "Enter Input Folder Path"