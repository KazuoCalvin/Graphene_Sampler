# -*- mode: python ; coding: utf-8 -*-
# PyInstaller .spec for Graphene_Sampler
# Entry point: main.py
# Includes 'ui' folder and attempts to include dependencies listed in requirements.txt

import os
from PyInstaller.utils.hooks import collect_submodules, collect_data_files
from PyInstaller.building.build_main import Analysis, PYZ, EXE, COLLECT

project_dir = os.path.dirname(__file__)
entry_script = os.path.join(project_dir, 'main.py')

# Add project dir to search path
pathex = [project_dir]

# Include UI folder (if present)
datas = []
ui_dir = os.path.join(project_dir, 'ui')
if os.path.isdir(ui_dir):
    # Tree-like inclusion: include entire ui directory under 'ui' in the bundle
    from PyInstaller.utils.hooks import collect_data_files as _cdf
    # collect_data_files on a package won't work for plain folders; use simple walk to build datas
    for root, _, files in os.walk(ui_dir):
        for f in files:
            src = os.path.join(root, f)
            # destination path inside bundle: preserve relative path under 'ui'
            dest = os.path.relpath(root, project_dir)
            datas.append((src, dest))

# Try to collect submodules and package data for packages listed in requirements.txt
hiddenimports = []
try:
    req_file = os.path.join(project_dir, 'requirements.txt')
    if os.path.exists(req_file):
        with open(req_file, 'r') as rf:
            for line in rf:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                pkg = line.split('==')[0].split('>=')[0].split('<')[0].strip()
                if not pkg:
                    continue
                try:
                    hiddenimports += collect_submodules(pkg)
                except Exception:
                    # ignore packages that cannot be collected automatically
                    pass
                try:
                    datas += collect_data_files(pkg)
                except Exception:
                    pass
except Exception:
    pass

a = Analysis(
    [entry_script],
    pathex=pathex,
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    noarchive=False
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='Graphene_Sampler',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Graphene_Sampler'
)