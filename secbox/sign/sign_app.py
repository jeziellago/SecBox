from os import system 


def sign_apk(apk_path):
    proc = system(
        'jarsigner -verbose -sigalg SHA1withRSA -storepass android \
        -digestalg SHA1 -keystore sign/key.keystore %s androiddebugkey ' % apk_path
    )
    return proc == 0