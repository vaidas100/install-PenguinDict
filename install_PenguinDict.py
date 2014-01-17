#!/usr/local/bin/python

"""
Instaliuoja PenguinDict
"""

import os
import sys
import stat
import getpass
import shutil

# isvalome ekrana
os.system('clear')

# paprashome ivesti pass
os.system('sudo echo')

# susirandame username
username = getpass.getuser()

# nusistatome kokios dir
home_dir = '/home/%s/' %(username)
desktop_dir = '/home/%s/Desktop/' %(username)
penguindict_dir = '/home/%s/PenguinDict/' %(username)

# triname sena PenguinDict direktorija
if os.path.exists(penguindict_dir):
    # keichiame direktorijos savininka
    os.system('sudo chown -R %s:%s "%s"' %(username,username,penguindict_dir))
    # triname
    for root, dirs, files in os.walk(penguindict_dir, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    shutil.rmtree(penguindict_dir)

# keichiame direktorija i home
os.chdir(home_dir)

# instaliuojame visokius modulius kuriu reikes
os.system('sudo apt-get install build-essential g++ git libqt5webkit5-dev libsqlite3-dev make qt5-default qt5-qmake qtbase5-dev qtdeclarative5-dev qtlocation5-dev qtquick1-5-dev qtsensors5-dev')

# atsisiunchiame PenguinDict
os.system('sudo git clone git://github.com/tuxmark5/PenguinDict.git %s' %(penguindict_dir))

# keichiame direktorijos savininka
os.system('sudo chown -R %s:%s "%s"' %(username,username,penguindict_dir))

# qmake, make
os.chdir(penguindict_dir)
os.system('qmake')
os.system('make')

# sukuriam PenguinDict.sh
bash_filename = penguindict_dir + 'PenguinDict.sh'
bashf = open(bash_filename,'w')
bashf.write('#!/bin/bash\n'
            'cd /home/%s/PenguinDict\n'
            '/home/%s/PenguinDict/PenguinDict'
            %(username,username)
)
bashf.close()
os.system('sudo chown %s:%s "%s"' %(username,username,bash_filename))
os.chmod(bash_filename, 0777)

# sukuriame PenguinDict.desktop failus
desktop_filename1 = penguindict_dir + 'PenguinDict.desktop'
desktop_filename2 = desktop_dir + 'PenguinDict.desktop'
desktop_filename3 = '/usr/share/applications/' + 'PenguinDict.desktop'
desktopf = open(desktop_filename1,'w')
desktopf.write('[Desktop Entry]\n'
               'Name=PenguinDict\n'
               'Version=1.0\n'
               'Comment=EN-LT dictionary\n'
               'Exec=%s\n'
               'Icon=%sicon.png\n'
               'Terminal=false\n'
               'Type=Application\n'
               'Categories=Office;\n'
               %(bash_filename,penguindict_dir)
)
desktopf.close()
os.system('sudo cp %s %s' %(desktop_filename1,desktop_filename2))
os.system('sudo cp %s %s' %(desktop_filename1,desktop_filename3))
os.system('sudo chown %s:%s "%s"' %(username,username,desktop_filename1))
os.system('sudo chown %s:%s "%s"' %(username,username,desktop_filename2))
os.system('sudo chown %s:%s "%s"' %(username,username,desktop_filename3))
os.chmod(desktop_filename1, 0777)
os.chmod(desktop_filename2, 0777)
os.chmod(desktop_filename3, 0777)

# ishvedame praneshima apie trukstama faila Anglonas.dic
last_print_text = [
    '',
    'Don\'t forget to copy file:',
    'Anglonas.dic',
    '-->',
    penguindict_dir,
    '',
]
longest_line_len = 0
for line in last_print_text:
    if len(line) > longest_line_len:
        longest_line_len = len(line)
print '#'*int(int(longest_line_len) + 8)
for line in last_print_text:
    while len(line) < longest_line_len:
        line = line + ' '
    print '#   ' + line + '   #'
print '#'*int(int(longest_line_len) + 8)

