# AutoCreate

This repository contains a script to automatically download the most viewed post from ppomppu.co.kr and create a narrated video from it.

## Usage
1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # on Windows use "venv\\Scripts\\activate"
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   Ensure `ffmpeg` is installed.

3. Place an image named `cover.jpg` in the repository root. This will be used as the video background.

4. Run the script:
   ```bash
   python autocreate_video.py
   ```

The script will save a video file named `ppomppu_YYYYMMDD.mp4`.
