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

# Requirements (important - sab libraries)
requirements = python3,kivy,kivymd,plyer,speechrecognition,groq,requests

# Permissions (Mic + Internet sabse zaroori)
android.permissions = INTERNET,RECORD_AUDIO,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# Orientation
orientation = portrait

# Android API settings (modern phones ke liye best)
android.api = 33
android.minapi = 21

# Architectures (dono common phones support karne ke liye)
android.archs = arm64-v8a, armeabi-v7a

# Fullscreen nahi rakhna (better UX)
fullscreen = 0

# Backup allowed
android.allow_backup = True

# Log level (debug ke liye)
[buildozer]
log_level = 2
warn_on_root = 1