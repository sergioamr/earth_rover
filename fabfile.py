from crypt import crypt
from fabric.api import local, settings, abort, run, env, sudo, put, get, prefix
import os
import shutil

BASE_DIR = os.path.dirname(__file__)
WORKSPACE_DIR = os.path.join(BASE_DIR, "workspace")


# from config import PI_PASSWORD

env.hosts = ["%s:%s" % ("raspberrypi.local", 22)]

# env.user = "pi"
# env.password = PI_PASSWORD



def catkin_unmake():
    devel_dir = os.path.join(WORKSPACE_DIR, "devel")
    build_dir = os.path.join(WORKSPACE_DIR, "build")
    make_file = os.path.join(WORKSPACE_DIR, "src", "CMakeLists.txt")
    workspace_file = os.path.join(WORKSPACE_DIR, ".catkin_workspace")

    if os.path.exists(devel_dir):
        shutil.rmtree(devel_dir)
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)
    if os.path.exists(make_file):
        os.remove(make_file)
    if os.path.exists(workspace_file):
        os.remove(workspace_file)

