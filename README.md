# AutoCreate

This repository contains a script to automatically download the most viewed post from ppomppu.co.kr and create a narrated video from it.

## 윈도우에서 파이썬 설치하기
1. [공식 파이썬 홈페이지](https://www.python.org/downloads/windows/)에서 최신 버전을 다운로드합니다.
2. 설치 프로그램 실행 시 **Add Python to PATH** 옵션을 선택한 뒤 설치합니다.
3. 설치가 끝나면 명령 프롬프트에서 `python --version`을 입력해 정상 설치 여부를 확인합니다.

이후 아래 사용법을 따라 가상환경을 만들어 주세요.

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
