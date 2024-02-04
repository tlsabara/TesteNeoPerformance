from  pathlib import Path
import pandas as pd
import logging
from collectors.yahoo_finance import create_flash_collector
from exporters import df_to_xlsx
from storage.gdrive import GoogleDriveHandler
from task_utils import load_json_config, delete_currency_file

BASE_FOLDER = Path(__file__).parent


logging.basicConfig(
    level=logging.INFO,
)
logging.info("Iniciando script...")

config = load_json_config(str(BASE_FOLDER / "config.json"))

df_list = []

logging.info("Executando tarefas...")
if True:
    for target in config["targets"]:
        if target["active"]:
            logging.info(f"Executando tarefa {target['quote_tag']}...")
            flash_collector = create_flash_collector(
                base_url=config["white_label_download_url"],
                target=target["quote_tag"],
                exporter=lambda x: x
            )
            df_list.append(flash_collector.run())
        else:
            logging.info(f"Tarefa {target['quote_tag']} desativada.")
    logging.info("Tarefas concluídas.")
    logging.info("Fazendo join dos dados coletados...")
    task_df = pd.concat(df_list, ignore_index=True)

    df_to_xlsx(task_df, str(BASE_FOLDER / config["target_file_name"]))

logging.info("Preparando para fazer o upload...")
google_drive = GoogleDriveHandler(str(BASE_FOLDER / "settings_t.yaml"))

try:
    id_ = google_drive.get_file_id_by_title(config["target_file_name"])
except Exception as e:
    logging.info(f"Arquivo {config['target_file_name']} não encontrado. Criando e fazendo upload...")
    google_drive.create_file(
        config["target_file_name"],
        config["target_file_name"],
        mime_type='application/vnd.ms-excel'
    ).upload_file()
else:
    logging.info(f"Arquivo {config['target_file_name']} encontrado. Fazendo upload...")
    google_drive.link_file(id_).set_content(content=config["target_file_name"]).upload_file()
    logging.info("Arquivo atualizado com sucesso.")

logging.info("Apagando arquivo de dados temporário...")
delete_currency_file(BASE_FOLDER / config["target_file_name"])
logging.info("Processo concluído.")
