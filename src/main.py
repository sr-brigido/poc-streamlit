"""Este módulo executa a aplicação como um todo."""

from streamlit import markdown

from backEnd.validador import inserirExcelBanco, validarExcel
from frontEnd.ui import ValidadorMetasUI


def app():
    """Roda aplicação de validação."""
    ui = ValidadorMetasUI()
    ui.cabecalho()

    arquivo = ui.uploadArquivo()

    markdown("---")

    if arquivo:
        df, result, error = validarExcel(arquivo)
        ui.resultados(result, error)

        if error:
            ui.erros()
        elif ui.inserirBanco():
            inserirExcelBanco(df)
            ui.sucesso()

    ui.downloadExemplo()


if __name__ == "__main__":
    app()
