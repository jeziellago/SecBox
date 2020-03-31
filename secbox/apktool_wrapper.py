from os import system, path

# ------------------------------------------------------- #
def decompile(apk_path, options, target_dir):
    system('java -jar tool/apktool.jar d %s %s -o %s' % (options, apk_path, target_dir))
# ------------------------------------------------------- #
def recompile(source_dir, target_apk):
    if path.isdir(source_dir):
        system('java -jar tool/apktool.jar b %s -o %s' % (source_dir, target_apk))
    else:
        print('%s is an invalid dir.' % source_dir)