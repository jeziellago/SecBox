from os import system, path


def decompile(apk_path, options, target_dir):
    command_template = 'java -jar tool/apktool.jar d %s %s -o %s --use-aapt2'
    proc = system(command_template % (options, apk_path, target_dir))
    return proc == 0

def recompile(source_dir, target_apk):
    command_template = 'java -jar tool/apktool.jar b %s -o %s --use-aapt2'
    proc = system(command_template % (source_dir, target_apk))
    return proc == 0
    