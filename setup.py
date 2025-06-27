from setuptools import setup, find_packages

setup(
    name='podcast-downloader',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'yt-dlp',
    ],
    entry_points={
        'console_scripts': [
            'podcast-downloader=podcast_downloader.main:main',
        ],
    },
    author='Gauransh',
    description='A CLI tool to download YouTube podcast playlists as MP3s',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
