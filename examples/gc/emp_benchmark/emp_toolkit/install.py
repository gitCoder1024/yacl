#!/usr/python
import subprocess

install_packages = """
if [ "$(uname)" == "Darwin" ]; then
	brew list openssl || brew install openssl
 	brew list pkg-config || brew install pkg-config
 	brew list cmake || brew install cmake
else
    if command -v apt-get >/dev/null; then
        sudo apt-get install -y software-properties-common
        sudo apt-get update
        sudo apt-get install -y cmake git build-essential libssl-dev
    elif command -v yum >/dev/null; then
        sudo yum install -y python3 gcc make git cmake gcc-c++ openssl-devel
    else
        echo "System not supported yet!"
    fi
fi
"""

install_template = """
git clone https://github.com/emp-toolkit/X.git
cd X
git checkout Y
cmake .
make -j4
sudo make install
cd ..
"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-install", "--install", action="store_true")
parser.add_argument("-deps", "--deps", action="store_true")
parser.add_argument(
    "--tool", nargs="?", const="8052d95ddf56b519a671b774865bb13157b3b4e0"
)
parser.add_argument("--ot", nargs="?", const="0342af547fa80477e866c56b5e2632315ae51721")
parser.add_argument(
    "--sh2pc", nargs="?", const="61589f52111a26015b2bb8ab359dc457f8a246eb"
)
parser.add_argument(
    "--ag2pc", nargs="?", const="61589f52111a26015b2bb8ab359dc457f8a246eb"
)
parser.add_argument(
    "--agmpc", nargs="?", const="0add81ed517ac5b83d3a6576572b8daa0d236303"
)
parser.add_argument("--zk", nargs="?", const="4a0d717f5e3d18b408db422b845ccb18e24a853b")
args = parser.parse_args()

print(vars(args))


for k in ["tool", "ot", "zk", "sh2pc", "ag2pc", "agmpc"]:
    if vars(args)[k]:
        template = install_template.replace("X", "emp-" + k).replace("Y", vars(args)[k])
        print(template)
        subprocess.call(["bash", "-c", template])
