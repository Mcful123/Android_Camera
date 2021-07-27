# Connecting phone to computer 
To connect an Android phone to a computer, 'USB-debugging' must be turned on in settings on the phone. Go to settings->About phone->Software information. Tap 'Build number' 7 times to turn on 'Developer options'. Turn on USB-debugging in settings->Developer options->USB-debugging. <br />

Setting the phone to do not disturb prevents random notifications from interfering with the touch inputs. Also, in the camera app settings->shooting methods-> Press Volume key to -> set to zoom for a consistent way to remotely zoom in and out<br />

Android Debug Bridge (ADB) <br />
For Windows PC: The adb.exe, AdbWinApi.dll, and AdbWinUsbApi.dll from supporting files-windows must be placed in the working directory <br />
For Linux: The adb file must be placed in the working directory <br />

The first time a phone is connected to a new computer, the phone will ask for confirmation to connect. <br />

# SCRCPY 
scrcpy (the rest of the files in the supporting files-windows except the 3 'ADB' files) is used for streaming the phone screen to the computer. Mouse and keyboard can be used on the app for touch and keyboard inputs. 

# adb 
for full commands: https://developer.android.com/studio/command-line/adb <br />
on Windows: send commands with "os.system('adb ...')" <br />
on Linux: send commands with "os.system('./adb ...')" <br />

sending touch inputs: ('adb shell input tap x-coord y-coord')
sending swipe inputs: ('adb shell input touchscreen swipe x1 y1 x2 y2 duration') <- duration is in milliseconds 
sending keyevents: ('adb shell input keyevent ___ ') for full KEYCODES: https://developer.android.com/reference/android/view/KeyEvent

