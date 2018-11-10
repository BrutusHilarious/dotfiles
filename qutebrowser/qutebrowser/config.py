## Qutebrowser

config.load_autoconfig()

c.downloads.location.directory = '/home/evan/downloads'
#c.content.cookies.accept = 'never'
c.content.cookies.store = False

#css = '~/_code/qutebrowser-userstyles.css'
#c.content.user_stylesheets = css

#c.content.pdfjs = True

c.messages.timeout = 1000

c.url.start_pages = "https://www.google.com"

c.url.searchengines = {
    "DEFAULT": "https://www.google.com/search?q={}"
}

### Zoom Level ###

c.zoom.default = '150%'

### Fonts ###

## Font used in the completion categories.
## Type: Font
c.fonts.completion.category = 'bold 20pt monospace'

## Font used in the completion widget.
## Type: Font
c.fonts.completion.entry = '20pt monospace'

## Font used for the debugging console.
## Type: QtFont
c.fonts.debug_console = '20pt monospace'

## Font used for the downloadbar.
## Type: Font
c.fonts.downloads = '20pt monospace'

## Font used for the hints.
## Type: Font
c.fonts.hints = 'bold 30pt monospace'

## Font used in the keyhint widget.
## Type: Font
c.fonts.keyhint = '20pt monospace'

## Font used for error messages.
## Type: Font
c.fonts.messages.error = '20pt monospace'

## Font used for info messages.
## Type: Font
c.fonts.messages.info = '20pt monospace'

## Font used for warning messages.
## Type: Font
c.fonts.messages.warning = '20pt monospace'

## Default monospace fonts. Whenever "monospace" is used in a font
## setting, it's replaced with the fonts listed here.
## Type: Font
c.fonts.monospace = '"xos4 Terminus", Terminus, Monospace, "DejaVu Sans Mono", Monaco, "Bitstream Vera Sans Mono", "Andale Mono", "Courier New", Courier, "Liberation Mono", monospace, Fixed, Consolas, Terminal'

## Font used for prompts.
## Type: Font
c.fonts.prompts = '20pt sans-serif'

## Font used in the statusbar.
## Type: Font
c.fonts.statusbar = '20pt monospace'

## Font used in the tab bar.
## Type: QtFont
c.fonts.tabs = '20pt monospace'

## Font family for cursive fonts.
## Type: FontFamily
c.fonts.web.family.cursive = ''

## Font family for fantasy fonts.
## Type: FontFamily
c.fonts.web.family.fantasy = ''

## Font family for fixed fonts.
## Type: FontFamily
c.fonts.web.family.fixed = ''

## Font family for sans-serif fonts.
## Type: FontFamily
c.fonts.web.family.sans_serif = ''

## Font family for serif fonts.
## Type: FontFamily
c.fonts.web.family.serif = ''

## Font family for standard fonts.
## Type: FontFamily
c.fonts.web.family.standard = ''

## The default font size for regular text.
## Type: Int
c.fonts.web.size.default = 18

## The default font size for fixed-pitch text.
## Type: Int
c.fonts.web.size.default_fixed = 18

## The hard minimum font size.
## Type: Int
c.fonts.web.size.minimum = 18

## The minimum logical font size that is applied when zooming out.
## Type: Int
#c.fonts.web.size.minimum_logical = 

### end Fonts ###

### Custom Settings ###
#config.bind('<Ctrl-\>', 'config-source', mode='normal')

### Custom Colors ###

import subprocess
def read_xresources(prefix):
    props = {}
    x = subprocess.run(['xrdb', '-query'], stdout=subprocess.PIPE)
    lines = x.stdout.decode().split('\n')
    for line in filter(lambda l : l.startswith(prefix), lines):
        prop, _, value = line.partition(':\t')
        props[prop] = value
    return props
xresources = read_xresources('*')

## Hints ##
c.colors.hints.bg = xresources['*.color10']
c.colors.hints.fg = '#FFFFFF'
c.hints.border = '2px solid #FFFFFF'
c.colors.hints.match.fg = xresources['*.color15']
c.colors.keyhint.bg = '#000'
c.colors.keyhint.fg = xresources['*.color10']
c.colors.keyhint.suffix.fg = xresources['*.color15']
##

## Completion Categories ##
c.colors.completion.category.bg = xresources['*.color10']
c.colors.completion.category.fg = '#FFF'
c.colors.completion.category.border.bottom = '#000'
c.colors.completion.category.border.top = '#000'
c.colors.completion.fg = '#FFF'

c.colors.completion.even.bg = '#000'
c.colors.completion.odd.bg = '#000'

#c.colors.completion.scrollbar.fg = ''

c.colors.completion.match.fg = xresources['*.color6']

#c.colors.downloads.bar.bg = ''
#c.colors.downloads.error.bg = ''
#c.colors.downloads.start.bg = ''
#c.colors.downlaods.start.fg = ''
#c.colors.downloads.stop.bg = ''
#c.colors.downloads.stop.fg = ''
#c.colors.downloads.system.bg = ''
#c.colors.downloads.system.fg = ''

