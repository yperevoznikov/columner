# Columner
It's not always easy to tame AWK :)

# Make sure script executable
```shell
chmod +x <path-to-script>/columner.py
```

## Aliases examples:
alias dcps='docker-compose ps | <path-to-script>/columner.py NAME,SERVICE,CREATED,STATUS,PORTS'
alias dcpsn='docker-compose ps | <path-to-script>/columner.py NAME'

