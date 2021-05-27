# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['C:/Users/guilh/Documents/Dev/Python/Projetos/ZoomHackV3.0/main.py'],
             pathex=['C:\\Users\\guilh\\Documents\\Dev\\Python\\Projetos\\ZoomHackV3.0'],
             binaries=[('C:/Users/guilh/Documents/Dev/Python/Projetos/ZoomHackV3.0/utils/geckodriver32.exe', './utils'), ('C:/Users/guilh/Documents/Dev/Python/Projetos/ZoomHackV3.0/utils/geckodriver64.exe', './utils')],
             datas=[('C:/Users/guilh/Documents/Dev/Python/Projetos/ZoomHackV3.0/utils/geckodriver32.exe', './utils'), ('C:/Users/guilh/Documents/Dev/Python/Projetos/ZoomHackV3.0/utils/geckodriver64.exe', './utils')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Prezomba 3.0',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True , icon='C:\\Users\\guilh\\Documents\\Dev\\Python\\Projetos\\ZoomHackV3.0\\zoomhack.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Prezomba 3.0')
