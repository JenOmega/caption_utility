# Caption Utility

## Overview
This code exists as an experiment in using ChatGPT for code generation. The rest of this file, and almost all files, were made by ChatGPT.

The use case is captioning files for Stable Diffusion.  I got frustrated by manually creating .txt files, opening images one at a time and adding the same caption to a batch of them, etc. So I fired up ChatGPT and asked it to help me make a python project that would open my image folder and edit all the captions with a web interface. Et voila, it does. This took about an hour.

It took about an hour to do this whole thing, and I've never written python before. I never heard of flask before I started it.  I do intend to add more features as I use it. 

## Features
- Display images from a selected directory in a gallery view.
- Append custom text to image descriptions with formatting rules.
- Dark mode interface for improved visual comfort.
- Supports basic image operations like zoom and selection within the browser.

## Installation

### Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.8 or higher
- pip and virtualenv (recommended)

### Setup
To install Caption Utility, follow these steps:

Linux and macOS:
```bash
git clone https://github.com/jenomega/caption_utility.git
cd caption_utility
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
