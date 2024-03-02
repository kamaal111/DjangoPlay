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

echo "Preinstalling Python packages"
echo "Creating virtual env"
cp -f .devcontainer/rye-config.toml ~/.rye/config.toml
curl -sSf https://rye-up.com/get | RYE_INSTALL_OPTION="--yes"  bash
source "$HOME/.rye/env"
rye sync
