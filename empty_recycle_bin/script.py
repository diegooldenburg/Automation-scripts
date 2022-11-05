import os

os = str(input('What OS are you using? (Windows/Unix): '))
if os == 'Windows':
    import winshell
    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
if os == 'Unix':
    os.system('sudo rm -rf ~/.Trash/*')