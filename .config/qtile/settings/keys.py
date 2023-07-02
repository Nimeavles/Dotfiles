from libqtile.config import Key
from libqtile.command import lazy

mod = "mod4"

keys = [
    # Switch between windows
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "k", lazy.layout.shuffle_down(),desc="Move window down"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes

    Key([mod], "m", lazy.spawn("rofi -show drun"), desc="Run rofi"),
    Key([mod, "shift"], "m", lazy.spawn("rofi -show emoji"), desc="Run rofi emoji"),

    Key([mod, "control"], "s", lazy.spawn("shutdown now"), desc="Shutdown the system"),
    Key([mod, "control"], "h", lazy.spawn("sudo pm-suspend"), desc="Suspend the System"),
    
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "Return", lazy.spawn("kitty"), desc="Launch terminal"),

    #Thunar
    Key([mod], "e", lazy.spawn("thunar")),

    #screenshots
    Key([mod, "shift"], "s", lazy.spawn("flameshot gui")),

    #Vscode
    Key([mod],"v", lazy.spawn("code")),

    #Discord
    Key([mod], "d", lazy.spawn("discord")),
]
