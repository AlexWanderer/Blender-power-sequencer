import bpy
import os

def kmi_props_setattr(kmi_props, attr, value):
    try:
        setattr(kmi_props, attr, value)
    except AttributeError:
        print("Warning: property '%s' not found in keymap item '%s'" %
              (attr, kmi_props.__class__.__name__))
    except Exception as e:
        print("Warning: %r" % e)

wm = bpy.context.window_manager
kc = wm.keyconfigs.new(os.path.splitext(os.path.basename(__file__))[0])

# Map View2D
km = kc.keymaps.new('View2D', space_type='EMPTY', region_type='WINDOW', modal=False)

kmi = km.keymap_items.new('sequencer.tf_position', 'G', 'PRESS')
kmi = km.keymap_items.new('sequencer.tf_position', 'G', 'PRESS', alt=True)
kmi = km.keymap_items.new('sequencer.tf_scale', 'S', 'PRESS')
kmi = km.keymap_items.new('sequencer.tf_scale', 'S', 'PRESS', alt=True)
kmi = km.keymap_items.new('sequencer.tf_rotation', 'R', 'PRESS')
kmi = km.keymap_items.new('sequencer.tf_rotation', 'R', 'PRESS', alt=True)
kmi = km.keymap_items.new('sequencer.tf_call_menu', 'I', 'PRESS')
kmi = km.keymap_items.new('sequencer.tf_select', 'A', 'PRESS')
kmi = km.keymap_items.new('sequencer.tf_draw_alpha', 'Q', 'PRESS')
kmi = km.keymap_items.new('sequencer.tf_draw_alpha', 'Q', 'PRESS', alt=True)
kmi = km.keymap_items.new('sequencer.tf_crop', 'C', 'PRESS')
kmi = km.keymap_items.new('sequencer.tf_crop', 'C', 'PRESS', alt=True)
kmi = km.keymap_items.new('sequencer.tf_select', 'RIGHTMOUSE', 'PRESS')
kmi = km.keymap_items.new('sequencer.tf_select', 'RIGHTMOUSE', 'PRESS', shift=True)
kmi = km.keymap_items.new('sequencer.tf_call_menu_layers', 'RIGHTMOUSE', 'PRESS', alt=True)
kmi = km.keymap_items.new('sequencer.tf_call_menu_layers', 'RIGHTMOUSE', 'PRESS', shift=True, alt=True)
kmi = km.keymap_items.new('sequencer.tf_set_cursor2d', 'RIGHTMOUSE', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('view2d.scroller_activate', 'LEFTMOUSE', 'PRESS')
kmi = km.keymap_items.new('view2d.scroller_activate', 'MIDDLEMOUSE', 'PRESS')
kmi = km.keymap_items.new('view2d.pan', 'MIDDLEMOUSE', 'PRESS')
kmi = km.keymap_items.new('view2d.pan', 'MIDDLEMOUSE', 'PRESS', shift=True)
kmi = km.keymap_items.new('view2d.pan', 'TRACKPADPAN', 'ANY')
kmi = km.keymap_items.new('view2d.scroll_right', 'WHEELDOWNMOUSE', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('view2d.scroll_left', 'WHEELUPMOUSE', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('view2d.scroll_down', 'WHEELDOWNMOUSE', 'PRESS', shift=True)
kmi = km.keymap_items.new('view2d.scroll_up', 'WHEELUPMOUSE', 'PRESS', shift=True)
kmi = km.keymap_items.new('view2d.ndof', 'NDOF_MOTION', 'ANY')
kmi = km.keymap_items.new('view2d.zoom_out', 'WHEELOUTMOUSE', 'PRESS')
kmi = km.keymap_items.new('view2d.zoom_in', 'WHEELINMOUSE', 'PRESS')
kmi = km.keymap_items.new('view2d.zoom_out', 'NUMPAD_MINUS', 'PRESS')
kmi = km.keymap_items.new('view2d.zoom_in', 'NUMPAD_PLUS', 'PRESS')
kmi = km.keymap_items.new('view2d.zoom', 'TRACKPADPAN', 'ANY', ctrl=True)
kmi = km.keymap_items.new('view2d.smoothview', 'TIMER1', 'ANY', any=True)
kmi = km.keymap_items.new('view2d.scroll_down', 'WHEELDOWNMOUSE', 'PRESS')
kmi = km.keymap_items.new('view2d.scroll_up', 'WHEELUPMOUSE', 'PRESS')
kmi = km.keymap_items.new('view2d.scroll_right', 'WHEELDOWNMOUSE', 'PRESS')
kmi = km.keymap_items.new('view2d.scroll_left', 'WHEELUPMOUSE', 'PRESS')
kmi = km.keymap_items.new('view2d.zoom', 'MIDDLEMOUSE', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('view2d.zoom', 'TRACKPADZOOM', 'ANY')
kmi = km.keymap_items.new('view2d.zoom_border', 'B', 'PRESS', shift=True)

# Map Sequencer
km = kc.keymaps.new('Sequencer', space_type='SEQUENCE_EDITOR', region_type='WINDOW', modal=False)

kmi = km.keymap_items.new('wm.call_menu', 'P', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'name', 'vseqf.quickparents_menu')
kmi = km.keymap_items.new('wm.call_menu', 'Z', 'PRESS')
kmi_props_setattr(kmi.properties, 'name', 'vseqf.quickzooms_menu')
kmi = km.keymap_items.new('wm.call_menu', 'M', 'PRESS', alt=True)
kmi_props_setattr(kmi.properties, 'name', 'vseqf.quickmarkers_menu')
kmi = km.keymap_items.new('sequencer.refresh_all', 'R', 'PRESS', shift=True)
kmi = km.keymap_items.new('sequencer.select_all', 'A', 'PRESS')
kmi_props_setattr(kmi.properties, 'action', 'TOGGLE')
kmi = km.keymap_items.new('sequencer.select_all', 'I', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'action', 'INVERT')
kmi = km.keymap_items.new('sequencer.cut', 'K', 'PRESS')
kmi_props_setattr(kmi.properties, 'type', 'SOFT')
kmi = km.keymap_items.new('sequencer.cut', 'K', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'type', 'HARD')
kmi = km.keymap_items.new('power_sequencer.toggle_sequences_muted', 'H', 'PRESS')
kmi = km.keymap_items.new('power_sequencer.toggle_sequences_muted', 'H', 'PRESS', alt=True)
kmi_props_setattr(kmi.properties, 'use_unselected', True)
kmi = km.keymap_items.new('sequencer.lock', 'L', 'PRESS', shift=True)
kmi = km.keymap_items.new('sequencer.unlock', 'L', 'PRESS', shift=True, alt=True)
kmi = km.keymap_items.new('sequencer.reassign_inputs', 'R', 'PRESS')
kmi = km.keymap_items.new('sequencer.reload', 'R', 'PRESS', alt=True)
kmi = km.keymap_items.new('sequencer.reload', 'R', 'PRESS', shift=True, alt=True)
kmi_props_setattr(kmi.properties, 'adjust_length', True)
kmi = km.keymap_items.new('sequencer.offset_clear', 'O', 'PRESS', alt=True)
kmi = km.keymap_items.new('sequencer.duplicate_move', 'D', 'PRESS', shift=True)
kmi = km.keymap_items.new('power_sequencer.delete_direct', 'X', 'PRESS')
kmi = km.keymap_items.new('sequencer.paste', 'V', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('sequencer.images_separate', 'Y', 'PRESS')
kmi = km.keymap_items.new('sequencer.meta_toggle', 'TAB', 'PRESS')
kmi = km.keymap_items.new('sequencer.meta_make', 'G', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('sequencer.meta_separate', 'G', 'PRESS', alt=True)
kmi = km.keymap_items.new('sequencer.view_selected', 'NUMPAD_PERIOD', 'PRESS')
kmi = km.keymap_items.new('sequencer.view_selected', 'HOME', 'PRESS', shift=True)
kmi = km.keymap_items.new('sequencer.view_selected', 'DEL', 'PRESS', shift=True)
kmi = km.keymap_items.new('sequencer.strip_jump', 'RIGHT_BRACKET', 'PRESS')
kmi_props_setattr(kmi.properties, 'next', True)
kmi_props_setattr(kmi.properties, 'center', False)
kmi = km.keymap_items.new('sequencer.strip_jump', 'LEFT_BRACKET', 'PRESS')
kmi_props_setattr(kmi.properties, 'next', False)
kmi_props_setattr(kmi.properties, 'center', False)
kmi = km.keymap_items.new('sequencer.strip_jump', 'RIGHT_BRACKET', 'PRESS', alt=True)
kmi_props_setattr(kmi.properties, 'next', True)
kmi_props_setattr(kmi.properties, 'center', True)
kmi = km.keymap_items.new('sequencer.strip_jump', 'LEFT_BRACKET', 'PRESS', alt=True)
kmi_props_setattr(kmi.properties, 'next', False)
kmi_props_setattr(kmi.properties, 'center', True)
kmi = km.keymap_items.new('sequencer.swap', 'LEFT_ARROW', 'PRESS', alt=True)
kmi_props_setattr(kmi.properties, 'side', 'LEFT')
kmi = km.keymap_items.new('sequencer.swap', 'RIGHT_ARROW', 'PRESS', alt=True)
kmi_props_setattr(kmi.properties, 'side', 'RIGHT')
kmi = km.keymap_items.new('sequencer.gap_insert', 'EQUAL', 'PRESS', shift=True)
kmi = km.keymap_items.new('sequencer.snap', 'S', 'PRESS', shift=True)
kmi = km.keymap_items.new('power_sequencer.speed_up_sequence', 'S', 'PRESS', alt=True)
kmi = km.keymap_items.new('sequencer.cut_multicam', 'ONE', 'PRESS')
kmi_props_setattr(kmi.properties, 'camera', 1)
kmi = km.keymap_items.new('sequencer.cut_multicam', 'TWO', 'PRESS')
kmi_props_setattr(kmi.properties, 'camera', 2)
kmi = km.keymap_items.new('sequencer.cut_multicam', 'THREE', 'PRESS')
kmi_props_setattr(kmi.properties, 'camera', 3)
kmi = km.keymap_items.new('sequencer.cut_multicam', 'FOUR', 'PRESS')
kmi_props_setattr(kmi.properties, 'camera', 4)
kmi = km.keymap_items.new('sequencer.cut_multicam', 'FIVE', 'PRESS')
kmi_props_setattr(kmi.properties, 'camera', 5)
kmi = km.keymap_items.new('sequencer.cut_multicam', 'SIX', 'PRESS')
kmi_props_setattr(kmi.properties, 'camera', 6)
kmi = km.keymap_items.new('sequencer.cut_multicam', 'SEVEN', 'PRESS')
kmi_props_setattr(kmi.properties, 'camera', 7)
kmi = km.keymap_items.new('sequencer.cut_multicam', 'EIGHT', 'PRESS')
kmi_props_setattr(kmi.properties, 'camera', 8)
kmi = km.keymap_items.new('sequencer.cut_multicam', 'NINE', 'PRESS')
kmi_props_setattr(kmi.properties, 'camera', 9)
kmi = km.keymap_items.new('sequencer.cut_multicam', 'ZERO', 'PRESS')
kmi_props_setattr(kmi.properties, 'camera', 10)
kmi = km.keymap_items.new('sequencer.select', 'SELECTMOUSE', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'extend', True)
kmi_props_setattr(kmi.properties, 'linked_handle', False)
kmi_props_setattr(kmi.properties, 'left_right', 'NONE')
kmi_props_setattr(kmi.properties, 'linked_time', False)
kmi = km.keymap_items.new('sequencer.select', 'SELECTMOUSE', 'PRESS', shift=True, alt=True)
kmi_props_setattr(kmi.properties, 'extend', True)
kmi_props_setattr(kmi.properties, 'linked_handle', True)
kmi_props_setattr(kmi.properties, 'left_right', 'NONE')
kmi_props_setattr(kmi.properties, 'linked_time', False)
kmi = km.keymap_items.new('sequencer.select', 'SELECTMOUSE', 'PRESS', alt=True)
kmi_props_setattr(kmi.properties, 'extend', False)
kmi_props_setattr(kmi.properties, 'linked_handle', True)
kmi_props_setattr(kmi.properties, 'left_right', 'NONE')
kmi_props_setattr(kmi.properties, 'linked_time', False)
kmi = km.keymap_items.new('sequencer.select', 'SELECTMOUSE', 'PRESS', shift=True, ctrl=True)
kmi_props_setattr(kmi.properties, 'extend', True)
kmi_props_setattr(kmi.properties, 'linked_handle', False)
kmi_props_setattr(kmi.properties, 'left_right', 'NONE')
kmi_props_setattr(kmi.properties, 'linked_time', True)
kmi = km.keymap_items.new('sequencer.select_more', 'NUMPAD_PLUS', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('sequencer.select_less', 'NUMPAD_MINUS', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('sequencer.select_linked_pick', 'L', 'PRESS')
kmi_props_setattr(kmi.properties, 'extend', False)
kmi = km.keymap_items.new('sequencer.select_linked_pick', 'L', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'extend', True)
kmi = km.keymap_items.new('sequencer.select_linked', 'L', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('power_sequencer.border_select', 'B', 'PRESS')
kmi = km.keymap_items.new('wm.call_menu', 'A', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'name', 'SEQUENCER_MT_add')
kmi = km.keymap_items.new('wm.call_menu', 'C', 'PRESS')
kmi_props_setattr(kmi.properties, 'name', 'SEQUENCER_MT_change')
kmi = km.keymap_items.new('sequencer.slip', 'S', 'PRESS')
kmi = km.keymap_items.new('wm.context_set_int', 'O', 'PRESS')
kmi_props_setattr(kmi.properties, 'data_path', 'scene.sequence_editor.overlay_frame')
kmi_props_setattr(kmi.properties, 'value', 0)
kmi = km.keymap_items.new('transform.seq_slide', 'G', 'PRESS')
kmi = km.keymap_items.new('transform.seq_slide', 'EVT_TWEAK_S', 'ANY')
kmi = km.keymap_items.new('transform.transform', 'E', 'PRESS')
kmi_props_setattr(kmi.properties, 'mode', 'TIME_EXTEND')
kmi = km.keymap_items.new('marker.add', 'M', 'PRESS')
kmi = km.keymap_items.new('marker.rename', 'M', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('sequencer.select_border', 'B', 'PRESS', shift=True)
kmi = km.keymap_items.new('power_sequencer.smart_snap', 'K', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'side', 'left')
kmi = km.keymap_items.new('power_sequencer.smart_snap', 'K', 'PRESS', alt=True)
kmi_props_setattr(kmi.properties, 'side', 'right')
kmi = km.keymap_items.new('power_sequencer.fade_strips', 'F', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'fade_type', 'left')
kmi = km.keymap_items.new('power_sequencer.fade_strips', 'F', 'PRESS', alt=True)
kmi_props_setattr(kmi.properties, 'fade_type', 'right')
kmi = km.keymap_items.new('power_sequencer.channel_offset', 'UP_ARROW', 'PRESS', alt=True)
kmi_props_setattr(kmi.properties, 'direction', 'up')
kmi = km.keymap_items.new('power_sequencer.channel_offset', 'DOWN_ARROW', 'PRESS', alt=True)
kmi_props_setattr(kmi.properties, 'direction', 'down')
kmi = km.keymap_items.new('power_sequencer.concatenate_strips', 'C', 'PRESS', shift=True)
kmi = km.keymap_items.new('power_sequencer.sound_toggle_waveform', 'W', 'PRESS')
kmi = km.keymap_items.new('power_sequencer.add_crossfade', 'C', 'PRESS', ctrl=True, alt=True)
kmi = km.keymap_items.new('sequencer.change_path', 'O', 'PRESS', ctrl=True, alt=True)
kmi_props_setattr(kmi.properties, 'filter_image', True)
kmi = km.keymap_items.new('power_sequencer.fade_strips', 'F', 'PRESS')
kmi_props_setattr(kmi.properties, 'fade_type', 'both')
kmi = km.keymap_items.new('power_sequencer.mouse_cut', 'ACTIONMOUSE', 'CLICK', ctrl=True)
kmi_props_setattr(kmi.properties, 'select_mode', 'smart')
kmi_props_setattr(kmi.properties, 'cut_mode', 'cut')
kmi_props_setattr(kmi.properties, 'auto_move_cursor', False)
kmi_props_setattr(kmi.properties, 'cursor_offset', 8)
kmi_props_setattr(kmi.properties, 'remove_gaps', True)
kmi = km.keymap_items.new('power_sequencer.mouse_cut', 'SELECTMOUSE', 'CLICK', ctrl=True)
kmi_props_setattr(kmi.properties, 'select_mode', 'smart')
kmi_props_setattr(kmi.properties, 'cut_mode', 'trim')
kmi_props_setattr(kmi.properties, 'cursor_offset', 8)
kmi_props_setattr(kmi.properties, 'remove_gaps', True)
kmi = km.keymap_items.new('power_sequencer.edit_crossfade', 'C', 'PRESS', alt=True)
kmi = km.keymap_items.new('power_sequencer.delete_direct', 'DEL', 'PRESS')
kmi = km.keymap_items.new('sequencer.gap_remove', 'BACK_SPACE', 'PRESS')
kmi_props_setattr(kmi.properties, 'all', True)
kmi = km.keymap_items.new('sequencer.select', 'SELECTMOUSE', 'PRESS')
kmi_props_setattr(kmi.properties, 'extend', False)
kmi_props_setattr(kmi.properties, 'linked_handle', False)
kmi_props_setattr(kmi.properties, 'left_right', 'NONE')
kmi_props_setattr(kmi.properties, 'linked_time', False)
kmi = km.keymap_items.new('power_sequencer.render_video', 'F12', 'PRESS', alt=True)
kmi_props_setattr(kmi.properties, 'use_proxies', False)
kmi_props_setattr(kmi.properties, 'preset', 'youtube')
kmi = km.keymap_items.new('power_sequencer.import_local_footage', 'I', 'PRESS', shift=True, ctrl=True)
kmi_props_setattr(kmi.properties, 'keep_audio', True)
kmi = km.keymap_items.new('power_sequencer.add_title_marker', 'M', 'PRESS', shift=True, ctrl=True)
kmi = km.keymap_items.new('power_sequencer.add_numbered_marker', 'M', 'PRESS', ctrl=True, alt=True)
kmi = km.keymap_items.new('sequencer.view_all', 'HOME', 'PRESS')
kmi = km.keymap_items.new('sequencer.view_selected', 'END', 'PRESS')
kmi = km.keymap_items.new('power_sequencer.add_transform_effect', 'T', 'PRESS')
kmi = km.keymap_items.new('power_sequencer.ripple_delete', 'X', 'PRESS', shift=True)
kmi = km.keymap_items.new('power_sequencer.preview_last_cut', 'P', 'PRESS', shift=True)
kmi = km.keymap_items.new('power_sequencer.mouse_cut', 'ACTIONMOUSE', 'PRESS', shift=True, ctrl=True)
kmi_props_setattr(kmi.properties, 'select_mode', 'cursor')
kmi_props_setattr(kmi.properties, 'cut_mode', 'cut')
kmi = km.keymap_items.new('power_sequencer.toggle_preview_selection', 'P', 'PRESS', ctrl=True, alt=True)
kmi = km.keymap_items.new('sequencer.select', 'RIGHT_ARROW', 'PRESS', ctrl=True, alt=True)
kmi_props_setattr(kmi.properties, 'left_right', 'RIGHT')
kmi_props_setattr(kmi.properties, 'linked_time', True)
kmi = km.keymap_items.new('sequencer.select', 'LEFT_ARROW', 'PRESS', ctrl=True, alt=True)
kmi_props_setattr(kmi.properties, 'left_right', 'LEFT')
kmi_props_setattr(kmi.properties, 'linked_time', True)
kmi = km.keymap_items.new('power_sequencer.mouse_cut', 'SELECTMOUSE', 'PRESS', ctrl=True, alt=True)
kmi_props_setattr(kmi.properties, 'select_mode', 'cursor')
kmi_props_setattr(kmi.properties, 'cut_mode', 'trim')
kmi_props_setattr(kmi.properties, 'remove_gaps', True)
kmi = km.keymap_items.new('power_sequencer.cycle_scenes', 'TAB', 'PRESS', shift=True)
kmi = km.keymap_items.new('power_sequencer.mouse_cut', 'ACTIONMOUSE', 'PRESS', shift=True, ctrl=True)
kmi = km.keymap_items.new('power_sequencer.mouse_cut', 'SELECTMOUSE', 'PRESS', ctrl=True, alt=True)
kmi = km.keymap_items.new('power_sequencer.grab_closest_handle_or_cut', 'G', 'PRESS', shift=True)
kmi = km.keymap_items.new('wm.call_menu', 'X', 'PRESS', alt=True)
kmi_props_setattr(kmi.properties, 'name', 'SEQUENCER_MT_power_sequencer_menu')
kmi = km.keymap_items.new('power_sequencer.change_playback_speed', 'ONE', 'PRESS')
kmi_props_setattr(kmi.properties, 'speed', 'normal')
kmi = km.keymap_items.new('power_sequencer.change_playback_speed', 'TWO', 'PRESS')
kmi_props_setattr(kmi.properties, 'speed', 'fast')
kmi = km.keymap_items.new('power_sequencer.change_playback_speed', 'THREE', 'PRESS')
kmi_props_setattr(kmi.properties, 'speed', 'faster')
kmi = km.keymap_items.new('power_sequencer.change_playback_speed', 'FOUR', 'PRESS')
kmi_props_setattr(kmi.properties, 'speed', 'double')
kmi = km.keymap_items.new('power_sequencer.change_playback_speed', 'FIVE', 'PRESS')
kmi_props_setattr(kmi.properties, 'speed', 'triple')
kmi = km.keymap_items.new('power_sequencer.deselect_handles_seq_slide', 'G', 'PRESS', ctrl=True, alt=True)
kmi = km.keymap_items.new('power_sequencer.copy_selection', 'C', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('power_sequencer.copy_selection', 'X', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'delete_selection', True)

# Map Screen
km = kc.keymaps.new('Screen', space_type='EMPTY', region_type='WINDOW', modal=False)

kmi = km.keymap_items.new('pillar.browser', 'A', 'PRESS', shift=True, ctrl=True, alt=True)
kmi = km.keymap_items.new('pillar.browser', 'A', 'PRESS', shift=True, ctrl=True, alt=True)
kmi = km.keymap_items.new('pillar.browser', 'A', 'PRESS', shift=True, ctrl=True, alt=True)
kmi = km.keymap_items.new('screen.animation_step', 'TIMER0', 'ANY', any=True)
kmi = km.keymap_items.new('screen.region_blend', 'TIMERREGION', 'ANY', any=True)
kmi = km.keymap_items.new('screen.screen_set', 'RIGHT_ARROW', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'delta', 1)
kmi = km.keymap_items.new('screen.screen_set', 'LEFT_ARROW', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'delta', -1)
kmi = km.keymap_items.new('screen.screen_full_area', 'UP_ARROW', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('screen.screen_full_area', 'DOWN_ARROW', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('screen.screen_full_area', 'SPACE', 'PRESS', shift=True)
kmi = km.keymap_items.new('screen.screen_full_area', 'F10', 'PRESS', alt=True)
kmi_props_setattr(kmi.properties, 'use_hide_panels', True)
kmi = km.keymap_items.new('screen.screenshot', 'F3', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('screen.screencast', 'F3', 'PRESS', alt=True)
kmi = km.keymap_items.new('screen.region_quadview', 'Q', 'PRESS', ctrl=True, alt=True)
kmi = km.keymap_items.new('screen.repeat_history', 'F3', 'PRESS')
kmi = km.keymap_items.new('screen.repeat_last', 'R', 'PRESS', shift=True)
kmi = km.keymap_items.new('screen.region_flip', 'F5', 'PRESS')
kmi = km.keymap_items.new('screen.redo_last', 'F6', 'PRESS')
kmi = km.keymap_items.new('script.reload', 'F8', 'PRESS')
kmi = km.keymap_items.new('file.execute', 'RET', 'PRESS')
kmi = km.keymap_items.new('file.execute', 'NUMPAD_ENTER', 'PRESS')
kmi = km.keymap_items.new('file.cancel', 'ESC', 'PRESS')
kmi = km.keymap_items.new('ed.undo', 'Z', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('ed.redo', 'Z', 'PRESS', shift=True, ctrl=True)
kmi = km.keymap_items.new('ed.undo_history', 'Z', 'PRESS', ctrl=True, alt=True)
kmi = km.keymap_items.new('render.render', 'F12', 'PRESS')
kmi_props_setattr(kmi.properties, 'use_viewport', True)
kmi = km.keymap_items.new('render.render', 'F12', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'animation', True)
kmi_props_setattr(kmi.properties, 'use_viewport', True)
kmi = km.keymap_items.new('render.view_cancel', 'ESC', 'PRESS')
kmi = km.keymap_items.new('render.view_show', 'F11', 'PRESS')
kmi = km.keymap_items.new('render.play_rendered_anim', 'F11', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('screen.userpref_show', 'U', 'PRESS', ctrl=True, alt=True)

# Map Frames
km = kc.keymaps.new('Frames', space_type='EMPTY', region_type='WINDOW', modal=False)

kmi = km.keymap_items.new('screen.frame_offset', 'RIGHT_ARROW', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'delta', 10)
kmi = km.keymap_items.new('screen.frame_offset', 'LEFT_ARROW', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'delta', -10)
kmi = km.keymap_items.new('screen.frame_offset', 'LEFT_ARROW', 'PRESS')
kmi_props_setattr(kmi.properties, 'delta', -1)
kmi = km.keymap_items.new('screen.frame_offset', 'RIGHT_ARROW', 'PRESS')
kmi_props_setattr(kmi.properties, 'delta', 1)
kmi = km.keymap_items.new('screen.frame_offset', 'WHEELDOWNMOUSE', 'PRESS', alt=True)
kmi_props_setattr(kmi.properties, 'delta', 1)
kmi = km.keymap_items.new('screen.frame_offset', 'WHEELUPMOUSE', 'PRESS', alt=True)
kmi_props_setattr(kmi.properties, 'delta', -1)
kmi = km.keymap_items.new('screen.frame_jump', 'RIGHT_ARROW', 'PRESS', shift=True, ctrl=True)
kmi_props_setattr(kmi.properties, 'end', True)
kmi = km.keymap_items.new('screen.frame_jump', 'LEFT_ARROW', 'PRESS', shift=True, ctrl=True)
kmi_props_setattr(kmi.properties, 'end', False)
kmi = km.keymap_items.new('screen.keyframe_jump', 'UP_ARROW', 'PRESS')
kmi_props_setattr(kmi.properties, 'next', True)
kmi = km.keymap_items.new('screen.keyframe_jump', 'DOWN_ARROW', 'PRESS')
kmi_props_setattr(kmi.properties, 'next', False)
kmi = km.keymap_items.new('screen.keyframe_jump', 'MEDIA_LAST', 'PRESS')
kmi_props_setattr(kmi.properties, 'next', True)
kmi = km.keymap_items.new('screen.keyframe_jump', 'MEDIA_FIRST', 'PRESS')
kmi_props_setattr(kmi.properties, 'next', False)
kmi = km.keymap_items.new('screen.animation_play', 'A', 'PRESS', alt=True)
kmi = km.keymap_items.new('screen.animation_play', 'A', 'PRESS', shift=True, alt=True)
kmi_props_setattr(kmi.properties, 'reverse', True)
kmi = km.keymap_items.new('screen.animation_cancel', 'ESC', 'PRESS')
kmi = km.keymap_items.new('screen.animation_play', 'MEDIA_PLAY', 'PRESS')
kmi = km.keymap_items.new('screen.animation_cancel', 'MEDIA_STOP', 'PRESS')

# Map Animation Channels
km = kc.keymaps.new('Animation Channels', space_type='EMPTY', region_type='WINDOW', modal=False)

kmi = km.keymap_items.new('anim.channels_click', 'LEFTMOUSE', 'PRESS')
kmi = km.keymap_items.new('anim.channels_click', 'LEFTMOUSE', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'extend', True)
kmi = km.keymap_items.new('anim.channels_click', 'LEFTMOUSE', 'PRESS', shift=True, ctrl=True)
kmi_props_setattr(kmi.properties, 'children_only', True)
kmi = km.keymap_items.new('anim.channels_rename', 'LEFTMOUSE', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('anim.channels_rename', 'LEFTMOUSE', 'DOUBLE_CLICK')
kmi = km.keymap_items.new('anim.channel_select_keys', 'LEFTMOUSE', 'DOUBLE_CLICK')
kmi = km.keymap_items.new('anim.channel_select_keys', 'LEFTMOUSE', 'DOUBLE_CLICK', shift=True)
kmi_props_setattr(kmi.properties, 'extend', True)
kmi = km.keymap_items.new('anim.channels_find', 'F', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('anim.channels_select_all_toggle', 'A', 'PRESS')
kmi = km.keymap_items.new('anim.channels_select_all_toggle', 'I', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'invert', True)
kmi = km.keymap_items.new('anim.channels_select_border', 'B', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'extend', True)
kmi = km.keymap_items.new('anim.channels_select_border', 'EVT_TWEAK_L', 'ANY')
kmi = km.keymap_items.new('anim.channels_delete', 'X', 'PRESS')
kmi = km.keymap_items.new('anim.channels_delete', 'DEL', 'PRESS')
kmi = km.keymap_items.new('anim.channels_setting_toggle', 'W', 'PRESS', shift=True)
kmi = km.keymap_items.new('anim.channels_setting_enable', 'W', 'PRESS', shift=True, ctrl=True)
kmi = km.keymap_items.new('anim.channels_setting_disable', 'W', 'PRESS', alt=True)
kmi = km.keymap_items.new('anim.channels_editable_toggle', 'TAB', 'PRESS')
kmi = km.keymap_items.new('anim.channels_expand', 'NUMPAD_PLUS', 'PRESS')
kmi = km.keymap_items.new('anim.channels_collapse', 'NUMPAD_MINUS', 'PRESS')
kmi = km.keymap_items.new('anim.channels_expand', 'NUMPAD_PLUS', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'all', False)
kmi = km.keymap_items.new('anim.channels_collapse', 'NUMPAD_MINUS', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'all', False)
kmi = km.keymap_items.new('anim.channels_move', 'PAGE_UP', 'PRESS')
kmi_props_setattr(kmi.properties, 'direction', 'UP')
kmi = km.keymap_items.new('anim.channels_move', 'PAGE_DOWN', 'PRESS')
kmi_props_setattr(kmi.properties, 'direction', 'DOWN')
kmi = km.keymap_items.new('anim.channels_move', 'PAGE_UP', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'direction', 'TOP')
kmi = km.keymap_items.new('anim.channels_move', 'PAGE_DOWN', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'direction', 'BOTTOM')
kmi = km.keymap_items.new('anim.channels_group', 'G', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('anim.channels_ungroup', 'G', 'PRESS', alt=True)

# Map Graph Editor
km = kc.keymaps.new('Graph Editor', space_type='GRAPH_EDITOR', region_type='WINDOW', modal=False)

kmi = km.keymap_items.new('wm.context_toggle', 'H', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'data_path', 'space_data.show_handles')
kmi = km.keymap_items.new('graph.cursor_set', 'ACTIONMOUSE', 'PRESS')
kmi = km.keymap_items.new('graph.clickselect', 'SELECTMOUSE', 'PRESS')
kmi_props_setattr(kmi.properties, 'extend', False)
kmi_props_setattr(kmi.properties, 'column', False)
kmi_props_setattr(kmi.properties, 'curves', False)
kmi = km.keymap_items.new('graph.clickselect', 'SELECTMOUSE', 'PRESS', alt=True)
kmi_props_setattr(kmi.properties, 'extend', False)
kmi_props_setattr(kmi.properties, 'column', True)
kmi_props_setattr(kmi.properties, 'curves', False)
kmi = km.keymap_items.new('graph.clickselect', 'SELECTMOUSE', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'extend', True)
kmi_props_setattr(kmi.properties, 'column', False)
kmi_props_setattr(kmi.properties, 'curves', False)
kmi = km.keymap_items.new('graph.clickselect', 'SELECTMOUSE', 'PRESS', shift=True, alt=True)
kmi_props_setattr(kmi.properties, 'extend', True)
kmi_props_setattr(kmi.properties, 'column', True)
kmi_props_setattr(kmi.properties, 'curves', False)
kmi = km.keymap_items.new('graph.clickselect', 'SELECTMOUSE', 'PRESS', ctrl=True, alt=True)
kmi_props_setattr(kmi.properties, 'extend', False)
kmi_props_setattr(kmi.properties, 'column', False)
kmi_props_setattr(kmi.properties, 'curves', True)
kmi = km.keymap_items.new('graph.clickselect', 'SELECTMOUSE', 'PRESS', shift=True, ctrl=True, alt=True)
kmi_props_setattr(kmi.properties, 'extend', True)
kmi_props_setattr(kmi.properties, 'column', False)
kmi_props_setattr(kmi.properties, 'curves', True)
kmi = km.keymap_items.new('graph.select_leftright', 'SELECTMOUSE', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'mode', 'CHECK')
kmi_props_setattr(kmi.properties, 'extend', False)
kmi = km.keymap_items.new('graph.select_leftright', 'SELECTMOUSE', 'PRESS', shift=True, ctrl=True)
kmi_props_setattr(kmi.properties, 'mode', 'CHECK')
kmi_props_setattr(kmi.properties, 'extend', True)
kmi = km.keymap_items.new('graph.select_leftright', 'LEFT_BRACKET', 'PRESS')
kmi_props_setattr(kmi.properties, 'mode', 'LEFT')
kmi_props_setattr(kmi.properties, 'extend', False)
kmi = km.keymap_items.new('graph.select_leftright', 'RIGHT_BRACKET', 'PRESS')
kmi_props_setattr(kmi.properties, 'mode', 'RIGHT')
kmi_props_setattr(kmi.properties, 'extend', False)
kmi = km.keymap_items.new('graph.select_all_toggle', 'A', 'PRESS')
kmi_props_setattr(kmi.properties, 'invert', False)
kmi = km.keymap_items.new('graph.select_all_toggle', 'I', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'invert', True)
kmi = km.keymap_items.new('graph.select_border', 'B', 'PRESS')
kmi_props_setattr(kmi.properties, 'extend', False)
kmi_props_setattr(kmi.properties, 'axis_range', False)
kmi_props_setattr(kmi.properties, 'include_handles', False)
kmi = km.keymap_items.new('graph.select_border', 'B', 'PRESS', alt=True)
kmi_props_setattr(kmi.properties, 'extend', False)
kmi_props_setattr(kmi.properties, 'axis_range', True)
kmi_props_setattr(kmi.properties, 'include_handles', False)
kmi = km.keymap_items.new('graph.select_border', 'B', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'axis_range', False)
kmi_props_setattr(kmi.properties, 'include_handles', False)
kmi = km.keymap_items.new('graph.select_border', 'B', 'PRESS', ctrl=True, alt=True)
kmi_props_setattr(kmi.properties, 'axis_range', True)
kmi_props_setattr(kmi.properties, 'include_handles', True)
kmi = km.keymap_items.new('graph.select_lasso', 'EVT_TWEAK_A', 'ANY', ctrl=True)
kmi_props_setattr(kmi.properties, 'deselect', False)
kmi = km.keymap_items.new('graph.select_lasso', 'EVT_TWEAK_A', 'ANY', shift=True, ctrl=True)
kmi_props_setattr(kmi.properties, 'deselect', True)
kmi = km.keymap_items.new('graph.select_circle', 'C', 'PRESS')
kmi = km.keymap_items.new('graph.select_column', 'K', 'PRESS')
kmi_props_setattr(kmi.properties, 'mode', 'KEYS')
kmi = km.keymap_items.new('graph.select_column', 'K', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'mode', 'CFRA')
kmi = km.keymap_items.new('graph.select_column', 'K', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'mode', 'MARKERS_COLUMN')
kmi = km.keymap_items.new('graph.select_column', 'K', 'PRESS', alt=True)
kmi_props_setattr(kmi.properties, 'mode', 'MARKERS_BETWEEN')
kmi = km.keymap_items.new('graph.select_more', 'NUMPAD_PLUS', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('graph.select_less', 'NUMPAD_MINUS', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('graph.select_linked', 'L', 'PRESS')
kmi = km.keymap_items.new('graph.frame_jump', 'G', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('graph.snap', 'S', 'PRESS', shift=True)
kmi = km.keymap_items.new('graph.mirror', 'M', 'PRESS', shift=True)
kmi = km.keymap_items.new('graph.handle_type', 'V', 'PRESS')
kmi = km.keymap_items.new('graph.interpolation_type', 'T', 'PRESS')
kmi = km.keymap_items.new('graph.easing_type', 'E', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('graph.smooth', 'O', 'PRESS', alt=True)
kmi = km.keymap_items.new('graph.sample', 'O', 'PRESS', shift=True)
kmi = km.keymap_items.new('graph.bake', 'C', 'PRESS', alt=True)
kmi = km.keymap_items.new('wm.call_menu', 'X', 'PRESS')
kmi_props_setattr(kmi.properties, 'name', 'GRAPH_MT_delete')
kmi = km.keymap_items.new('wm.call_menu', 'DEL', 'PRESS')
kmi_props_setattr(kmi.properties, 'name', 'GRAPH_MT_delete')
kmi = km.keymap_items.new('graph.duplicate_move', 'D', 'PRESS', shift=True)
kmi = km.keymap_items.new('graph.keyframe_insert', 'I', 'PRESS')
kmi = km.keymap_items.new('graph.click_insert', 'ACTIONMOUSE', 'CLICK', ctrl=True)
kmi_props_setattr(kmi.properties, 'extend', False)
kmi = km.keymap_items.new('graph.click_insert', 'ACTIONMOUSE', 'CLICK', shift=True, ctrl=True)
kmi_props_setattr(kmi.properties, 'extend', True)
kmi = km.keymap_items.new('graph.copy', 'C', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('graph.paste', 'V', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('graph.paste', 'V', 'PRESS', shift=True, ctrl=True)
kmi_props_setattr(kmi.properties, 'flipped', True)
kmi = km.keymap_items.new('graph.previewrange_set', 'P', 'PRESS', ctrl=True, alt=True)
kmi = km.keymap_items.new('graph.view_all', 'HOME', 'PRESS')
kmi = km.keymap_items.new('graph.view_all', 'NDOF_BUTTON_FIT', 'PRESS')
kmi = km.keymap_items.new('graph.view_selected', 'NUMPAD_PERIOD', 'PRESS')
kmi = km.keymap_items.new('graph.view_frame', 'NUMPAD_0', 'PRESS')
kmi = km.keymap_items.new('graph.fmodifier_add', 'M', 'PRESS', shift=True, ctrl=True)
kmi_props_setattr(kmi.properties, 'only_active', False)
kmi = km.keymap_items.new('anim.channels_editable_toggle', 'TAB', 'PRESS')
kmi = km.keymap_items.new('transform.translate', 'G', 'PRESS')
kmi = km.keymap_items.new('transform.translate', 'EVT_TWEAK_S', 'ANY')
kmi = km.keymap_items.new('transform.transform', 'E', 'PRESS')
kmi_props_setattr(kmi.properties, 'mode', 'TIME_EXTEND')
kmi = km.keymap_items.new('transform.rotate', 'R', 'PRESS')
kmi = km.keymap_items.new('transform.resize', 'S', 'PRESS')
kmi = km.keymap_items.new('wm.context_toggle', 'O', 'PRESS')
kmi_props_setattr(kmi.properties, 'data_path', 'tool_settings.use_proportional_fcurve')
kmi = km.keymap_items.new('wm.context_set_enum', 'COMMA', 'PRESS')
kmi_props_setattr(kmi.properties, 'data_path', 'space_data.pivot_point')
kmi_props_setattr(kmi.properties, 'value', 'BOUNDING_BOX_CENTER')
kmi = km.keymap_items.new('wm.context_set_enum', 'PERIOD', 'PRESS')
kmi_props_setattr(kmi.properties, 'data_path', 'space_data.pivot_point')
kmi_props_setattr(kmi.properties, 'value', 'CURSOR')
kmi = km.keymap_items.new('wm.context_set_enum', 'PERIOD', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'data_path', 'space_data.pivot_point')
kmi_props_setattr(kmi.properties, 'value', 'INDIVIDUAL_ORIGINS')
kmi = km.keymap_items.new('marker.add', 'M', 'PRESS')
kmi = km.keymap_items.new('marker.rename', 'M', 'PRESS', ctrl=True)

# Map Window
km = kc.keymaps.new('Window', space_type='EMPTY', region_type='WINDOW', modal=False)

kmi = km.keymap_items.new('wm.call_menu_pie', 'S', 'PRESS', ctrl=True, alt=True)
kmi_props_setattr(kmi.properties, 'name', 'pie.editor')
kmi = km.keymap_items.new('wm.call_menu_pie', 'S', 'PRESS', ctrl=True, alt=True)
kmi_props_setattr(kmi.properties, 'name', 'pie.editor')
kmi = km.keymap_items.new('wm.call_menu_pie', 'S', 'PRESS', ctrl=True, alt=True)
kmi_props_setattr(kmi.properties, 'name', 'pie.editor')
kmi = km.keymap_items.new('wm.call_menu_pie', 'S', 'PRESS', ctrl=True, alt=True)
kmi_props_setattr(kmi.properties, 'name', 'pie.editor')
kmi = km.keymap_items.new('wm.call_menu_pie', 'S', 'PRESS', ctrl=True, alt=True)
kmi_props_setattr(kmi.properties, 'name', 'pie.editor')
kmi = km.keymap_items.new('wm.call_menu_pie', 'S', 'PRESS', ctrl=True, alt=True)
kmi_props_setattr(kmi.properties, 'name', 'pie.editor')
kmi = km.keymap_items.new('wm.call_menu_pie', 'S', 'PRESS', ctrl=True, alt=True)
kmi_props_setattr(kmi.properties, 'name', 'pie.editor')
kmi = km.keymap_items.new('wm.pm_edit', 'ACCENT_GRAVE', 'PRESS', shift=True, ctrl=True)
kmi = km.keymap_items.new('wm.call_menu_pie', 'S', 'PRESS', ctrl=True, alt=True)
kmi_props_setattr(kmi.properties, 'name', 'pie.editor')
kmi = km.keymap_items.new('wm.call_menu_pie', 'S', 'PRESS', ctrl=True, alt=True)
kmi_props_setattr(kmi.properties, 'name', 'pie.editor')
kmi = km.keymap_items.new('wm.window_duplicate', 'W', 'PRESS', ctrl=True, alt=True)
kmi = km.keymap_items.new('wm.read_homefile', 'N', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('wm.save_homefile', 'U', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('wm.call_menu', 'O', 'PRESS', shift=True, ctrl=True)
kmi_props_setattr(kmi.properties, 'name', 'INFO_MT_file_open_recent')
kmi = km.keymap_items.new('wm.open_mainfile', 'O', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('wm.open_mainfile', 'F1', 'PRESS')
kmi = km.keymap_items.new('wm.link', 'O', 'PRESS', ctrl=True, alt=True)
kmi = km.keymap_items.new('wm.append', 'F1', 'PRESS', shift=True)
kmi = km.keymap_items.new('power_sequencer.save_direct', 'S', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('wm.save_mainfile', 'W', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('wm.save_as_mainfile', 'S', 'PRESS', shift=True, ctrl=True)
kmi = km.keymap_items.new('wm.save_as_mainfile', 'F2', 'PRESS')
kmi = km.keymap_items.new('wm.save_as_mainfile', 'S', 'PRESS', ctrl=True, alt=True)
kmi_props_setattr(kmi.properties, 'copy', True)
kmi = km.keymap_items.new('wm.window_fullscreen_toggle', 'F11', 'PRESS', alt=True)
kmi = km.keymap_items.new('wm.quit_blender', 'Q', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('wm.doc_view_manual_ui_context', 'F1', 'PRESS', alt=True)
kmi = km.keymap_items.new('wm.redraw_timer', 'T', 'PRESS', ctrl=True, alt=True)
kmi = km.keymap_items.new('wm.debug_menu', 'D', 'PRESS', ctrl=True, alt=True)
kmi = km.keymap_items.new('wm.search_menu', 'SPACE', 'PRESS')
kmi = km.keymap_items.new('wm.call_menu', 'NDOF_BUTTON_MENU', 'PRESS')
kmi_props_setattr(kmi.properties, 'name', 'USERPREF_MT_ndof_settings')
kmi = km.keymap_items.new('wm.context_set_enum', 'F2', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'data_path', 'area.type')
kmi_props_setattr(kmi.properties, 'value', 'LOGIC_EDITOR')
kmi = km.keymap_items.new('wm.context_set_enum', 'F3', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'data_path', 'area.type')
kmi_props_setattr(kmi.properties, 'value', 'NODE_EDITOR')
kmi = km.keymap_items.new('wm.context_set_enum', 'F4', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'data_path', 'area.type')
kmi_props_setattr(kmi.properties, 'value', 'CONSOLE')
kmi = km.keymap_items.new('wm.context_set_enum', 'F5', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'data_path', 'area.type')
kmi_props_setattr(kmi.properties, 'value', 'VIEW_3D')
kmi = km.keymap_items.new('wm.context_set_enum', 'F6', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'data_path', 'area.type')
kmi_props_setattr(kmi.properties, 'value', 'GRAPH_EDITOR')
kmi = km.keymap_items.new('wm.context_set_enum', 'F7', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'data_path', 'area.type')
kmi_props_setattr(kmi.properties, 'value', 'PROPERTIES')
kmi = km.keymap_items.new('wm.context_set_enum', 'F8', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'data_path', 'area.type')
kmi_props_setattr(kmi.properties, 'value', 'SEQUENCE_EDITOR')
kmi = km.keymap_items.new('wm.context_set_enum', 'F9', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'data_path', 'area.type')
kmi_props_setattr(kmi.properties, 'value', 'OUTLINER')
kmi = km.keymap_items.new('wm.context_set_enum', 'F10', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'data_path', 'area.type')
kmi_props_setattr(kmi.properties, 'value', 'IMAGE_EDITOR')
kmi = km.keymap_items.new('wm.context_set_enum', 'F11', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'data_path', 'area.type')
kmi_props_setattr(kmi.properties, 'value', 'TEXT_EDITOR')
kmi = km.keymap_items.new('wm.context_set_enum', 'F12', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'data_path', 'area.type')
kmi_props_setattr(kmi.properties, 'value', 'DOPESHEET_EDITOR')
kmi = km.keymap_items.new('wm.context_scale_float', 'NDOF_BUTTON_PLUS', 'PRESS')
kmi_props_setattr(kmi.properties, 'data_path', 'user_preferences.inputs.ndof_sensitivity')
kmi_props_setattr(kmi.properties, 'value', 1.100000023841858)
kmi = km.keymap_items.new('wm.context_scale_float', 'NDOF_BUTTON_MINUS', 'PRESS')
kmi_props_setattr(kmi.properties, 'data_path', 'user_preferences.inputs.ndof_sensitivity')
kmi_props_setattr(kmi.properties, 'value', 0.9090908765792847)
kmi = km.keymap_items.new('wm.context_scale_float', 'NDOF_BUTTON_PLUS', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'data_path', 'user_preferences.inputs.ndof_sensitivity')
kmi_props_setattr(kmi.properties, 'value', 1.5)
kmi = km.keymap_items.new('wm.context_scale_float', 'NDOF_BUTTON_MINUS', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'data_path', 'user_preferences.inputs.ndof_sensitivity')
kmi_props_setattr(kmi.properties, 'value', 0.6666666865348816)
kmi = km.keymap_items.new('info.reports_display_update', 'TIMER_REPORT', 'ANY', any=True)
kmi = km.keymap_items.new('wm.console_toggle', 'F2', 'PRESS', ctrl=True)

