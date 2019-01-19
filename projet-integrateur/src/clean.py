#!/usr/bin/python3
# coding: UTF-8

from subprocess import call
import sys

def rmDocker(name):
    call(["docker", "stop", name])
    call(["docker", "rm", name])

if(len(sys.argv) != 2):
    print("Wrong number of argument : Usage --> python clean.py numberOfDockerToRemove")

else:
    for i in range(int(sys.argv[1])):
        name = 'minio'+str(i)
        rmDocker(name)
    call("rm -rf /mnt/data*", shell=True)


