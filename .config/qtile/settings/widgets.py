from libqtile import widget, bar, qtile
#from libqtile.config import Screen
from theme import colors,colors2
from libqtile.widget import net, cpu

def separator():
    return widget.Sep( linewidth=0, padding=10, background=colors2.bar)

def powerline_cir_right(bg,fg):
    return widget.TextBox(
        foreground = fg,
        background = bg,
        text = ' ', # nf-ple-right_half_circle_thick
        padding = -0.5,
        fontsize = 30
    )

def powerline_cir_left(bg,fg):
    return widget.TextBox(
        foreground = fg,
        background = bg,
        text = '', # nf-ple-left_half_circle_thick
        fontsize = 30,
        padding = -0.5,
    )

def powerline(fg,bg):
    return widget.TextBox(
        foreground = fg,
        background = bg,
        text = '', # Icon: nf-oct-triangle_left
        padding = -3
    )

def cpu(bg,fg):
    return widget.CPU(
        background = bg,
        foreground = fg,
        format = ' {freq_current}GHz  {load_percent}%',
    )

def Net(bg, fg):
    return widget.Net(
        background = bg,
        foreground = fg,
        format = '直 {down} ↓↑ {up}',
    )

def sound(fg):
  return widget.TextBox(
        text = ' 墳  ',
        foreground = fg,
        mouse_callbacks = {
        'Button1': lambda: qtile.cmd_spawn("amixer sset Master toggle"),
        'Button4': lambda: qtile.cmd_spawn("amixer -D pulse sset Master 2+"),
        'Button5': lambda: qtile.cmd_spawn("amixer -D pulse sset Master 2%-"),
        },
    )

def Memory(bg,fg):
    return widget.Memory(
        font='UbuntuMono Nerd Font',
        color=["#fffff"],
        foreground = fg,
        background = bg,
        format = '{MemUsed: .0f}{mm} //{MemTotal: .0f}{mm} ',
        measure_mem = "M",
        measure_swap = "M",
    )

def CurrentLayout(bg,fg):
    return widget.CurrentLayout(
        background = bg,
        foreground = fg,
    )

def CurrentLayoutIcon(bg,fg):
    return widget.CurrentLayoutIcon(
        background = bg,
        foreground = fg,
        scale = 0.65
    )

def Clock(bg,fg):
    return widget.Clock(
        format='  %Y/%m/%d %a   %I:%M:%S %p ',
        background = bg,
        foreground = fg,
    )

def Systray(bg):
    return widget.Systray(
        background = bg,
    ),


primary_widgets = [
     widget.GroupBox(
        foreground=None,
        background=colors2.bar,
        font='UbuntuMono Nerd Font',
        fontsize=19,
        padding_y=8,
        padding_x=10,
        active=colors.active,
        inactive=colors.inactive,
        rounded=True,
        highlight_method='block',
        urgent_border=colors.urgent,
        this_current_screen_border=colors.dark,
        this_screen_border=colors.dark,
        disable_drag=True
    ),

    CurrentLayoutIcon(colors2.yellow, colors.dark),
    CurrentLayout(colors2.yellow, colors.dark),
    separator(),
    powerline_cir_left(colors2.bar, colors2.over_board),
    widget.TextBox(
        background=colors2.over_board,
        foreground=colors.dark,
    ),
    Clock(colors2.over_board,colors.dark),   
    powerline_cir_right(colors2.bar, colors2.over_board),
    separator(),
    widget.Systray(),
]

secondary_widgets = [
    widget.GroupBox(
        foreground=colors.light,
        background=colors.light,
        font='UbuntuMono Nerd Font',
        fontsize=19,
        margin_y=3,
        margin_x=10,
        padding_y=8,
        padding_x=10,
        borderwidth=1,
        active=colors.active,
        inactive=colors.inactive,
        rounded=False,
        highlight_method='block',
        urgent_border=colors.urgent,
        this_current_screen_border=colors.dark,
        this_screen_border=colors.dark,
        disable_drag=True
    ),
    widget.WindowName(
        foreground=colors.light,
        background=colors.light,
        fontsize=13,
        font="UbuntuMono Nerd Font",
    ),
    powerline(colors2.yellow,colors.light),      
    CurrentLayoutIcon(colors2.yellow, colors.dark),
    CurrentLayout(colors2.yellow, colors.dark),
    powerline(colors2.blue,colors2.yellow),
    widget.TextBox(
        background=colors2.blue,
        foreground=colors.dark,
    ),
    Clock(colors2.blue,colors.dark),   
    powerline(colors.light,colors2.blue),
]

widget_defaults = {
    'font': 'Ubuntu Mono Nerd Font',
    'fontsize': 18,
    'padding': 1
}
extension_defaults = widget_defaults.copy()
