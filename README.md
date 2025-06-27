# YouTube Podcast Downloader

A simple and efficient Python CLI tool to download podcast episodes from YouTube playlists and save them as MP3 audio files with structured metadata.

## Features

- Download full podcast playlists from YouTube as MP3
- Automatically names and organizes episodes by playlist order
- Saves episode metadata to a JSON file
- Easy-to-use CLI interface
- Fast downloads using `yt-dlp` and `ffmpeg`

---

## Installation

### Prerequisites

- Python 3.7 or higher
- `ffmpeg` installed and available in your system PATH
- `pip` (Python package manager)

### Clone and Install (Local Development)

```bash
git clone https://github.com/yourusername/podcast-downloader.git
cd podcast-downloader
pip install -e .
