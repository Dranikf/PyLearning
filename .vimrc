set number
set tabstop=4

set hlsearch
set splitbelow
set splitright
set encoding=utf-8

" настройк плагинов для vim-plug
call plug#begin('~/.vim/plugged')
Plug 'scrooloose/nerdtree', { 'on':  'NERDTreeToggle' }
Plug 'ycm-core/YouCompleteMe'
call plug#end()

nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>

"mappings
map <C-n> :NERDTreeToggle<CR>
map <C-m> <Plug> (easymotion-prefix)
"mappings
