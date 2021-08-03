import sys


print("sys.argv: {}\n".format(sys.argv))

print("sys.prefix: {}\n".format(sys.prefix))

print("sys.executable: {}\n".format(sys.executable))

print("sys.version: {}\n".format(sys.version))

print("sys.version_info: {}\n".format(sys.version_info))

print("sys.version_info.major: {}\n".format(sys.version_info.major))

for path in sys.path:
    print(path)
print()

print("sys.platform: {}\n".format(sys.platform))

print(dir(sys), '\n')

print("We have a problem", file=sys.stderr)












