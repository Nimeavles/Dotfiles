from libqtile import layout
from libqtile.config import Match
from theme import colors

layout_conf = {
  'border_focus': colors.focus[0],
  'border_width': 1,
  'margin': 4
}

layouts = [
 layout.Max(),
 layout.MonadTall(**layout_conf),
 #layout.MonadWide(**layout_conf),
 layout.Bsp(**layout_conf),
 #layout.Matrix(columns=2, **layout_conf),
 layout.RatioTile(**layout_conf),
 # layout.Columns(),
 # layout.Tile(),
 # layout.TreeTab(),
 # layout.VerticalTile(),
 # layout.Zoomy(),
]
