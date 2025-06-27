import os
import json
import yt_dlp

def download_podcast(playlist_url, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    metadata_list = []

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_dir, '%(playlist_index)s - %(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': False,
        'noplaylist': False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(playlist_url, download=True)
        entries = info_dict.get('entries', [])

        for entry in entries:
            if entry:
                metadata = {
                    'title': entry.get('title'),
                    'url': entry.get('webpage_url'),
                    'duration': entry.get('duration'),
                    'upload_date': entry.get('upload_date'),
                    'id': entry.get('id'),
                    'index': entry.get('playlist_index')
                }
                metadata_list.append(metadata)

    # Save metadata
    with open(os.path.join(output_dir, 'metadata.json'), 'w') as f:
        json.dump(metadata_list, f, indent=2)

    print(f"\nDownloaded {len(metadata_list)} podcast episodes to '{output_dir}'.")
