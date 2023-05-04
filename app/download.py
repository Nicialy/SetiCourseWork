import pathlib
from typing import List
from fastapi import UploadFile
import os

class DownloadFiles():
    async def __call__(self, upload_files: UploadFile) -> dict:

        async def download_file(upload_files: UploadFile) -> dict:
            folder_path = pathlib.Path(__file__).parent.resolve()
            upload_path = folder_path.joinpath(pathlib.Path("assets"))
            photo_path = upload_path.joinpath(pathlib.Path(f"{upload_files.filename}"))
            with open(photo_path, "wb+") as file_object:
                file_object.write(upload_files.file.read())
                url = upload_files.filename
            return url
        return await download_file(upload_files)


downloadfilesproduct = DownloadFiles()


def read_html_from_file(file: str) -> str:
    folder_path = pathlib.Path(__file__).parent.resolve()
    upload_path = folder_path.joinpath(pathlib.Path("assets"))
    photo_path = upload_path.joinpath(pathlib.Path(f"{file}"))
    with open(photo_path, 'r',encoding="utf8") as fh:
        data = fh.read()
    return data

def delete_file(file: str) -> None:
    folder_path = pathlib.Path(__file__).parent.resolve()
    upload_path = folder_path.joinpath(pathlib.Path("assets"))
    photo_path = upload_path.joinpath(pathlib.Path(f"{file}"))
    os.remove(photo_path)
