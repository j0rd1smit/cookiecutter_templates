import os
import zipfile

from src.Constants import RootPaths


def main() -> None:
    competition_name = "{{cookiecutter.competition}}"
    os.system(f"kaggle competitions download -c {competition_name}")

    with zipfile.ZipFile(f"{competition_name}.zip") as f:
        f.extractall(RootPaths.DATA_RAW)

    os.remove(f"{competition_name}.zip")


if __name__ == "__main__":
    main()
