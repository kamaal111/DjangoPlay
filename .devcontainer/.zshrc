# 👉 Rebuild this dev container to have these changes reflected

export ZSH="$HOME/.oh-my-zsh"

ZSH_THEME="robbyrussell"

plugins=(
    git
    zsh-autosuggestions
    zsh-syntax-highlighting
)

source $ZSH/oh-my-zsh.sh
source "$HOME/.rye/env" || true

alias bat=batcat
