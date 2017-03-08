# cmdYi
Yi 4k commandline controller for PC  

Windows executable: [cmdYi.zip](https://github.com/NikolayRag/cmdYi/releases/download/v1.3/cmdYi.exe)


Using this tool you can:


### Get camera settings
Example: `-getSettings`, `-getBuzzerVolume` and so on flags, refered to API names.  
You can shorten flags up any unamiguous abbriviation like `-getSe` or `-getB`.


### Set camera settings
Example: `-setB(uzzerVolume)` [index]
Where index is a number, refered to command-related value. Run tool without arguments to see all value lists.
The only exception so far is `setDateTime` which have `"yyyy-MM-dd HH:mm:ss"` value format. Notice quotes you should use.


### Make video or photo
The flags are '-capturePhoto', '-startRecording' and '-stopRecording'.  
Successfull '-capturePhoto' and '-stopRecording' should return recorded file name.
While recording you will be unable to set settings.


### Listen to camera events
Using `-listen` flag, controller will print any camera event, which is battery ammount, settings changed and so on.
You should press Enter to stop controller.
In addition, running `-listen` will switch viewfinder on, making available RTSP preview at `rtsp://192.168.42.1/live`.
