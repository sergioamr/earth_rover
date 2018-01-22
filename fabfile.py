from crypt import crypt
from fabric.api import local, settings, abort, run, env, sudo, put, get, prefix, cd
import os
import shutil
from subprocess import call


BASE_DIR = os.path.dirname(__file__)
WORKSPACE_DIR = os.path.join(BASE_DIR, "workspace")

# from config import PI_PASSWORD
env.hosts = ["%s:%s" % ("10.2.50.180", 22)]
env.user = "paul"
env.password = "mouse"

TEST_VERSION = "0.0.1"


def unmake():
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


def test():
    sudo("echo hello")


def install():
    """
    installs into /opt/earthrover_ros
    :return:
    """
    install_path = "/opt/earthrover_ros/kinetic"
    sudo("mkdir -p %s" % install_path)
    with cd("/home/paul/earth-ugv/workspace"):
        sudo("source /opt/ros/kinetic/setup.sh && source ~/earth-ugv/workspace/devel/setup.sh && catkin_make install -DCMAKE_INSTALL_PREFIX=%s" % install_path)


def build_test():
    tag = TEST_VERSION
    put("docker", "~")
    sudo('docker build --no-cache=true -t="earthrover/earthrover-test:%s" docker/earthrover-test' % tag)
    # sudo('docker push earthrover/earthrover-test:%s' % tag)
    # sudo('docker tag earthrover/earthrover-test:%s earthrover/earthrover-test:latest' % tag)
    # sudo('docker push earthrover/earthrover-test:latest')