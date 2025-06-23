"""Auto-create a video from the most viewed post on ppomppu.co.kr.

This script downloads today's most viewed post from ppomppu, converts the
content to speech and creates a simple video clip using moviepy.

External dependencies:
- requests
- beautifulsoup4
- gtts
- moviepy

Example usage:
    python autocreate_video.py

This program requires network access for scraping the website and for
Google Text-to-Speech. Ensure `ffmpeg` is installed for moviepy.
"""

import os
from datetime import datetime
from io import BytesIO
import requests
from bs4 import BeautifulSoup
from gtts import gTTS
from moviepy.editor import ImageClip, AudioFileClip, CompositeVideoClip


BASE_URL = "https://www.ppomppu.co.kr"
HOT_PAGE = f"{BASE_URL}/hot.php"


def fetch_hot_posts():
    """Fetch the list of hot posts and return tuples of (title, url, views)."""
    resp = requests.get(HOT_PAGE)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    posts = []
    for tr in soup.select("table.list_table tr.line" ):
        title_cell = tr.select_one("td:nth-of-type(3) a")
        view_cell = tr.select_one("td:nth-of-type(6)")
        if not title_cell or not view_cell:
            continue
        title = title_cell.get_text(strip=True)
        link = title_cell["href"]
        if not link.startswith("http"):
            link = BASE_URL + link
        try:
            views = int(view_cell.get_text(strip=True).replace(",", ""))
        except ValueError:
            views = 0
        posts.append((title, link, views))
    return posts


def get_top_post():
    posts = fetch_hot_posts()
    if not posts:
        raise RuntimeError("No posts found")
    return max(posts, key=lambda x: x[2])


def fetch_post_content(url):
    resp = requests.get(url)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    content_div = soup.find("td", class_="board-contents")
    if not content_div:
        content_div = soup.find("div", id="bbs_write")
    if not content_div:
        raise RuntimeError("Could not locate post content")
    return content_div.get_text(separator="\n", strip=True)


def text_to_speech(text, out_path):
    tts = gTTS(text=text, lang="ko")
    tts.save(out_path)


def create_video(image_path, audio_path, out_path, duration):
    image_clip = ImageClip(image_path, duration=duration)
    audio_clip = AudioFileClip(audio_path)
    video = image_clip.set_audio(audio_clip)
    video.write_videofile(out_path, codec="libx264", audio_codec="aac")


def main():
    print("Fetching hottest post...")
    title, url, views = get_top_post()
    print(f"Top post: {title} ({views} views)")
    content = fetch_post_content(url)

    print("Generating speech...")
    audio_file = "output.mp3"
    text_to_speech(content, audio_file)
    duration = AudioFileClip(audio_file).duration

    print("Creating video...")
    image_path = "cover.jpg"
    if not os.path.exists(image_path):
        # Create a temporary image if none exists
        from PIL import Image, ImageDraw, ImageFont
        img = Image.new("RGB", (1280, 720), color=(255, 255, 255))
        d = ImageDraw.Draw(img)
        d.text((50, 340), title, fill=(0, 0, 0))
        img.save(image_path)
    video_file = f"ppomppu_{datetime.now().strftime('%Y%m%d')}.mp4"
    create_video(image_path, audio_file, video_file, duration)
    print("Video saved to", video_file)


if __name__ == "__main__":
    main()
