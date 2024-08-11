from yt_dlp import YoutubeDL
from pathlib import Path

def download_video(url: str, format: str) -> str:
    output_dir = Path("media")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    ydl_opts = {
        'format': 'bestaudio/best' if format == 'mp3' else 'best',
        'outtmpl': str(output_dir / '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }] if format == 'mp3' else [],
    }
    
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        file_name = ydl.prepare_filename(info_dict)
        if format == 'mp3':
            file_name = file_name.rsplit('.', 1)[0] + '.mp3'
        return str(file_name)