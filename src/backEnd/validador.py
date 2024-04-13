"""Este módulo contém funções que validam e carregam \
o excel no banco de dados."""

import pandas as pd

from contracts.contratoMetas import Metas

DATABASE_URL = "postgresql://admin:admin@localhost:5432/poc_streamlit"


def validarExcel(arquivo):
    """Valida o arquivo excel de input."""
    try:
        df = pd.read_excel(arquivo)

        colunasExtras = set(df.columns) - set(Metas.model_fields.keys())
        if colunasExtras:
            return (
                False,
                f"Colunas extras detectadas \
                    no Excel: {', '.join(colunasExtras)}",
            )

        for index, row in df.iterrows():
            try:
                _ = Metas(**row.to_dict())
            except Exception as e:
                raise ValueError(f"Erro na linha {index + 2}: {e}")

        return df, True, None

    except ValueError as ve:
        return df, False, str(ve)
    except Exception as e:
        return df, False, f"Erro inesperado: {str(e)}"


def inserirExcelBanco(df):
    """Carrega Dataframe no Banco de dados."""
    df.to_sql("metas", con=DATABASE_URL, if_exists="replace", index=False)