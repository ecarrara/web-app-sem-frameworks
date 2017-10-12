#!/bin/bash

cmd=$1

case $cmd in
    "frontdev")
        pushd frontend
        npm run dev
        popd
        ;;
    "backdev")
        pushd backend
        uwsgi --wsgi-file app.py --http 0.0.0.0:5000 --py-autoreload=1
        popd
        ;;
    *)
        echo -e "frontdev - Roda o frontend em modo de desenvolvimento."
        ;;
esac

