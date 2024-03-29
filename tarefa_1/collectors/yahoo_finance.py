from typing import Any, Optional, Callable
from pydantic import validate_call
import pandas as pd
from datetime import datetime, timedelta
from collectors.bases import BaseCollector


class FastCollector(BaseCollector):

    @validate_call
    def __init__(self, url:str, target:str, start_date:str, end_date:str, exporter: Optional[Callable] = None):
        self.url = url
        self.target = target
        self.start_date = start_date
        self.end_date = end_date
        self.exporter = exporter
        self.df = None

    @property
    def target_url(self) -> str:
        return self.url.format(quote_tag=self.target, start_date=self.start_date, end_date=self.end_date)

    def _load(self) -> None:
        self.df = pd.read_csv(self.target_url)

    def _transform(self) -> None:
        self.df.insert(1, "quote_tag", self.target)

    def _export(self) -> Any:
        return self.exporter(self.df)


@validate_call
def create_flash_collector(
        base_url:str,
        target:str,
        start_date:Optional[str] = None,
        end_date:Optional[str] = None,
        exporter: Optional[Callable] = None
) -> FastCollector:

    if not start_date:
        start_date = str(int((datetime.now() - timedelta(days=365)).timestamp()))
    if not end_date:
        end_date = str(int(datetime.now().timestamp()))
    if not exporter:
        exporter = lambda x: x
    return FastCollector(base_url, target, start_date, end_date, exporter)




if __name__ == '__main__':
    from tarefa_1.task_utils import load_json_config

    config = load_json_config(r"/home/tlsabara/git_unix/TesteNeoPerformance/tarefa_1/config.json")
    flash_collector = create_flash_collector(
        base_url=config["white_label_download_url"],
        target="META",
    )
    df = flash_collector.run()

    print(df.shape)