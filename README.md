# RAUnlockRandomizer
Achievement unlock sound randomizer for RetroArch and PCSX2 (OGG Vorbis)

# Prerequisites
* Windows
* A bunch of your favorite achievement unlock sounds as OGG Vorbis (.OGG) files
* [Python](https://python.org/)
* [pydub](https://pypi.org/project/pydub/) (if using PCSX2)
* [ffmpeg](https://ffmpeg.org/) (if using PCSX2)

# Installation
On first launch, this will create a configuration file in the same directory (config.cfg) where you need to populate your path variables:

* sounds_path (Sound File Directory)
* retroarch_path (RetroArch Directory)
* pcsx2_exe_path (PCSX2 Executable Path) (optional)
* ffmpeg_path (ffmpeg Directory) (optional)

If you provide a PCSX2 path, it will show you two options to pick.  If you only provide a RetroArch path, it will simply choose a sound and run RetroArch

For the paths, you need to specify backslashes with two slashes, like: C:\\Emulators\\RetroArch

The PCSX2 option will automatically convert the OGG file to a WAV format file for PCSX2 to use.

# Running

Upon running, you will be asked to choose an option (if PCSX2 used):

* [1] RetroArch
* [2] PCSX2
* [0] Exit Launcher

If PCSX2 is not used, the program will randomly choose an unlock sound and overwrite it in the target application option.
