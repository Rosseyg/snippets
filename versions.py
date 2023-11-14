import sys

print(sys.version)
print(sys.version_info)
print(sys.version_info.major)
print(sys.version_info.minor)
print(sys.version_info.micro)
print(sys.executable)
print(sys.path)
print(sys.platform)
# print current python modules
#print(sys.modules)

#print django location and version
import django
print(django.__file__)
print(django.get_version())
