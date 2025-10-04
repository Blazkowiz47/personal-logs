" Obsidian Vim Configuration

" Exit insert mode
inoremap jk <Esc>

" Yank to system clipboard
vnoremap <leader>y "+y
nnoremap <leader>y "+y

" Paste from system clipboard
nnoremap <leader>p "+p
vnoremap <leader>p "+p

" Center screen after jumps
nnoremap n nzz
nnoremap N Nzz
nnoremap <C-d> <C-d>zz
nnoremap <C-u> <C-u>zz

" Obsidian-specific commands
" Follow link under cursor
exmap follow obcommand editor:follow-link
nmap gd :follow<CR>

" Go back
exmap back obcommand app:go-back
nmap <C-o> :back<CR>

" Go forward
exmap forward obcommand app:go-forward
nmap <C-i> :forward<CR>

" Toggle checkbox
exmap togglecheck obcommand editor:toggle-checklist-status
nmap <leader>t :togglecheck<CR>
