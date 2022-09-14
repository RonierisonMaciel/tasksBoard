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

### Preparar o ambiente para fazer o deploy da aplicação

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
### Criar um projeto Django

1. Use o comandao *django-admin startproject* para criar um projeto no Django.

```bash
django-admin startproject config .
```

2. Use o comandao *django-admin startapp* para criar uma aplicação no Django.

```bash
django-admin startapp
```

3. Execute o site Django localmente com *manage.py runserver*.

```bash
python manage.py runserver
```

### Configurar a aplicação Django para o Elastic Beanstalk

1. ...


</details>
