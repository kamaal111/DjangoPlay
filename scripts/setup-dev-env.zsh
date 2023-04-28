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
deactivate || echo "Nothing to deactivate"
cd /workspaces/DjangoPlay
rm -rf .venv
echo "Creating virtual env"
python --version
python -m venv .venv
. .venv/bin/activate
echo "Installing Poetry"
pip install poetry
echo "Installing all the packages with Poetry"
poetry install
