# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_data_files, collect_submodules

a = Analysis(
    ['admission.py'],
    pathex=[],
    binaries=[],
    datas=[
        *collect_data_files('customtkinter'),
        *collect_data_files('tkcalendar'),
        *collect_data_files('webdriver_manager'),
        ('timetable_data.json', '.'),
        ('favicon.ico', '.'),
    ],
    hiddenimports=[
        *collect_submodules('keyring'),
        *collect_submodules('oauth2client'),
        *collect_submodules('google'),
        *collect_submodules('gspread'),
        *collect_submodules('selenium'),
        *collect_submodules('webdriver_manager'),
        *collect_submodules('tkcalendar'),
        *collect_submodules('customtkinter'),
        'tkinter',
        'tkinter.ttk',
        'tkinter.messagebox',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='admission',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    runtime_tmpdir=None,
    console=False,
    icon='favicon.ico',
)
