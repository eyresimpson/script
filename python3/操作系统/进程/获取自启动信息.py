import subprocess
import chardet as chardet


def get_autorun_info():
    result = subprocess.run("wmic startup get caption, command, location", shell=True, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    encoding = chardet.detect(result.stdout)["encoding"]
    print(encoding)
    info = result.stdout.decode(encoding)
    return info


autorun_info = get_autorun_info()
print("Autorun Program Information:")
print(autorun_info)
