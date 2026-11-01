from pathlib import Path
import argparse
import shutil

def setup_auto_configs():
    """
    Создаёт обычные директории и символические ссылки на файлы в домашней папке.

    Обходит директории рекурсивно. По умолчанию пропускает существующие файлы
    и конфликтующие директории, сохраняя содержимое существующих каталогов.
    Существующие символические ссылки удаляет и создаёт заново.

    При использовании --force перемещает существующие файлы и директории
    в папку backup/ перед созданием символических ссылок. Если резервная
    копия с таким именем уже существует, объект пропускается.

    Игнорирует .DS_Store и папку backup/.

    Command-line arguments:
        -f, --force: Перемещать существующие файлы и директории в backup/
            перед созданием символических ссылок.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--force", action="store_true")
    args = parser.parse_args()

    source_dir = Path(__file__).resolve().parent.parent / "auto_configs"

    backup_dir = source_dir / "backup"

    ignore_files = {".DS_Store", "backup"}

    def setup_path(source):
        if source.name in ignore_files:
            return

        relative_path = source.relative_to(source_dir)
        target = Path.home() / relative_path
        backup_target = backup_dir / relative_path

        if source.is_dir() and target.is_dir() and not target.is_symlink():
            for child in source.iterdir():
                setup_path(child)
            return

        if target.is_symlink():
            target.unlink()

        elif target.exists():
            if not args.force:
                print(f"skip: {relative_path}")
                return

            if backup_target.exists() or backup_target.is_symlink():
                print(f"skip: backup exists: {relative_path}")
                return

            backup_target.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(target), str(backup_target))
            print(f"backup: {relative_path}")

        if source.is_dir():
            target.mkdir()
            for child in source.iterdir():
                setup_path(child)
        else:
            target.symlink_to(source)
            print(f"link: {relative_path}")

    for source in source_dir.iterdir():
        setup_path(source)


if __name__ == "__main__":
    setup_auto_configs()
