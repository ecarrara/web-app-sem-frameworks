#!/bin/bash

cmd=$1

case $cmd in
    "frontdev")
        pushd frontend
        npm run dev
        popd
        ;;
    *)
        echo -e "frontdev - Roda o frontend em modo de desenvolvimento."
        ;;
esac

