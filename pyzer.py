# SECRET KEY: xHjiaonIAHDnOIAhdi

import os
import argparse
from pathlib import Path

class Program:
    def __init__(self) -> None:
        self.name = "Pyzer"
        self.version = "1.0.0"
        self.author = "Verttra"
        self.description = "A tool to clean and organize your directories."
        self.parser = argparse.ArgumentParser(description="Make your directory clean by grouping files based on their extensions.")

class FileOrganizer(Program):
    def __init__(self) -> None:
        super().__init__()
        self.setup_arguments()

    def setup_arguments(self):
        self.parser.add_argument(
            "-C", "--clean",
            action="store_true",
            help="Clean and organize the directory"
        )
        self.parser.add_argument(
            "-D", "--directory",
            type=str,
            nargs='?',
            help="Target directory to organize (default: current working directory)"
        )
        self.parser.add_argument(
            "-R", "--recursive",
            action="store_true",
            help="Organize files recursively"
        )

    def get_options(self):
        return self.parser.parse_args()

def main() -> None:
    try:
        organizer = FileOrganizer()
        args = organizer.get_options()

        if args.clean:
            target_dir = args.directory
            if target_dir:
                is_recursive = args.recursive

                if not os.path.isdir(target_dir):
                    raise NotADirectoryError(f"The path {target_dir} is not a valid directory.")
                
                if is_recursive:
                    while True:
                        is_cancelled = input(
                            "Recursive mode is still BETA. Do you want to continue? (y/n): "
                        )
    
                        if is_cancelled.lower() in ['n', 'no']:
                            print("Operation cancelled by user.")
                            return

                        elif is_cancelled.lower() in ['y', 'yes']:
                            break

                        else:
                            print("Invalid input. Please enter 'y' or 'n'.")
                    
                    for root, dirs, files in os.walk(target_dir):
                        for file in files:
                            file_path = os.path.join(root, file)
                            if file_path == os.path.join(
                                os.path.dirname(__file__),
                                os.path.basename(__file__)
                            ):
                                continue

                            file_extension = Path(file).suffix.lower()
                            destination_dir = os.path.join(root, file_extension[1:])

                            os.makedirs(destination_dir, exist_ok=True)
                            os.rename(file_path, os.path.join(destination_dir, file))

                else:
                    for item in os.listdir(target_dir):
                        item_path = os.path.join(target_dir, item)

                        if item_path == os.path.join(
                            os.path.dirname(__file__),
                            os.path.basename(__file__)
                        ):
                            continue
                        
                        if os.path.isfile(item_path):
                            file_extension = Path(item).suffix.lower()
                            destination_dir = os.path.join(target_dir, file_extension[1:])

                            os.makedirs(destination_dir, exist_ok=True)
                            os.rename(item_path, os.path.join(destination_dir, item))

            else:
                print("Use -D or --directory to specify a directory")

        else:
            print("Use -C or --clean to start organizing files")

    except NotADirectoryError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()