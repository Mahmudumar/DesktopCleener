
# Desktop Cleener

## Introduction

Desktop Cleener is a Python application designed to help users keep their desktops clean and organized by automatically sorting and moving files from the desktop into designated folders based on their file types.

## Features

- **Automated File Sorting**: Automatically moves files from the desktop to appropriate libraries according to their extensions.
- **Manual Configuration**: Users manually edit the Python script to define file types and their target library folders using an in-script dictionary.
- **Progress Display**: Includes a real-time progress bar that shows the status of file movements.
- **Logging**: Generates detailed logs of the file sorting process, capturing both successful operations and errors.

## Future Features

- **Dynamic File Type Management**: Users will be able to add new file types and associate them automatically with specified libraries directly from the application's settings panel, enhancing flexibility and adaptability.

## Potential Dangers

- **Misplacement of Files**: Files might be moved to incorrect folders if file extensions are improperly configured or unrecognized.
- **Data Loss**: In cases where files are overwritten or deleted during sorting, there's a risk of losing data.

## Risk Mitigation

To minimize risks associated with Desktop Cleener, consider the following precautions:

- **Backup Files**: Always back up important data before running the sorting script. This way, if files are misplaced or lost, you can restore them from the backup.
- **Review Configuration**: Carefully review and test the file extension and folder mapping in the `database` dictionary to ensure that all configurations are correct before running the script.
- **Version Control**: Use version control systems to track changes made to the configuration and the script itself. This practice helps in rolling back to a previous state if something goes wrong.
- **Incremental Changes**: Start by sorting a small number of files to test the script's effectiveness and safety before using it to organize large amounts of data.
- **Error Handling**: Improve the script by implementing robust error handling that can prevent data loss and provide clear diagnostics about what went wrong.

## Installation

To set up Desktop Cleener on your machine, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/MahmudUmar/desktop-cleener.git
   ```

## Usage

Before running the script, open the `desktop_cleener.py` file and locate the dictionary named `database`. Edit this dictionary to customize the file types and their respective target libraries:

```python
database = {
    'Documents': {'txt', 'pdf', 'docx'},
    'Music': {'mp3', 'wav'},
    'Pictures': {'jpg', 'png'},
    'Videos': {'mp4', 'mov'}
}
```

After configuring the dictionary, run the script from the command line to start organizing your desktop files:

```bash
python desktop_cleener.py
```

## Contributing

Contributions are welcome! Please feel free to fork the repository, make changes, and submit pull requests. You can also open issues for bugs, suggestions, or feature requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

Thanks to all the contributors who have helped shape this project. Your contributions are greatly appreciated!

Including upcoming enhancements in your README not only informs users about what improvements to expect but also demonstrates your commitment to developing and refining your application.
