# Deploying a Django application TaskBoard to Elastic Beanstalk

<br>

## Estruturação do Projeto
---


<details>
<summary>Passo a passo</summary>

```bash
git clone
```

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

```bash
pip install -r requirements.txt
```

```bash
django-admin startproject config .
```

```bash
django-admin startapp taskboard
```

```bash
touch taskboard/urls.py
```

```bash
touch taskboard/serializer.py
```

```bash
touch taskboard/forms.py
```

```bash
mkdir taskboard/templates
```

```bash
mkdir taskboard/templates/modals
```

```bash
touch taskboard/templates/base.html
```

```bash
touch taskboard/templates/board.html
```

```bash
touch taskboard/templates/index.html
```

```bash
touch taskboard/templates/modals/edit_status.html
```

```bash
touch taskboard/templates/modals/new_board.html
```

```bash
touch taskboard/templates/modals/new_status.html
```

```bash
mkdir taskboard/static
```

```bash
touch taskboard/static/style.css
```

```bash
touch taskboard/static/getTaskIs.js
```

```bash
mkdir tests
```

![Database diagram](/db-diagram.png "Database diagram")

Planejamento de rotas:
```bash
'/' -> tela com diversos boards e botão para novos boards
'/new-board' -> criação de novo board
'/<int:board_id>' -> tela do board com diversas tasks
'/<int:board_id>/new-task' -> criação de novas tasks
'/api/<int:board_id>' -> endpoint da api que retorna as tasks do board
'/api/<int:board_id>/<str:status>' -> endpoint da api que retorna as tasks do board com status específico
```

Planejamento de templates:
```bash
'base.html' -> base dos templates que será exportada para os demais templates 
'index.html' -> tela com um botão para novos boards + listagem dos boards criados 
'board.html' -> tela do board + botão de nova task + listagem das tasks
'new_task.html' -> modal para criação de tasks
'new_board.html' -> modal para criação de boards 
'edit_status.html' -> modal para edição de status
```
</details>

<br>
<br>



## Execução da aplicação
---

<details>
<summary>Passo a passo</summary>

1. Crie o ambiente virtual

```bash
python3 -m venv .venv
```

2. Ative o ambiente virtual

```bash
source .venv/bin/activate
```

3. Instale os requerimentos para a aplicação

```bash
pip install -r requirements.txt
```

4. Crie a migrações necessárias

```bash
python3 manage.py makemigrations
```

5. Realize as migrações

```bash
python3 manage.py migrate
```

6. Rode a aplicação

```bash
python3 manage.py runserver
```

</details>

<br>
<br>

## Implementação
---

<details>
<summary>Passo a passo</summary>

### Construir o TaskBoard funcional

1. Implementar os models Board e Task no models.py;

2. Implementar as funções index.py e board_page.py que renderizam os templates (nesse momento não é necessário fazer a lógica para criar novos boards e tasks);

3. Implementar os templates index.html e board.html que serão renderizados pelas funções criadas (não é necessário fazer a parte do formulário que recebe os dados para novos objetos);

4. Implementar as rotas '' e '/<int:board_id>' que consumirão as funções e templates implementados nos pontos 2 e 3 e inclui o arquivo taskboard.urls dentro do config/urls.py;

5. Registrar os models na rota de admin;

6. Criar um super usuário e no painel admin (localhost:8000/admin) criar um board e uma task nesse board para teste das páginas;

7. Adicionar os formulários nos templates html criados;

8. Implementar as classes de formulário em forms.py;

9. Refatorar funções nas views para receber requisição post e criar os objetos;

10. Implementar o serializador do board em serializer.py

11. Implementar a viewset para o board que consome o serializador implementado;

12. Implementa o Router, registra a viewset dos boards e adiciona a rota 'api/' redirecionando para as urls do Router;

13. Já é possível visualizar a rota '/api' na aplicação, pode consumir via postman a rota 'api/boards';

14. Realizar passos 10, 11 e 12 para o modelo Task;

15. Implementar as 'extra-actions' que serão filtros associados aos status das tasks;

16. Refatorar o html fazendo a extensão do base.html

17. Estilização usando bootstrap

</details>

<br>
<br>

## Deploy
---

<details>
<summary>Passo a passo</summary>

## Preparar o ambiente para fazer o deploy da aplicação

### Instalar a EB CLI

1. Para instalar o *EB CLI*, execute o seguinte comando.

```bash
pip install awsebcli --upgrade --user
```

