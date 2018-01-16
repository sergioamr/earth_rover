from crypt import crypt
from fabric.api import local, settings, abort, run, env, sudo, put, get, prefix
import os

BASE_DIR = os.path.dirname(__file__)
WORKSPACE_DIR = os.path.join(BASE_DIR, "workspace/src")

from config import PI_PASSWORD

env.hosts = ["%s:%s" % ("raspberrypi.local", 22)]

env.user = "pi"
env.password = PI_PASSWORD


def init_local():


