name = "tk_config_default2"

version = "1.2.10"

authors = [
    "Autodesk"
]

description = \
    """
    The second generation default configuration for Shotgun Toolkit.
    """

requires = [
    "cmake-3+",
    "pip-19+",
    "python-2.7+<3"
]

variants = [
    ["platform-linux"]
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "tk_config_default2-{version}".format(version=str(version))