- A opção --upgrade informa ao pip para atualizar os requisitos que já estão instalados. A opção --user informa ao pip para instalar o programa em um subdiretório do diretório de usuário para evitar a modificação de bibliotecas usadas pelo seu sistema operacional.

2. Adicione o caminho para o arquivo executável da sua variável PATH:
- No Linux e macOS: 
 - Linux: ~/.local/bin
 - macOS: ~/Library/Python/3.7/bin
- Para modificar a variável PATH (Linux, Unix ou macOS):
 - Encontre o script de perfil do shell em sua pasta de usuário. Se você não tiver certeza de qual shell você tem, execute echo $SHELL.
 ```bash
 ls -a ~
 ```
 - Bash: .bash_profile, .profile ou .bash_login.
 - Zsh: .zshrc
 - Tcsh: .tcshrc, .cshrc ou .login.
 
 2.1 Adicione um comando de exportação ao script de perfil. O seguinte exemplo adiciona o caminho representado por *LOCAL_PATH* à variável PATH atual.
 
 ```bash
 export PATH=LOCAL_PATH:$PATH
 ```

2.2 Carregue o script de perfil descrito na primeira etapa para a sessão atual. O seguinte exemplo carrega o script de perfil representado por *PROFILE_SCRIPT*.

```bash
source ~/PROFILE_SCRIPT
```

2.3 No windows:
 - 1. Python 3.7: %USERPROFILE%\AppData\Roaming\Python\Python37\Scripts Versões anteriores do Python: %USERPROFILE%\AppData\Roaming\Python\Scripts
 - 2. Para modificar a variável PATH (Windows):
 - 3. Pressione a tecla Windows e insira *environment variables*.
 - 4. Escolha Edit environment variables for your account.
 - 5. Selecione PATH e, em seguida, Edit (Editar).
 - 6. Adicione caminhos ao campo Variable value, separados por ponto e vírgula. Por exemplo: *C:\item1\path;* *C:\item2\path*
 - 7. Selecione OK duas vezes para aplicar as novas configurações.
 - 8. Feche todas as janelas do prompt de comando em execução e abra novamente uma janela do prompt de comando.

3. Verifique se a EB CLI foi instalada corretamente executando eb --version.

```bash
eb --version
```

4. Se você precisar desinstalar a EB CLI, use pip uninstall.

```bash
pip uninstall awsebcli
```

<br>

### Implantar uma aplicação Django no Elastic Beanstalk


1. Crie um ambiente virtual denominado *.venv*.

```bash
python3 -m venv .venv
```

2. Ative o ambiente virtual.

```bash
source .venv/bin/activate
```

3. Use *pip* para instalar o Django.

```bash
pip install django==3.2
```

4. Para verificiar se o Django está instalado, insira o seguinte.

```bash
pip freeze
```
```
Django==3.2
```
<br>

### Criar um projeto Django

1. Use o comandao *django-admin startproject* para criar um projeto no Django.

```bash
django-admin startproject config .
```

2. Use o comandao *django-admin startapp* para criar uma aplicação no Django.

```bash
django-admin startapp taskboard
```

3. Execute o site Django localmente com *manage.py runserver*.

```bash
python manage.py runserver
```
<br>
 
### Configurar a aplicação Django para o Elastic Beanstalk

1. Ative o ambiente virtual.

```bash
source .venv/bin/activate
```

2. Execute *pip freeze* e salve a saída em um arquivo chamado *requirements.txt*

```bash
pip freeze > requirements.txt
```

3. Crie um diretório chamado *.ebextensions*.

```bash
mkdir .ebextensions
```
- O Elastic Beanstalk usa o *requirements.txt* para determinar que pacote instalar nas instâncias do EC2 que executam a aplicação.

4. No diretório *.ebextensions*, adicione um arquivo de configuração chamado *django.config* com o texto a seguir. Exemplo *~/App/.ebextensions/django.config*

```bash
option_settings:
  aws:elasticbeanstalk:application:environment:
    DJANGO_SETTINGS_MODULE: "config.settings"
    PYTHONPATH: "/var/app/current:$PYTHONPATH"
  aws:elasticbeanstalk:container:python:
    WSGIPath: "config.wsgi:application"
```
- Essa configuração, *WSGIPath*, especifica o local do script *WSGI* que o Elastic Beanstalk usa para iniciar a aplicação.

5. Use o comando *deactivate* para desativar o ambiente virtual.

```bash
deactivate
```
- Reative o ambiente virtual sempre que for necessário adicionar pacotes ao aplicativo ou executá-lo localmente.
 
