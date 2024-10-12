#!/bin/zsh

if [ ! -f $ZSH/oh-my-zsh.sh ]
then
    echo "Installing Oh My Zsh"
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended

    echo "Installing zsh-autosuggestions"
    git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

    echo "Installing zsh-syntax-highlighting"
    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
fi

echo "Updating zsh configuration"
cp -f .devcontainer/.zshrc ~/.zshrc

. ~/.zshrc

cp -f rye-config.toml ~/.rye/config.toml
curl -sSf https://rye.astral.sh/get | RYE_INSTALL_OPTION="--yes"  bash

. "$HOME/.rye/env"

mkdir -p ~/.zfunc
rye self completion -s zsh > ~/.zfunc/_rye

mkdir -p $ZSH_CUSTOM/plugins/rye
rye self completion -s zsh > $ZSH_CUSTOM/plugins/rye/_rye

rye sync
