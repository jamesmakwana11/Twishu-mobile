[app]

# App ka naam
title = Twishu

# Package name (unique hona chahiye)
package.name = twishu
package.domain = org.twishu

# Source directory
source.dir = .

# Files include karne ke liye
source.include_exts = py,png,jpg,kv,atlas

# Version
version = 1.0

# Requirements
requirements = python3,kivy,kivymd,plyer,speechrecognition,groq,requests

# Permissions
android.permissions = INTERNET,RECORD_AUDIO,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# Orientation
orientation = portrait

# Android Build Settings (Important Fix)
android.api = 33
android.minapi = 21
android.build_tools = 34.0.0        # ← Yeh line add ki hai (license error fix)

# Architectures
android.archs = arm64-v8a, armeabi-v7a

# Other settings
fullscreen = 0
android.allow_backup = True

# Log level
[buildozer]
log_level = 2
warn_on_root = 1
