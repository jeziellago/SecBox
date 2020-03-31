import os 
import sys

'''
HOW IT WORKS?

$ python sign_app.py MyApp.apk

'''
APK_PATH=sys.argv[1]

os.system(
    'jarsigner -verbose -sigalg SHA1withRSA -storepass android \
    -digestalg SHA1 -keystore key.keystore %s androiddebugkey ' % APK_PATH
)