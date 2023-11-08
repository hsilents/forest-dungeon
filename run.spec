# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

added_files = [ #FILES/FOLDERS TO INCLUDE IN COMPILED VERSION
    ('DungeonGame','DungeonGame'),
    ('assets','assets')
]

a = Analysis(
    ['run.py'],
    pathex=[],
    binaries=[],
    datas=added_files,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)


