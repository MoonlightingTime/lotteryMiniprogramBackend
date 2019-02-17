pip3 list --format=freeze | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip3 install -U
