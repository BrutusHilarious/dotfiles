# -*- mode: sh; -*-
### Evan's Bashrc ###

### Shopt Settings ###
shopt -s autocd
shopt -s checkwinsize
shopt -s expand_aliases
shopt -s nocaseglob
shopt -s cdspell
shopt -s histappend
###

### Disable Bell in Terminal: URXVT ###
xset b off
###

### History ###
HISTSIZE=10000
HISTFILESIZE=10000
###

### FCEDIT ###
FCEDIT="emacs"

### PATH ###
PATH=$PATH\:/home/evan/_code/scripts ; export PATH
###

### Locale Setting for 'ls' Sorting ###
export LC_COLLATE=C
###

### Aliases ###
alias ls="LC_ALL=C ls --color=auto -NX"
alias la="ls -A"
alias mpv="c;mpv"
alias feh='feh -ZF -B "#000" --no-fehbg'
alias ff="~/.firefox/firefox"
###

### Carbon Navigation ###
alias dl="clear;cd ~/downloads"
alias org="clear;cd ~/_orgs"
alias ex="clear;cd ~/_nextcloud"
alias ..="cd .."



### Music Aliases ###
alias mp="clear; mpc pause"
alias mpl="clear; mpc play"
alias mn="clear; mpc next"
alias mpr="clear; mpc prev"

alias pia="/opt/pia/run.sh"

# Editing Aliases #
alias e="emacs -Q -nw --color"
alias .b="e ~/.bashrc" 
alias .v="e ~/.vimrc" 
alias .e="e ~/.emacs.d/init.el"
alias .xr="e ~/.Xresources"
alias .q="e ~/.config/qutebrowser/config.py"
alias .i="e ~/.i3/config"
alias .z="e ~/.config/zathura/zathurarc"
alias .co="e ~/.config/compton.conf"
alias .p="e ~/.config/polybar/config"
alias .r="e ~/.config/ranger/rc.conf"
alias .tx="e ~/.tmux.conf"
alias c="clear"
###

### Python ###
alias py="python3"
alias python="python3"
###

### ??? ###
stty -ixon

### Import Pywal Colors to Bash ###
#source "$HOME/.cache/wal/colors.sh"
. "${HOME}/.cache/wal/colors.sh"

# i don't think this is useful.
###

### Example: Content goes betwixt elipses ###
#export PS1="\e[$colorCYAN ... \e[m "
###

### Git Status Function PS1 ###

###

### Prompt Command ###
redBOLDSTART="\033[1;31m"
redBOLDEND="\033[0m"
PROMPT_COMMAND='printf $redBOLDSTART%"$COLUMNS"s$redBOLDEND |tr " " "-"'
###

### Prompt Function ###
func_prompt () {

    local REDBOLDSTART="\[\033[1;31m" 
    local REDBOLDEND="\033[0m\]"

    local tophook="┌─"
    local bottomhook="└─"
    local dash="-"
    local dirdur="\w"

    echo "$tophook[$REDBOLDSTART$dirdur$REDBOLDEND]\n$bottomhook:"

}
###

### Export PS1 ###
export PS1=$(func_prompt)
###

### Add Colors to Man Pages ###
man() {
    env \
        LESS_TERMCAP_mb=$(printf "\e[1;31m") \
        LESS_TERMCAP_md=$(printf "\e[1;36m") \
        LESS_TERMCAP_me=$(printf "\e[0m") \
        LESS_TERMCAP_se=$(printf "\e[0m") \
        LESS_TERMCAP_so=$(printf "\e[31;1;7m") \
        LESS_TERMCAP_ue=$(printf "\e[0m") \
        LESS_TERMCAP_us=$(printf "\e[1;32m") \
            man "$@"
}
###

alias config='/usr/bin/git --git-dir=/home/evan/.cfg/ --work-tree=/home/evan'
