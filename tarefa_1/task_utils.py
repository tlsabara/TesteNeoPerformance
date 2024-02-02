import json
import os
from dotenv import load_dotenv
from pathlib import Path
import logging

def delete_currency_file(filename: str) -> None:
    Path(filename).unlink()
    logging.info(f"Arquivo {filename} deletado.")



def load_json_config(json_config: str) -> dict:
    """Realiza a leitura e a conversão do arquivo json de configuração em um dicionário."""
    load_dotenv()
    logging.info("Carregando arquivo de configuração.")
    conf = json.loads(open(json_config).read())

    required_parameters = [
        "white_label_download_url",
        "white_label_site_url",
        "targets",
        "project_name",
        "version",
        "target_file_id",
        "target_file_name"
    ]

    valid_parameters = (
        conf.get("project_name") == os.getenv("PROJECT_NAME")
        and conf.get("version") == os.getenv("VERSION")
    )

    for param in required_parameters:
        if param not in conf:
            raise ValueError(f"Parametro {param} ausente no arquivo de configuração.")

    required_target_parameters = [
        "quote_tag",
        "company",
        "active"
    ]

    for target in conf["targets"]:
        for param in required_target_parameters:
            if param not in target:
                raise ValueError(
                    f"Parametro {param} ausente no arquivo de configuração. Target: {target['quote_tag']}."
                )
    logging.info("Arquivo de configuração carregado com sucesso.")
    return conf

if __name__ == '__main__':
    config = load_json_config(r"/home/tlsabara/git_unix/TesteNeoPerformance/tarefa_1/config.json")