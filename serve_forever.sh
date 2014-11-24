#!/bin/bash -e

main() {
    . gif_env/bin/activate
    pip install waitress

    while [ 1 ]; do
        pserve --reload development.ini
        sleep 1
    done
}

main "$@"
