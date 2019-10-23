
import subprocess


def open_app():
    subprocess.call(
        ["/usr/bin/open", "-W", "-n", "-a", "/Applications/Xcode.app"])


if __name__ == '__main__':
    open_app()