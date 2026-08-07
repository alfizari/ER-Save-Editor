# -*- mode: python ; coding: utf-8 -*-
# Build for Apple Silicon (arm64) macOS as a proper .app bundle (onedir).
# Run from repo root:
#   source .venv/bin/activate
#   pyinstaller src/build_mac.spec
from pathlib import Path

# Resolve project paths relative to this spec file (src/) and the repo root.
SPEC_DIR = Path(SPECPATH).resolve()
SRC_DIR = SPEC_DIR
ROOT_DIR = SPEC_DIR.parent
ENTRY = str(SRC_DIR / "Final.py")
RESOURCES = str(SRC_DIR / "Resources")

a = Analysis(
    [ENTRY],
    pathex=[str(SRC_DIR), str(ROOT_DIR)],
    binaries=[],
    datas=[
        (RESOURCES, "Resources"),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

# Onedir EXE (required for a proper macOS .app; onefile+BUNDLE is deprecated).
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="Elden_Ring_Save_Editor",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
    windowed=True,
    target_arch="arm64",
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name="Elden_Ring_Save_Editor",
)

app = BUNDLE(
    coll,
    name="Elden_Ring_Save_Editor_App.app",
    icon=None,
    bundle_identifier="com.eldenring.saveeditor",
    info_plist={
        "NSHighResolutionCapable": True,
        "LSMinimumSystemVersion": "11.0",
        "CFBundleDisplayName": "Elden Ring Save Editor",
        "CFBundleName": "Elden Ring Save Editor",
        "CFBundleShortVersionString": "2.1",
        "CFBundleVersion": "2.1",
    },
)
