from libqtile import hook
from os import path
import subprocess

from settings.keys import *
from settings.groups import *
from settings.layouts import *
from settings.widgets import *
from settings.mouse import *
from settings.path import *
#from settings.screens import *

@hook.subscribe.startup_once
def autostart():
    subprocess.call([path.join(qtile_path, 'autostart.sh')])

main = None
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
auto_fullscreen = True
focus_on_window_activation = 'urgent'
wmname = 'Qtile'

