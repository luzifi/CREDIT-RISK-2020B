import os
import subprocess


class Main:

    def __init__(self):
        pass

    @staticmethod
    def hello(world: str = "World") -> str:
        return f"Hello, {world}"

    @staticmethod
    def console():
        cmd = "ipython"
        if os.name != "posix":
            cmd = f"winpty {cmd}"
        return subprocess.run(cmd, shell=True, check=True, env=None)

    @staticmethod
    def notebook(port: int = 9999, no_browser: bool = False):
        cmd = f"jupyter-notebook --port {port}"
        if no_browser:
            cmd += " --no-browser"
        return os.system(cmd)
