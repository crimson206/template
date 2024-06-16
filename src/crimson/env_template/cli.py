import argparse
from .utils import (
    generate_toml,
    create_skeleton,
    generate_setup_env_script,
    setup_env
)


def build_up_skeleton():
    generate_toml()
    generate_setup_env_script()
    create_skeleton()


def setup_conda_env():
    setup_env()


def main():
    parser = argparse.ArgumentParser(description='CLI for env-template commands')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    _ = subparsers.add_parser('build-up-skeleton', help='Build up the project skeleton')
    _ = subparsers.add_parser('setup-conda-env', help='Set up the Conda environment')

    args = parser.parse_args()

    if args.command == 'build-up-skeleton':
        build_up_skeleton()
    elif args.command == 'setup-conda-env':
        setup_conda_env()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
