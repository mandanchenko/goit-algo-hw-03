import argparse
from pathlib import Path
import shutil


def parse_argv():
    parser = argparse.ArgumentParser(description="Копіює файли в папку")
    parser.add_argument("-s", "--source", type=Path, help="Папка з файлами")
    parser.add_argument(
        "-o", "--output", type=Path, default=Path("output"), help="Папка для копіювання"
    )
    return parser.parse_args()


def get_paths_from_user():
    source_path = input("Введіть шлях до вихідної директорії: ")

    while not source_path:
        print("Шлях до вихідної директорії не може бути порожнім.")
        source_path = input("Введіть шлях до вихідної директорії ще раз: ")

    output_path = input(
        "Введіть шлях до директорії призначення (або натисніть Enter для використання 'dist'): "
    )
    output_path = output_path or "output"

    return Path(source_path), Path(output_path)


def copy_files_to_folders(source: Path, output: Path):
    for file_or_dir in source.iterdir():
        if file_or_dir.is_dir():
            copy_files_to_folders(file_or_dir, output)
        else:
            folder_name = (
                file_or_dir.suffix[1:] if file_or_dir.suffix else "no_extension"
            )
            folder = output / folder_name
            folder.mkdir(parents=True, exist_ok=True)
            shutil.copy(file_or_dir, folder)


def main():
    args = parse_argv()

    if not args.source:
        source_path, output_path = get_paths_from_user()
    else:
        source_path, output_path = args.source, args.output

    try:
        copy_files_to_folders(source_path, output_path)
        print("Копіювання завершено успішно.")
    except Exception as e:
        print(f"Помилка: {e}")


if __name__ == "__main__":
    main()