#c.colors.completion.item.selected.bg = xresources['*.color6']
c.colors.completion.item.selected.bg = '#c0392b'  
c.colors.completion.item.selected.fg = '#FFF'
c.colors.completion.item.selected.border.bottom = '#000'
c.colors.completion.item.selected.border.top = '#000'

#c.colors.completion.match.fg = '#000'

#c.colors.keyhint.suffix.fg = ''

## Messages ##
c.colors.messages.error.bg = '#c0392b'
#c.colors.messages.error.fg = ''
#c.colors.messages.error.border = ''
c.colors.messages.info.bg = '#c0392b'
#c.colors.messages.info.fg = ''
c.colors.messages.info.border = '#000'
c.colors.messages.warning.bg = '#c0392b'
#c.colors.messages.warning.fg = ''
#c.colors.messages.warning.border = ''
##

## Colors: Prompts ##
#c.colors.prompts.bg = ''
#c.colors.prompts.fg = ''
#c.colors.prompts.border = ''
#c.colors.prompts.selected.bg = ''

## Colors: Statusbar ##
#c.colors.statusbar.caret.bg =
#c.colors.statusbar.caret.fg =
#c.colors.statusbar.caret.selection.bg =
#c.colors.statusbar.caret.selection.fg =

c.colors.statusbar.command.bg = xresources['*.color10']
#c.colors.statusbar.command.fg = ''
#c.colors.statusbar.command.private.bg = ''
#c.colors.statusbar.command.private.fg = ''

#c.colors.statusbar.insert.bg = xresources['*.color10']
c.colors.statusbar.insert.bg = '#c0392b'
#c.colors.statusbar.insert.fg = ''

c.colors.statusbar.normal.bg = xresources['*.color6']
#c.colors.statusbar.normal.fg = xresources['*.color10']

#c.colors.statusbar.passthrough.bg = ''
#c.colors.statusbar.passthrough.fg = ''

#c.colors.statusbar.private.bg = ''
#c.colors.statusbar.private.fg = ''

#c.colors.statusbar.progress.bg = ''

##c.colors.statusbar.url.fg = '#FFF'
#c.colors.statusbar.url.hover.fg = ''
#c.colors.statusbar.url.success.http.fg = ''
#c.colors.statusbar.url.success.https.fg = '#27AE60'
#c.colors.statusbar.url.warn.fg = ''
##

## Colors - Tabs ##
c.colors.tabs.bar.bg = '#000'
c.colors.tabs.even.bg = '#000'
#c.colors.tabs.even.fg = ''
#c.colors.tabs.indicator.error = ''
#c.colors.tabs.indicator.start = ''
#c.colors.tabs.indicator.stop = ''
#c.colors.tabs.indicator.system = ''
c.colors.tabs.odd.bg = '#000'
#c.colors.tabs.odd.fg = ''
c.colors.tabs.selected.even.bg = xresources['*.color6']
#c.colors.tabs.selected.even.fg = ''
c.colors.tabs.selected.odd.bg = xresources['*.color6']
#c.colors.tabs.selected.odd.fg = ''
##

#c.colors.webpage.bg = '#000'

### Misc Settings
c.content.frame_flattening = True
c.content.geolocation = False
c.messages.timeout = 10000
#c.content.developer_extras = True
c.content.headers.do_not_track = True
###
### Custom Keybindings ###

# Scroll Page - Up
config.unbind('<k>', mode='normal')
config.bind('<Ctrl-p>', 'scroll up')

# Scroll Page - Down
config.unbind('<j>', mode='normal')
config.bind('<Ctrl-n>', 'scroll down')

# Scroll Down One Page
config.unbind('<Ctrl-v>', mode='normal')
config.bind('<Ctrl-v>', 'scroll-page 0 1')

# Scroll Up One Page
config.bind('<Alt-v>', 'scroll-page 0 -1')

# Enter Command
config.unbind('<:>', mode='normal')
config.bind('<Alt-x>', 'set-cmd-text :')

# Tabs - General
config.unbind('<Ctrl-PgDown>', mode='normal')
config.unbind('<Ctrl-PgUp>', mode='normal')
config.unbind('J', mode='normal')
config.unbind('T', mode='normal')

# Tab - Focus*
config.bind('<Ctrl-o>', 'tab-focus')

# Next Tab
#config.bind('<Ctrl-o>', 'tab-next')
config.bind('<Alt-n>', 'tab-next')
config.bind('<Alt-p>', 'tab-prev')

# Previous Tab
# I might need better preferred s for tab cycling.

### Download Youtube Video ~/downloads ###
config.bind('dyv', 'spawn youtube-dl {url} &')
config.bind('dya', 'spawn youtube-dl --extract-audio --format m4a {url} &')
###

#config.bind('m', 'spawn mpv {url}')

