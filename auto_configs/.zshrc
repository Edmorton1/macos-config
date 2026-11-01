# =========================================================
# History
# =========================================================

unset HISTFILE
HISTSIZE=1000
SAVEHIST=0

setopt HIST_IGNORE_DUPS

# =========================================================
# Shell behavior
# =========================================================

setopt AUTOCD
setopt NUMERIC_GLOB_SORT

# =========================================================
# Completion
# =========================================================

# Load completion system
autoload -Uz compinit

compinit

# Enable interactive completion menu selection
zstyle ':completion:*' menu select

# Make completion case-insensitive
# Example: "doc" can complete to "Documents"
zstyle ':completion:*' matcher-list 'm:{a-z}={A-Za-z}'  # lowercase input matches upper and lower

# =========================================================
# Prompt
# =========================================================

eval "$(starship init zsh)"

# =========================================================
# NVM
# =========================================================

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

# =========================================================
# Custom functions
# =========================================================

[[ -f ~/.zshrc.local ]] && source ~/.zshrc.local
