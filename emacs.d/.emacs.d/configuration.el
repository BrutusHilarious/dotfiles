(setq inhibit-startup-message t)
(setq ring-bell-function 'ignore)
(setq make-backup-files nil)
(menu-bar-mode 0)
(tool-bar-mode 0)
(scroll-bar-mode -1)
(blink-cursor-mode -1)
(set-default 'cursor-type 'box)
(size-indication-mode t)
(global-visual-line-mode t)
;(toggle-truncate-lines t)
;(global-hl-line-mode +1)
;(set-face-background 'hl-line "#F13333")

(global-prettify-symbols-mode t)

(setq-default tab-width 2)

(set-language-environment "UTF-8")
(set-default-coding-systems 'utf-8)

(add-hook 'org-mode-hook #'org-bullets-mode)
(add-hook 'org-mode-hook #'org-indent-mode)

(add-to-list 'org-structure-template-alist
	     '("el" "#+BEGIN_SRC emacs-lisp\n?\n#+END_SRC"))

(org-babel-do-load-languages
 'org-babel-load-languages
 '((emacs-lisp . t)
   (python . t)
   (dot . t)
   (gnuplot . t)))

(setq org-ellipsis "⤵")
(setq org-src-tab-acts-natively t)
(setq org-src-fontify-natively t)

(setq org-confirm-babel-evaluate nil)

(setq ido-enable-flex-matching nil)
(setq ido-create-new-buffer 'always)
(setq ido-everywhere t)
(setq ido-vertical-define-keys 'C-n-and-C-p-only)
(ido-mode 1)
(ido-vertical-mode 1)
;(setq ido-file-extensions-order '(".org" ".txt" ".py" ".emacs" ".xml" ".el" ".ini" ".cfg" ".cnf"))

(defun bind-ido-keys ()
  (define-key ido-completion-map (kbd "C-l") 'ido-up-directory))
(add-hook 'ido-setup-hook #'bind-ido-keys)
;https://emacs.stackexchange.com/questions/3729/how-do-i-bind-keys-in-ido

(require 'golden-ratio-scroll-screen)
(global-set-key (kbd "M-v") 'golden-ratio-scroll-screen-down)
(global-set-key (kbd "C-v") 'golden-ratio-scroll-screen-up)

(global-set-key (kbd "C-x C-b") 'eval-buffer)

(require 'helm-config)
;(helm-mode 1)

;(define-key helm-map (kbd "<tab>") 'helm-execute-persistent-action)

(global-set-key (kbd "M-x") 'helm-M-x)
;(global-set-key (kbd "C-x b") 'helm-buffers-list)
;(global-set-key (kbd "C-x r b") 'helm-bookmarks)
;(global-set-key (kbd "M-y") 'helm-show-kill-ring)
;(global-set-key (kbd "C-x C-f") 'helm-find-files)
;(global-set-key (kbd "C-x p") 'package-list-packages)

;(set-default-font "Liberation Mono 18")
;(set-default-font "Fira Code 18")
(set-default-font "Hack Nerd Font 18")

(setq custom-safe-themes t)
(add-to-list 'custom-theme-load-path "~/.emacs.d/themes")
(add-hook 'after-init-hook (lambda () (load-theme 'xresources)))

(defun my/insert-line-before (times)
  "Inserts a newline(s) above the line containing the cursor."
  (interactive "p")
  (save-excursion
    (move-beginning-of-line 1)
    (newline)))

(global-set-key (kbd "C-S-o")
		'my/insert-line-before)

(setq package-archives
     '(("gnu" . "https://elpa.gnu.org/packages/")
       ("marmalade" . "https://marmalade-repo.org/packages/")
       ("melpa" . "https://melpa.org/packages/")))
