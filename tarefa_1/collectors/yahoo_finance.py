from tarefa_1.collectors.bases import BaseCollector


class FlashCollector(BaseCollector):

    def __init__(self, url, target, start_date, end_date, exporter):
        self.url = url
        self.target = target
        self.start_date = start_date
        self.end_date = end_date
        self.exporter = exporter

    @property
    def target_url(self) -> str:
        return self.url.format(quote_tag=self.target, start_date=self.start_date, end_date=self.end_date)

    def _load(self) -> None:
        pass

    def _transform(self) -> None:
        pass

    def _export(self) -> Any:
        pass