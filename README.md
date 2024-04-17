# POC do framework Streamlit
Este repositório tem como objetivo criar uma POC utilizando [streamlit](https://docs.streamlit.io/) para apresentação na aula de Data Engineering Programming, matéria presente no MBA de Engenharia de dados da FIAP.

>Versão 1.0.0 | Autor: Gabriel Ronchi Brigido | Versão do Python 3.12.2

## Pré-requisitos
- Para o versionamento e reastreabiliade do código use o **Git**, instalação [aqui](https://git-scm.com)
- Para edição facilitada do código use o **VSCode**, instalação [aqui](https://code.visualstudio.com/)
- Para melhor controle de versões de instalação do *Python* use o **Pyenv**, guia de instalação [aqui](https://www.youtube.com/watch?v=HTx18uyyHw8) e documentação [aqui](https://github.com/pyenv/pyenv)
- Para gerenciamento de pacotes de dependências use o **Poetry**, consulte a  documentação [aqui](https://python-poetry.org/docs/)


## Ajustando o ambiente

Uma vez com os pré-requisitos atendidos você pode clonar este repositório para um repositório local na sua máquina e começar a executá-lo

- Clone o repositório:

```bash
    git clone https://github.com/sr-brigido/poc-streamlit.git
    cd poc-streamlit #Navegue até a pasta do projeto
```

- Uma vez no diretório, execute os comandos do `Poetry` para preparar o ambiente do projeto

```bash
poetry config virtualenvs.in-project true   #Comando para criar os ambientes virtuais dentro do projeto
poetry config virtualenvs.prefer-active-python true #Comando para o poetry identificar a versão do python utilizada do projeto
```
```bash
poetry install --no-root    #instalar as dependencias base do projeto
```

- Execute o seguinte comando para iniciar aplicação

```bash
poetry run task run    #iniciar o FrontEnd com Streamlit
```

## Contato

Para sugestões, dicas e feedbacks utilize os seguintes e-mails do grupo:

**Gabriel Ronchi Brigido** - [gabriel.brigido@gbinteligencia.com](mailto:gabriel.brigido@gbinteligencia.com)

**Isabella Piveta de Godoy** - [isabellapiveta@gmail.com](mailto:isabellapiveta@gmail.com)

**Jéssica Ramos Pino de Souza** - [jessycapino16@gmail.com](mailto:jessycapino16@gmail.com)

**Mariana Marques de Carvalho** - [marianammc2008@yahoo.com.br](mailto:marianammc2008@yahoo.com.br)

**Grazielle Djunko Ida** - [grazy.ida89@gmail.com](mailto:grazy.ida89@gmail.com)
