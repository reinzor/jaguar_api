jaguar-console () { 
    depcheck ipython
    JAGUAR_API_DIR=`rospack find jaguar_api`/src/jaguar_api
    ipython -i --no-banner --no-confirm-exit --autocall 2 "${JAGUAR_API_DIR}/jaguar.py" -- $*
}
