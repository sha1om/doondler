#! /usr/bin/python3
from modules.package_managers import DefaultManager


def main():
    """ Install all system dependencies. """
    package_manager = DefaultManager().get_default_manager()()
    package_manager.install("curl")
    package_manager.install("python3")
    # All dependencies here


if __name__ == "__main__":
    main()
