# AutoCreate

This repository contains a script to automatically download the most viewed post from ppomppu.co.kr and create a narrated video from it.

## Usage
1. Install dependencies:
   ```bash
   pip install requests beautifulsoup4 gtts moviepy pillow
   ```
   Ensure `ffmpeg` is installed.

2. Place an image named `cover.jpg` in the repository root. This will be used as the video background.

3. Run the script:
   ```bash
   python autocreate_video.py
   ```

The script will save a video file named `ppomppu_YYYYMMDD.mp4`.
