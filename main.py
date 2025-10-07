import dearpygui.dearpygui as dpg
import comp151Colors
dpg.create_context()
dpg.create_viewport(title="Cat", width=1000, height=1500)
with dpg.window(label="Cat", width=1000, height=1500):
    with dpg.drawlist(width=1000, height=1500):
        dpg.draw_arrow((750, 620), (500, 670), color=comp151Colors.GRAY, thickness=5)
        dpg.draw_rectangle((350, 420), (600, 700), fill=comp151Colors.GRAY)
        dpg.draw_triangle((470, 200), (400, 200), (425, 140),
                          color=comp151Colors.GRAY, thickness=10, fill=comp151Colors.PINK)
        dpg.draw_triangle((550, 200), (480, 200), (525, 140),
                          color=comp151Colors.GRAY, thickness=10, fill=comp151Colors.PINK)
        dpg.draw_circle((480, 320), 150, fill=comp151Colors.GRAY)
        dpg.draw_triangle((450, 330), (500, 330), (475, 360),
                          fill=comp151Colors.PINK)
        dpg.draw_triangle((380, 520), (420, 520), (400, 600),
                          fill=comp151Colors.LIGHT_GREY)
        dpg.draw_triangle((530, 520), (570, 520), (550, 600),
                          fill=comp151Colors.LIGHT_GREY)
        dpg.draw_circle((430, 260), 30, fill=comp151Colors.GREEN)
        dpg.draw_circle((520, 260), 30, fill=comp151Colors.GREEN)
        dpg.draw_polyline([(350, 320), (250, 320)], color=comp151Colors.WHITE, thickness=5)
        dpg.draw_polyline([(350, 340), (250, 340)], color=comp151Colors.WHITE, thickness=5)
        dpg.draw_polyline([(580, 320), (680, 320)], color=comp151Colors.WHITE, thickness=5)
        dpg.draw_polyline([(580, 340), (680, 340)], color=comp151Colors.WHITE, thickness=5)
        dpg.draw_text((40, 550), "Grace Chesebro",
                      color=comp151Colors.LIGHT_PURPLE, size=32)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()