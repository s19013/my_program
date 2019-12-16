set mouse-=a "no mouse

"set tabstop=2
"set shiftwidth=2

autocmd Filetype js setlocal ts=2 sw=2 expandtab

""------------------------------------
" Display
""------------------------------------

set cursorline " カーソル行をハイライト

" 不可視文字表示
set list
set listchars=tab:>\ ,extends:<

" 全角スペースの表示
highlight ZenkakuSpace cterm=underline ctermfg=red guibg=darkgray
match ZenkakuSpace /　/

""------------------------------------
" Map
""------------------------------------

" ハイライトを抑制
nmap \q :nohlsearch<CR>

noremap <BS> <Nop>
noremap <UP> <Nop>
noremap <Down> <Nop>
noremap <Left> <Nop>
noremap <Right> <Nop>

noremap! <BS> <Nop>
noremap! <UP> <Nop>
noremap! <Down> <Nop>
noremap! <Left> <Nop>
noremap! <Right> <Nop>

" Command History
cnoremap <C-p> <Up>
cnoremap <C-n> <Down>

" Buffer
nnoremap <silent> [b :bprevious<CR>
nnoremap <silent> ]b :bnext<CR>
nnoremap <silent> [B :bfirst<CR>
nnoremap <silent> ]B :blast<CR>

" Insert Mode での移動
inoremap <C-e> <END>
inoremap <C-a> <HOME>
inoremap <C-b> <Left>
inoremap <C-f> <Right>
inoremap <silent> jj <ESC>
inoremap <silent> <C-j> <ESC>

" visual時vで行末まで選択
vnoremap v $h
