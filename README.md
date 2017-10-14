# App Web sem Frameworks

Exemplo de aplicação sem usar frameworks. O objetivo desse projeto é mostrar
como desenvolver aplicações web em Python e Javascript do começo ao fim
sem depender de frameworks e bibliotecas de terceiros.

Não que você vá fazer isso no seu trabalho, mas é interessante saber como as
coisas funcionam por de baixo dos panos.

## Como faz pra rodar isso?

A aplicação esta separada em `backend` (python) e `frontend` (js).

### Executando o backend

Entra na pastinha `backend`, cria uma virtualenv, instala o uUWSGI nela
e pede para ele rodar sua aplicação em app.py.

```shellscript
cd backend
mkvirtualenv --python $(which python3) videoaula-js-py
pip install uwsgi
uwsgi --wsgi-file app.py --http 0.0.0.0:5000 --py-autoreload 1
```

O backend deve ser acessível do endereço `http://localhost:5000`.

### Executando o frontend

Entra na pastinha `frontend`, instala as o babel e o webpack para transpilar
seu ECMAScript 6 para Javascript antigão e então manda rodar as coisas.

```shellscript
npm install
npm run dev
```

O frontend deve ser acessível do endereço `http://localhost:9000`.

