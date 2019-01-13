# coding: UTF-8

from subprocess import call
import sys

def rmDocker(name):
    call(["docker", "stop", name])
    call(["docker", "rm", name])

if(len(sys.argv != 2)):
    print("Wrong number of argument : Usage --> python tmpRmDocker.py numberOfDockerToRemove")

else:
    for i in range(sys.argv[1]):
        name = 'minio'+str(i)
        rmDocker(name)