<br>

### Implantar o site com a CLI do EB

1. Inicialize o repositório da *EB CLI* com o comando *eb init*:

```bash
eb init -p python-3.7 taskboard-repo
```
- Esse comando cria um aplicativo chamado *taskboard-repo*. Ele também configura o seu repositório local para criar ambientes com a versão mais recente da plataforma *Python 3.7*.


2. Crie um ambiente e implante o aplicativo nele com eb create.

```bash
eb create taskboard-env
```
- Esse comando cria um ambiente do Elastic Beanstalk com carga balanceada chamado taskboard-env. A criação do ambiente leva cerca de 5 minutos. Como o Elastic Beanstalk cria os recursos necessários para executar a aplicação, ele gera mensagens informativas que a CLI do EB transmite ao terminal.
 
3. Quando o processo de criação do ambiente for concluído, localize o nome de domínio do seu novo ambiente executando eb status.

```bash
eb status
```
- Seu nome de domínio do ambiente é o valor da propriedade CNAME.

4. Abra o arquivo *settings.py* no diretório config. Localize a configuração *ALLOWED_HOSTS* e adicione o nome de domínio do aplicativo que você encontrou na etapa anterior ao valor da configuração. Se você não encontrar essa configuração no arquivo, adicione-a em uma nova linha.

```bash
ALLOWED_HOSTS = ['tasboard-env.elasticbeanstalk.com']
```

5. Salve o arquivo e, em seguida, implante o aplicativo executando *eb deploy*. Quando você executa eb deploy, a EB CLI empacota o conteúdo do diretório do projeto e implanta-o em seu ambiente.

```bash
eb deploy
```

6. Quando o processo de atualização do ambiente for concluído, abra o site com *eb open* no terminal.

```bash
eb open
```

7. Abra o console do Elastic Beanstalk no browser com *eb console* no terminal.

```bash
eb console
```

8. Para visualizar o log, execute o comando *eb logs* no terminal.

```bash
eb logs
```

9. Em caso de dúvidas, execute o comando *eb --help* no terminal.

```bash
eb --help
```

<br>

### Atualizar seu aplicativo

1. Modifique a configuração *TIME_ZONE* em settings.py. Exemplo ~/config/settings.py

```bash
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Recife"
USE_I18N = True
USE_TZ = True
```

2. Implante a aplicação no ambiente do Elastic Beanstalk.

```bash
eb deploy
```
<br>

### Criar um administrador de site

1. Ative seu ambiente virtual *.venv*

```bash
source .venv/bin/activate
```

2. Inicialize o banco de dados local do aplicativo Django.

```bash
python manage.py migrate
```

3. Execute *manage.py createsuperuser* para criar um administrador.

```bash
python manage.py createsuperuser
```

4. Para informar ao Django onde armazenar os arquivos estáticos, defina *STATIC_ROOT* em settings.py. Exemplo ~/App/config/settings.py

```bash
STATIC_ROOT = 'static'
```

5. Execute *manage.py collectstatic* para preencher o diretório static com os ativos estáticos (JavaScript, CSS e imagens) para o site de administração *(>> não vai funcionar <<)* vide tópico (9) e (10).

```bash
python manage.py collectstatic
```

6. Implante o aplicativo.

```bash
eb deploy
```

7. Exiba o console de administração abrindo o site em seu navegador, anexando */admin/* ao URL do site, como o seguinte:

```bash
http://taskboard-env.eba-98b6t7yt.us-west-2.elasticbeanstalk.com/admin/
```

8. Faça login com o nome de usuário e a senha que você configurou na etapa 3.

9. Teremos problemas com Admin em produção sem CSS, para solucionar instale o *whitenoise*

```bash
pip install whitenoise
```

10. Em seguida, adicione o *whitenoise* ao *MIDDLEWARE* no seu *settings.py* e por fim 

```bash
MIDDLEWARE = [
    # ...
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # ...
]
```

11. (Opcional) Caso queira armazenar em cache. Basta adicionar ao seu *settings.py*

```bash
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
```

<br>

### Apagar o projeto

1. Para economizar horas de instância e outros recursos da AWS entre as sessões de desenvolvimento, termine o ambiente do Elastic Beanstalk com eb terminate.

```bash
eb terminate taskboard-env
```

2. Se você já concluiu o aplicativo de exemplo, também pode remover a pasta do projeto.

```bash
rm -rf App
```

<br>

</details>
