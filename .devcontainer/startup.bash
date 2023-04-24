#!/bin/bash

if [[ ! -f $ZSH/oh-my-zsh.sh ]]
then
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended
fi

exit 0