### Unbind 'save' ###
#config.unbind('s', mode='normal')
###

### Clear All Messages ###
config.bind('cm', 'clear-messages')
###

### Open Quickmark in New Tab ###

###

# Go Back
config.unbind('H', mode='normal')
config.bind('<Ctrl-b>', 'back')

# Scroll to Percentage
config.unbind('G', mode='normal')
config.bind('<Alt-,>', 'scroll-to-perc 0', mode='normal')
config.bind('<Alt-.>', 'scroll-to-perc 100', mode='normal')

# Kill Current Window
config.unbind('d', mode='normal')
config.unbind('k', mode='normal')
config.bind('<Ctrl-k>', 'tab-close', mode='normal')

# Open URL
config.unbind('o', mode='normal')
config.bind('<Ctrl-f>', 'set-cmd-text -s :open', mode='normal')
# Other open flags: tab: -t, window: -w, secure: -s, private: -p

# Yank
#config.unbind('yy', mode='normal')
#config.bind('Alt-w', 'yank')

## Leave Mode: ESC
#config.unbind('Escape', mode='insert')
#config.unbind('Escape', mode='normal')
config.bind('<Ctrl-g>', 'leave-mode', mode='insert')
#config.bind('<Ctrl-g>', 'leave-mode', mode='normal')
config.bind('<Ctrl-g>', 'leave-mode', mode='command')
config.bind('<Ctrl-g>', 'leave-mode', mode='hint')
config.bind('<Ctrl-g>', 'leave-mode', mode='prompt')
config.bind('<Ctrl-g>', 'leave-mode', mode='passthrough')
config.bind('<Ctrl-g>', 'leave-mode', mode='yesno')
config.bind('<Ctrl-g>', 'leave-mode', mode='caret')
config.bind('<Ctrl-g>', 'leave-mode', mode='register')


#config.bind('<Ctrl-g>', 'leave-mode', mode='search')

# Search
#config.unbind('/', mode='normal')
#config.unbind('<Ctrl-s>', mode='normal')
#config.unbind('<Ctrl-r>', mode='normal')
#config.bind('<Ctrl-s>', 'search', mode='normal')
#config.bind('<Ctrl-r>', 'search --reverse', mode='normal')
#c.search.ignore_case = 'smart'
config.bind('<Ctrl-s>', 'set-cmd-text -s :search ', mode='normal')

# Passthrough Mode

## Editor Mode
#c.editor.command = ['emacs', '-Q -nw --color', '{file}']
#c.editor.command = ['urxvt', 'emacs', '{file}']

#### Caret Mode: Rebindings & Settings ####

### Enter Caret Mode ###
config.unbind('v', mode='normal')
config.bind('<Ctrl-Space>', 'enter-mode caret')
###

### Toggle Selection ###
config.bind('<Ctrl-Space>', 'toggle-selection', mode='caret')
###

### Move To: Next Line ###
config.unbind('j', mode='caret')
config.bind('<Ctrl-n>', 'move-to-next-line', mode='caret')
###

### Move To: Previous Line ###
config.unbind('k', mode='caret')
config.bind('<Ctrl-p>', 'move-to-prev-line', mode='caret')
###

### Move To: Next Character ###
config.unbind('l', mode='caret')
config.bind('<Ctrl-f>', 'move-to-next-char', mode='caret')
###

### Move To: Previous Character ###
config.unbind('h', mode='caret')
config.bind('<Ctrl-b>', 'move-to-prev-char', mode='caret')
###

### Yank Selection ###
config.unbind('y', mode='caret')
config.bind('<Alt-w>', 'yank selection', mode='caret')
###

### Move To: Next Word ###
config.unbind('w', mode='caret')
config.bind('<Alt-f>', 'move-to-next-word', mode='caret')
###

### Move To: Previous Word ###
config.unbind('b', mode='caret')
config.bind('<Alt-b>', 'move-to-prev-word', mode='caret')
###

### Move To: End of Word ###
config.unbind('e', mode='caret')
config.bind('<Alt-e>', 'move-to-end-of-word', mode='caret')
###

### Move To: Start of Document ###
config.unbind('gg', mode='caret')
config.bind('<Alt-,>', 'move-to-start-of-document', mode='caret')
###

### Move To: End of Document ###
config.unbind('G', mode='caret')
config.bind('<Alt-.>', 'move-to-end-of-document', mode='caret')
###

### Move To: Start of Line ###
config.unbind('0', mode='caret')
config.bind('<Ctrl-a>', 'move-to-start-of-line', mode='caret')
###

### Move To: End of Line ###
config.unbind('$', mode='caret')
config.bind('<Ctrl-e>', 'move-to-end-of-line', mode='caret')
###

#### END ####

#config.unbind('j', mode='caret')
#config.bind('<Ctrl-n>', 'down-line', mode='caret')

#config.unbind('y', 'yank', mode='caret')
#config.bind('<Alt-w>, yank, mode='caret')



###
