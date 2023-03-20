import json
import os
import sys
import random
import time
import traceback
from pydub import AudioSegment
import glob
import shutil
print("==========================================")
print("RetroAchievements Unlock Sound Randomizer")
print("Author: Froopy")
print("Version: 1.0.2")
print("==========================================")
#--
#-- Attempt to load configuration file or make one if one is not present
#--
config = ''
createnew = False
try:
  config = open(os.path.join(os.path.dirname(__file__), "config.cfg"), "r").read()
except:
  createnew = True
try:
  if createnew == True:
    config = {
      "sounds_path" : "",
      "retroarch_path" : "",
      "pcsx2_exe_path" : "",
      "bizhawk_path" : "",
      "ffmpeg_path" : ""
    }
    config = json.dumps(config)
    f = open(os.path.join(os.path.dirname(__file__), "config.cfg"), "x")
    f.write(config)
    f.close()
except:
  print('Startup error: Cannot open configuration file or create a new one (config.cfg).')
  print(traceback.format_exc())
  time.sleep(3)
  sys.exit()
try:
  config = json.loads(config)
  print("Configuration file loaded")
  print(f"Sounds Path: {config['sounds_path']}")
  print(f"RetroArch Path: {config['retroarch_path']}")
  print(f"PCSX2 Executable Path: {config['pcsx2_exe_path']}")
  print(f"bizhawk Path: {config['bizhawk_path']}")
  print(f"ffmpeg Path: {config['ffmpeg_path']}")
  print("==========================================")
except:
  print('Startup error: Configuration file is not valid.  Please delete it and rerun this program again (config.cfg).')
  print(traceback.format_exc())
  time.sleep(3)
  sys.exit()
if config["sounds_path"] == "" or config["retroarch_path"] == "":
  print('Startup error: Configuration file has blank settings.  sounds_path and retroarch_path are required to run (config.cfg).')
  print('NOTE: When typing the path on Windows in your configuration file, use double slashes instead of single')
  print('Example: C:\\Media\\Emulators\\RetroArch')
  time.sleep(3)
  sys.exit()
#--
#-- Print startup screen if necessary
#--
runchoice = "retroarch"
if config["pcsx2_exe_path"] != "" or config["bizhawk_path"] != "":
  print("Unlock Randomizer Launch Options")
  print("------------------------------------------")
  print("[1] - RetroArch")
  if config["pcsx2_exe_path"] != "":
    print("[2] - PCSX2")
  if config["bizhawk_path"] != "":
    print("[3] - bizhawk")
  print("[0] - Exit Launcher")
  print("------------------------------------------")
  userchoice = input("Enter option number: ")
  if userchoice not in ['1', '2', '3', '0']:
    print('Parameter error: Option number must be 0, 1, 2 or 3.')
    time.sleep(3)
    sys.exit()
  if userchoice == "2":
    if config["pcsx2_exe_path"] == "":
      print('Parameter error: PCSX2 executable path is blank')
      time.sleep(3)
      sys.exit()
    runchoice = "pcsx2"
  elif userchoice == "3":
    if config["bizhawk_path"] == "":
      print('Parameter error: bizhawk path is blank')
      time.sleep(3)
      sys.exit()
    runchoice = "bizhawk"
  elif userchoice == "0":
    sys.exit()
#--
#-- Choose unlock sound replace target run choice's unlock sound (convert if necessary) and run target application
#--
print("==========================================")
targetsoundfile = ""
try:
  allsounds = glob.glob(os.path.join(config["sounds_path"], "*.ogg"))
  targetsoundfile = allsounds[random.randint(0, len(allsounds) - 1)]
  if runchoice == "retroarch":
    #-- Copy file over to target
    shutil.move(targetsoundfile, os.path.join(config["retroarch_path"], "assets", "sounds", "unlock.ogg"))
  elif runchoice == "pcsx2":
    if config["ffmpeg_path"] == "":
      print('Sound error: ffmpeg path was not provided in configuration and is required for PCSX2')
      time.sleep(3)
      sys.exit()
    os.remove(os.path.join(os.path.dirname(config["pcsx2_exe_path"]), "resources", "sounds", "achievements", "unlock.wav"))
    AudioSegment.converter = os.path.join(config["ffmpeg_path"], "ffmpeg.exe")
    AudioSegment.probe = os.path.join(config["ffmpeg_path"], "ffprobe.exe")
    x = AudioSegment.from_file(targetsoundfile, format='ogg')
    x.export(os.path.join(os.path.dirname(config["pcsx2_exe_path"]), "resources", "sounds", "achievements", "unlock.wav"), format="wav")
  elif runchoice == "bizhawk":
    if config["ffmpeg_path"] == "":
      print('Sound error: ffmpeg path was not provided in configuration and is required for bizhawk')
      time.sleep(3)
      sys.exit()
    os.remove(os.path.join(config["bizhawk_path"], "overlay", "unlock.wav"))
    AudioSegment.converter = os.path.join(config["ffmpeg_path"], "ffmpeg.exe")
    AudioSegment.probe = os.path.join(config["ffmpeg_path"], "ffprobe.exe")
    x = AudioSegment.from_file(targetsoundfile, format='ogg')
    x.export(os.path.join(config["bizhawk_path"], "overlay", "unlock.wav"), format="wav")
  print(f"Random target chosen: {os.path.basename(targetsoundfile)}")
  print("Transferring random choice to target option application")
except:
  print('Sound error: Unable to transfer random sound to target option application')
  print(traceback.format_exc())
  time.sleep(3)
  sys.exit()
#--
#-- Launch target application
#--
try:
  print("Launching target option application in three seconds")
  time.sleep(3)
  if runchoice == "retroarch":
    os.startfile(os.path.join(config['retroarch_path'], "retroarch.exe"))
  elif runchoice == "pcsx2":
    os.startfile(config['pcsx2_exe_path'])
  elif runchoice == "bizhawk":
    os.startfile(os.path.join(config['bizhawk_path'], "EmuHawk.exe"))
except:
  print('Launch error: Unable to access target option application')
  print(traceback.format_exc())
  time.sleep(3)
  sys.exit()
sys.exit()