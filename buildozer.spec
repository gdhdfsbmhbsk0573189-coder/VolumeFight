[app]
title = Volume Fight
package.name = volumefight
package.domain = org.taha
version = 1.0
source.dir = .
source.include_exts = py
requirements = python3,kivy==2.3.0,pyjnius==1.6.1,cython==0.29.33
android.permissions = VIBRATE, MODIFY_AUDIO_SETTINGS
android.api = 33
android.minapi = 24
android.ndk = 25b
# این خط به گیت‌هاب می‌گه خودکار قوانین گوگل رو قبول کنه
android.accept_sdk_license = True
# این خط هم یه نسخه پایدار از build-tools رو تعیین می‌کنه
android.build_tools = 33.0.2
