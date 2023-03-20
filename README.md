# RAUnlockRandomizer
Achievement unlock sound randomizer for RetroArch and PCSX2 (OGG Vorbis)

# Prerequisites
* Windows
* A bunch of your favorite achievement unlock sounds as OGG Vorbis (.OGG) files
* [Python](https://python.org/)
* [pydub](https://pypi.org/project/pydub/)
* [ffmpeg](https://ffmpeg.org/) (if using PCSX2)

# Installation
On first launch, this will create a configuration file in the same directory (config.cfg) where you need to populate your path variables:

* sounds_path (Sound File Directory)
* retroarch_path (RetroArch Directory) (optional)
* pcsx2_exe_path (PCSX2 Executable Path) (optional)
* bizhawk_path (bizhawk Directory) (optional)
* ffmpeg_path (ffmpeg Directory) (optional)

At least one of retroarch_path, pcsx2_exe_path or bizhawk_path must be populated along with sounds_path.  If pcsx2_exe_path or bizhawk_path are used, ffmpeg_path must be populated.

For the paths, you need to specify backslashes with two slashes, like: C:\\\\Emulators\\\\RetroArch

The PCSX2 and bizhawk option will automatically convert the OGG file to a WAV format file for it to use.

# Running

Upon running, you will be asked to choose an option (if multiple option paths were given in configuration):

* [1] RetroArch
* [2] PCSX2
* [3] bizhawk
* [0] Exit Launcher

If only one option was given in configuration, this menu will be skipped and the program will randomly choose an unlock sound and overwrite it in the target application option then launch it for you.
