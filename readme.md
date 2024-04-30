# Desktop Cleener

## Introduction

Desktop Cleener is a Python application designed to help users keep their desktops clean and organized by automatically sorting and moving files from the desktop into designated folders based on their file types.

## Features

- Automated File Sorting: Automatically moves files from the desktop to appropriate libraries according to their extensions.
- Manual Configuration: Users manually edit the Python script to define file types and their target library folders using an in-script dictionary.
- Progress Display: Includes a real-time progress bar that shows the status of file movements.
- Logging: Generates detailed logs of the file sorting process, capturing both successful operations and errors.

## Installation

To set up Desktop Cleener on your machine, follow these steps:

1. Clone the repository:

   ```bash
   git clone <https://github.com/yourusername/desktop-cleener.git>

## Usage

Before running the script, open the desktop_cleener.py file and locate the dictionary named database. Edit this dictionary to customize the file types and their respective target libraries:

Example configuration dictionary:

```python
database = {
    'Documents': {'txt', 'pdf', 'docx'},
    'Music': {'mp3', 'wav'},
    'Pictures': {'jpg', 'png'},
    'Videos': {'mp4', 'mov'}
}
