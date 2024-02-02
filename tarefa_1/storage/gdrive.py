from __future__ import annotations
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from typing import Any

from pydrive.files import GoogleDriveFile


class GoogleDriveHandler:
    def  __init__(self, config_file: str):
        self.config_file = config_file
        self.ggl_auth = GoogleAuth(settings_file=self.config_file)
        self.ggl_auth.LocalWebserverAuth()
        self.ggl_drive = GoogleDrive(self.ggl_auth)
        self.ggl_file_instance: GoogleDriveFile | None = None

    def get_file_id_by_title(self, title: str) -> str:
        try:
            file_list = self.ggl_drive.ListFile({'q': f"title = '{title}' and trashed=false"}).GetList()
            if len(file_list) == 1:
                return file_list[0]['id']
            elif len(file_list) > 1:
                raise Exception(f"Encontrado {len(file_list)} arquivos com o mesmo nome {title}.")
            else:
                raise Exception(f"Nenhum arquivo encontrado com o nome {title}.")
        except Exception as e:
            raise Exception(f"Erro ao buscar arquivo {title}: {str(e)}")


    def link_file(self, id_file: str) -> GoogleDriveHandler:
        self.ggl_file_instance = self.ggl_drive.CreateFile({'id': id_file})
        return self

    def download_file(self) -> GoogleDriveHandler:
        self.ggl_file_instance.GetContentFile(self.ggl_file_instance['title'])
        return self

    def upload_file(self) -> GoogleDriveHandler:
        self.ggl_file_instance.Upload({'convert': True})
        return self

    def create_file(self, title: str, content: Any | bytes | str = None, mime_type: str = "text/plain") -> GoogleDriveHandler:
        self.ggl_file_instance = self.ggl_drive.CreateFile({'title': title, 'mimeType': mime_type})
        if content:
            self.set_content(content=content)
        return self

    def set_content(self, content: Any | bytes | str) -> GoogleDriveHandler:
        self.ggl_file_instance.SetContentFile(content)
        return self


if __name__ == '__main__':
    # https://drive.google.com/file/d/1eoEGmyApdbM7-42DXSseaUQ4wJ9xGONl/view?usp=sharing
    from datetime import datetime
    config_file = "settings_t.yaml"
    gdrive = GoogleDriveHandler(config_file)
    gdrive.create_file("text_file.txt", f"Hello World at {datetime.now()}").upload_file()

    message = input("Enter message: ")
    message += f" at {datetime.now()}"
    id_ = "1eoEGmyApdbM7-42DXSseaUQ4wJ9xGONl"

    gdrive.link_file(id_).set_content(content=message).upload_file()