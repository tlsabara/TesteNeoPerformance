import logging

import pandas as pd
from pydantic import validate_call
from typing import Optional, Any


@validate_call(config={"arbitrary_types_allowed": True})
def df_to_csv(df_: pd.DataFrame, output_path: Optional[str] = "output.csv") -> Any:
    logging.info(f"Exportando arquivo {output_path} como csv.")
    return df_.to_csv(output_path, index=False, encoding="utf-8")

@validate_call(config={"arbitrary_types_allowed": True})
def df_to_xlsx(df_: pd.DataFrame, output_path: Optional[str] = "output.xlsx") -> Any:
    logging.info(f"Exportando arquivo {output_path} como excel.")
    return df_.to_excel(output_path, index=False)


if __name__ == '__main__':
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    print(df_to_xlsx(df))