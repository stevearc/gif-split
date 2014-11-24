#!/bin/bash -e

dl () {
    local name=$1
    local url=$2
    local args=
    if [ "$url" ]; then
        args="-O $name"
    else
        url="$name"
        name=$(basename "$name")
    fi
    if [ ! -e "$name" ]; then
        wget -O "$name" "$url"
    fi
}

main() {
    pushd $(dirname $0) > /dev/null
    mkdir -p gif_split/static
    pushd gif_split/static > /dev/null
    if [ "$1" == "-r" ]; then
        rm -rf *
    fi

    local b_version="3.1.1"
    if [ ! -e bootstrap ]; then
        dl https://github.com/twbs/bootstrap/archive/v$b_version.zip
        unzip v$b_version.zip
        rm v$b_version.zip
        mv bootstrap-$b_version/dist bootstrap
        rm -rf bootstrap-$b_version
    fi

    popd > /dev/null
    popd > /dev/null
}

main "$@"
