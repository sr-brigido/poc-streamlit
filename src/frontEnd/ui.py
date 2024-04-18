"""Este módulo contém a classe que inicia a interface do app."""

from io import BytesIO

import streamlit as st
from pandas import DataFrame, ExcelWriter


class ValidadorMetasUI:
    """Interface do validador de tabela."""

    def __init__(self):
        """Inicia a instância da UI."""
        self.set_page_config()

    def set_page_config(self):
        """Abre configurações da página."""
        st.set_page_config(page_title="Validador de tabela de metas")

    def cabecalho(self):
        """Exibe título da página."""
        st.title("Faça upload do seu arquivo para verificação de metas")

    def uploadArquivo(self):
        """Habilita o upload de arquivos."""
        return st.file_uploader(
            "Carregue seu arquivo \
                            Excel aqui",
            type=["xlsx"],
        )

    def resultados(self, result, error):
        """Exibe os resultados da verificação."""
        if error:
            st.error(f"Erro na validação: {error}")
        else:
            st.success("O schema do arquivo Excel está correto!")

    def inserirBanco(self):
        """Exibe botão para carga de dados no banco."""
        return st.button("Salvar no Banco de Dados")

    def erros(self):
        """Exibe mensagem de erro."""
        return st.error("Necessário corrigir a planilha!")

    def sucesso(self):
        """Exibe mensagem de validação completa."""
        return st.success("Dados salvos com sucesso no banco de dados!")

    def downloadExemplo(self):
        """Exibe um botão de download com o exemplo\
              da tabela a ser preenchida."""
        dfExemplo = DataFrame(columns=["data", "vendedor", "valor"])
        buffer = BytesIO()

        with ExcelWriter(buffer, engine="xlsxwriter") as writer:
            dfExemplo.to_excel(writer, sheet_name="metas", index=False)

        return st.download_button(
            label="Baixe o arquivo de exemplo aqui",
            data=buffer.getvalue(),
            file_name="exemplo.xlsx",
            mime="application/vnd.ms-excel",
        )
