# Backend Django

Nessa pasta se encontram os arquivos de backend do projeto Django.

Será usado o Poetry como gestor pacotes.

Por isso, para instalar o projeto com as dependência de desenvolvimento, dentro das pasta backend rode

```bash
poetry install --with dev
```

Para rodar seu servidor Django ative o ambiente virtual:

```bash
poetry shell
```

Então rode

```bash
python manage.py runserver
```

## Padrão de código

Para o backend esse projeto usa o flake8, com as seguintes customizações

Tamanho de linha pode ter até 120 caracteres. Para ver o relatório do linter rode:

```bash
flake8 .
```

Para rodar os testes automáticos execute:

```bash
pytest devpro
```

Para gerar relatório de cobertura:

```bash
pytest devpro/ --cov devpro/ --cov-report html
```

# Shell do DJango

Essa template vem com [Django Extensions](https://django-extensions.readthedocs.io/) instalado. Então se recomenda usar
Para rodar sessão de shell interativa

```bash
python manage.py shell_plus --print-sql
```


# Usuário padrão

Nesse projeto o usuário foi customizado. Ele não tem username nem last_name como o usuário padrão do Django.
Ele usa o login como identificador único. O usuário se encontra na app base para que você pode acrescentar acampos de
acordo com sua necessidade.

## Configurações de instância

Para ler configurações de instância esse projeto usa a lib [python decouple](https://pypi.org/project/python-decouple/).
Ela é importada no arquivo settings.py

## Uploads de arquivos

O projeto está configurado para gravar arquivos publicos ou privados. Por isso, se usar ImageField ou FileField,
O parâmetro "upldat_to" precisar ter prefixo "public" para arquivos que sejam publicos e "private" para privados. Exemplos:

```python
from django.db.models import Model, ImageField, FileField

class UserProfile(Model):
    avatar = ImageField(upload_to='public/base/avatars/', null=True, blank=True)

class NotaFiscal(Model):
    arquivo = FileField(upload_to='private/base/notas_fiscais/')

```

