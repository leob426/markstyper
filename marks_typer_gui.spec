# -*- mode: python ; coding: utf-8 -*-
import requests.certs

a = Analysis(
    ['marks_typer_gui.py'],
    pathex=[],
    binaries=[],
    # Explicitly add certifi and chardet packages as data
    datas=[(requests.certs.where(), "certifi")],
    hiddenimports=['chardet', 'certifi'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='marks_typer_gui',
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
)
