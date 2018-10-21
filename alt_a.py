if 'gnome-terminal-server.Gnome-terminal' in window.get_active_class():
  keyboard.send_keys('<ctrl>+<shift>+a')
else:
  keyboard.send_keys('<ctrl>+a')