import os
import pathlib
import shutil


class Photo:
    def __init__(self, photo_path: str | None = None, id_client: int | None = None):
        self.aux_path = pathlib.PurePath(os.getcwd())
        self.id_client = id_client

        if photo_path is None and id_client is None:
            self.photo_path = f"{self.aux_path.parent}\\{self.aux_path.name}\\pictures\\avatar.svg"
        else:
            self.photo_path = f"{self.aux_path.parent}\\{self.aux_path.name}\\pictures\\{self.id_client}.jpg"
            try:
                os.remove(self.photo_path)
            except FileNotFoundError:
                pass

            try:
                shutil.copyfile(photo_path, self.photo_path)
            except FileNotFoundError:
                try:
                    os.mkdir(f"{self.aux_path.parent}\\{self.aux_path.name}\\pictures")
                    shutil.copyfile(photo_path, self.photo_path)
                except FileExistsError:
                    pass
