import platform

def platform_detection():
    return platform.system()

print("The Operating System of this machine is {}".format(platform_detection()))