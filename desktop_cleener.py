
"""
Desktop Cleener is a Python script designed to organize and clean up your desktop by moving files into predefined libraries based on their file types.

Features:
- Automatically sorts files from the desktop into corresponding folders like Documents, Music, Pictures, and Videos.
- Allows user-defined file type associations via an in-script dictionary.
- Provides a real-time progress bar and detailed logs of the file sorting process.

Usage:
1. Modify the 'database' dictionary in the script to customize file types and target directories.
2. Run the script to sort files on the desktop according to the defined settings.

Example dictionary configuration:
database = {
    'Documents': {'txt', 'pdf', 'docx'},
    'Music': {'mp3', 'wav'},
    'Pictures': {'jpg', 'png'},
    'Videos': {'mp4', 'mov'}
}

Dependencies: None beyond standard Python libraries.
"""

import pathlib
import os
import time
import tkinter as tk
import tkinter.ttk as ttk



class App:
    database = {
        'Documents': {'rtf', 'txt', 'pdf', 'xlsx',
                      'xls', 'zip', 'doc', 'docx',
                      'pptx', 'ppt', 'py', 'svg',
                      'html', 'htm', 'css', 'jar', 'java'},
        'Music': {'mp3', 'm4a', 'wav'},
        'Pictures': {'png', 'jpg', 'jpeg'},
        'Videos': {'mp4', 'mov', 'avi'},
        'Downloads': {'exe', 'msi'}

    }

    def __init__(self) -> None:
        self.app = tk.Tk()

        self.main_frame = tk.Frame(self.app)
        self.main_frame.pack()

        self.prog_bar = ttk.Progressbar(self.main_frame, length=500)
        self.prog_bar.pack(side='top')

        self.logs_msg = tk.Label(self.main_frame, text='')
        self.logs_msg.pack(side='top')

        self.done_bt = tk.Button(self.main_frame, text='Okay',command=self.okay,state='disabled')
        self.done_bt.pack(side='top')

        self.desktop_lib = pathlib.Path(r'C:\Users\USER\Desktop')
        self.counter = 0

        self.files_in_desktop = list(self.desktop_lib.iterdir())
        self.arr()
        self.app.mainloop()

    def log(self, msg):
        self.logs_msg['text'] = msg

    def update(self):
        """update the progress bar"""
        self.percent = round((self.counter/self.total)*100)
        if self.counter <= self.total:
            self.prog_bar['value'] = self.percent
        print(self.percent, '%')

    def count_files(self):
        """Count the number of files in the source folder to operate on.
          This is intended to calculate the progress
        """
        self.amount = 0
        self.acceptables = set()

        for sett in self.database.values():
            for acceptable in sett:
                self.acceptables.add(acceptable)

        for file in self.files_in_desktop:
            if file.suffix.lower().strip('.') in self.acceptables:
                self.amount += 1

        return self.amount

    def arr(self):
        from threading import Thread
        self.thread = Thread(target=self._arr)
        self.thread.daemon = True
        self.thread.start()

    def _arr(self):
        """Take the files found in the desktop folder
            to the desired location. The destination folders are in the 
            database above which is universal."""
        self.total = self.count_files()
        if self.total < 1:
                # TODO get into folders and move them
                self.log(f'No valid files in "{self.desktop_lib}" to move')
                self.done_bt['state']='active'
        else:
            for lib, file_types in zip(self.database.keys(),
                                    self.database.values()):

                lib_to_drop = pathlib.Path(fr'C:\Users\USER\{lib}')
                lib_to_drop_supported_files = file_types
            
                for file in self.files_in_desktop:
                    if (file.is_file()) and (file.suffix.lower().strip('.') in lib_to_drop_supported_files):
                        path = f'{lib_to_drop}\\{file.name}'
                        try:

                            new_path = file.rename(path)
                            print(f'successful {new_path}')
                            self.log(f'successful {new_path}')
                            self.counter += 1
                            self.update()

                        except FileExistsError:
                            print('already exists, replacing...')
                            self.log('already exists, replacing...')
                            os.remove(file)
                            print(f'Replaced {path}')
                            self.log(f'Replaced {path}')
                            self.counter += 1
                            self.update()

                        time.sleep(0.1)
                self.log(
                    'Done arranging files in their respective libraries')
            self.done_bt['state']='active'
    def okay(self):
        self.app.quit()


a = App()
