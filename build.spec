# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:\\Users\\Elliot CHEN\\Documents\\GitHub\\WonderhoyPlayer\\main.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\Elliot CHEN\\Documents\\GitHub\\WonderhoyPlayer\\main_win.py', '.'), ('C:\\Users\\Elliot CHEN\\Documents\\GitHub\\WonderhoyPlayer\\resources_rc.py', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='WonderhoyPlayer_Windows_x64.exe',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Users\\Elliot CHEN\\Documents\\GitHub\\WonderhoyPlayer\\wonderhoy.ico'],
)
