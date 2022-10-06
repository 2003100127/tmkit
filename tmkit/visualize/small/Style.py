from pymol import cmd


def style(sm_style="sticks"):
    cmd.hide(
        representation="spheres",
        selection='sm'
    )
    cmd.show(
        representation=sm_style,
        selection='sm'
    )