if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

export ZSH="/home/nimeavles/.oh-my-zsh"

ZSH_THEME="powerlevel10k/powerlevel10k"
plugins=( git zsh-syntax-highlighting zsh-autosuggestions )


source $ZSH/oh-my-zsh.sh

if [[ "$XDG_SESSION_DESKTOP" =~ "bspwm" ]] || \
   [[ "$XDG_SESSION_DESKTOP" =~ "qtile-venv" ]]
then
    xrandr --auto --output HDMI-1 --left-of eDP-1
    xrandr --auto --output eDP-1 --primary
fi


[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
typeset -g POWERLEVEL9K_INSTANT_PROMPT=quiet
alias ls='exa --group-directories-first'
alias tree='exa -T'
alias nv='nvim'
alias cat='bat'
alias py='python3'
