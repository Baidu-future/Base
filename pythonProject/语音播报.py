# coding: utf-8
import   pyttsx3
import  time

# 初始化
pt = pyttsx3.init()
# 说什么
pt.say("用户可以在程序－常用工具－磁盘工具里面创建dmg文件，大小自定义。可以用来放程序，打包文件，或用来做一个限定容量的路径。然后可以对这个磁盘进行其他操作，如用TOAST刻录。pyobjc-framework-OSAKit-5.3 pyobjc-framework-OpenDirectory-5.3 pyobjc-framework-Photos-5.3 pyobjc-framework-PhotosUI-5.3 pyobjc-framework-PreferencePanes-5.3 pyobjc-framework-PubSub-5.3 pyobjc-framework-QTKit-5.3 pyobjc-framework-Quartz-5.3 pyobjc-framework-SafariServices-5.3 pyobjc-framework-SceneKit-5.3 pyobjc-framework-ScreenSaver-5.3 pyobjc-framework-ScriptingBridge-5.3 pyobjc-framework-SearchKit-5.3 pyobjc-framework-Security-5.3 pyobjc-framework-SecurityFoundation-5.3 pyobjc-framework-SecurityInterface-5.3 pyobjc-framework-ServiceManagement-5.3 pyobjc-framework-Social-5.3 pyobjc-framework-SpriteKit-5.3 pyobjc-framework-StoreKit-5.3")
# 开始说吧
pt.runAndWait()

time.sleep(5)
pt.say("张大嘴")
pt.runAndWait()

time.sleep(5)
pt.say("眨眼睛")
pt.runAndWait()

time.sleep(2)
pt.say("语音播报完成")
pt.runAndWait()

print('————————————————————语音播报完成————————————————————————')