#!/usr/bin/python

import os
import getpass


def main():

    # clear screen
    os.system("clear")

    # ask for password
    os.system("sudo echo")

    # get username
    username = getpass.getuser()

    # install dependencies
    os.system(
        "yes | LC_ALL=en_US.UTF-8 "
        "sudo pacman -S "
        "git "
        "make "
        "gcc "
        "qt5-declarative "
        "qt5-webkit "
    )

    # make PenguinDict dir
    penguindict_dir = f"/home/{username}/PenguinDict/"
    if os.path.exists(penguindict_dir):
        os.system(f'sudo rm -r "{penguindict_dir}"')
    os.makedirs(penguindict_dir)

    # get PenguinDict source
    os.system(
        f'sudo git clone git://github.com/tuxmark5/PenguinDict.git "{penguindict_dir}"'
    )

    # install PenguinDict
    os.system(f'sudo chown -R {username}:{username} "{penguindict_dir}"')
    os.chdir(penguindict_dir)
    os.system("qmake")
    os.system("make")

    # make PenguinDict.sh file
    bash_file = os.path.join(penguindict_dir, "PenguinDict.sh")
    with open(bash_file, "w") as bash_fh:
        bash_fh.write(
            f"#!/bin/bash\n"
            f"cd /home/{username}/PenguinDict\n"
            f"/home/{username}/PenguinDict/PenguinDict"
        )
    os.system(f'sudo chown {username}:{username} "{bash_file}"')
    os.chmod(bash_file, 0o777)

    # make PenguinDict.desktop files
    desktop_file1 = os.path.join(penguindict_dir, "PenguinDict.desktop")
    desktop_file2 = "/usr/share/applications/PenguinDict.desktop"
    with open(desktop_file1, "w") as desktop_fh:
        desktop_fh.write(
            f"[Desktop Entry]\n"
            f"Name=PenguinDict\n"
            f"Version=1.0\n"
            f"Comment=EN-LT dictionary\n"
            f"Exec={bash_file}\n"
            f"Icon={penguindict_dir}icon.png\n"
            f"Terminal=false\n"
            f"Type=Application\n"
            f"Categories=Office;\n"
        )
    os.system(f"sudo cp {desktop_file1} {desktop_file2}")
    os.system(f'sudo chown {username}:{username} "{desktop_file1}"')
    os.system(f'sudo chown {username}:{username} "{desktop_file2}"')
    os.chmod(desktop_file1, 0o777)
    os.chmod(desktop_file2, 0o777)

    # print information about missing Anglonas.dic file
    lines = [
        "",
        "Don't forget to copy file:",
        "Anglonas.dic",
        "-->",
        penguindict_dir,
        "",
    ]
    max_line_len = len(max(lines, key=len))
    lines = [f"{line:{max_line_len}s}" for line in lines]
    print("#" * int(max_line_len + 8))
    for line in lines:
        print(f"#   {line}   #")
    print("#" * int(max_line_len + 8))


if __name__ == "__main__":
    main()
