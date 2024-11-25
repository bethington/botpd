import json
import os
import shutil

from config import Config
from mss import mss
from utils.misc import close_down_bnet_launcher, close_down_d2, only_lowercase_letters


def get_pd2_folder() -> str:
    """
    Get D2r folder
    try to find pre-set D2r folder
    :param config: the general config possibly containing 'saved_games_folder'
    :return: the D2r folder full path
    """
    d2_saved_games = Config().general["saved_games_folder"]
    if not d2_saved_games:
        # assign default value for en-us Windows users
        d2_saved_games = f"C:\\Diablo2Project\\ProjectD2"
    if not os.path.exists(d2_saved_games):
        print(f"Your PD2 Saved Games folder could not be found here: {d2_saved_games}, input the correct location:")
        d2_saved_games = input()
    if not os.path.exists(d2_saved_games):
        assert(f"Could not find PD2 Saved Games at {d2_saved_games}")
    return d2_saved_games

def backup_settings():
    d2_saved_games = get_pd2_folder()
    backup_file = f"{d2_saved_games}/d2gl.bak.json"
    current_file = f"{d2_saved_games}/d2gl.json"
    if os.path.exists(backup_file):
        r = input("PD2 settings backup already exists, are you sure you want to overwrite it? [y] to confirm")
        if not r == 'y':
            return
    shutil.copyfile(current_file, backup_file)
    print("PD2 settings backed up successfully.")

    backup_file = f"{d2_saved_games}/launch_options_backup.txt"
    current_file = f"{os.getenv('APPDATA')}/Battle.net/Battle.net.config"
    if os.path.exists(backup_file):
        r = input("PD2 launch options backup already exists, are you sure you want to overwrite it? [y] to confirm")
        if not r == 'y':
            return
    f = open(current_file)
    curr_settings = json.load(f)
    launch_options = curr_settings["Games"]["osi"]["AdditionalLaunchArguments"]
    with open(backup_file, 'w') as f:
        f.write(launch_options)
    print("PD2 launch options backed up successfully.")

def restore_settings_from_backup():
    d2_saved_games = get_pd2_folder()
    backup_file = f"{d2_saved_games}/d2gl.bak.json"
    current_file = f"{d2_saved_games}/d2gl.json"
    if not os.path.exists(backup_file):
        print("No PD2 settings backup file was found, couldn't restore.")
        return
    close_down_d2()
    try:
        shutil.copyfile(backup_file, current_file)
        print("PD2 settings restored successfully.")
    except Exception as e:
        print("PD2 settings restored unsuccessfully.")
        print(f"Error: {e}")

    backup_file = f"{d2_saved_games}/launch_options_backup.txt"
    current_file = f"{os.getenv('APPDATA')}/Battle.net/Battle.net.config"
    if not os.path.exists(backup_file):
        print("No PD2 launch options backup file was found, couldn't restore.")
        return
    with open(backup_file, 'r') as f:
        launch_options = f.read().strip()
    set_launch_settings(launch_options)
    print("PD2 launch options restored successfully.")

def set_launch_settings(launch_options):
    close_down_bnet_launcher()
    # open bnet config setts
    f = open(f"{os.getenv('APPDATA')}/Battle.net/Battle.net.config")
    curr_settings = json.load(f)
    # write launch options to bnet config
    try:
        curr_settings["Games"]["osi"]["AdditionalLaunchArguments"] = launch_options
        with open(f"{os.getenv('APPDATA')}/Battle.net/Battle.net.config", 'w') as outfile:
            json.dump(curr_settings, outfile, indent=4)
    except:
        print("Error: Could not set launch options.")
        print(f"You might need to set the launch options manually. Add launch options to PD2 in BNet launcher: {launch_options}")

def copy_mod_files():
    mod_name = only_lowercase_letters(Config().general["name"].lower())
    if not mod_name:
        mod_name = "botpd"
    old_path = "assets/mods/botpd"
    if not os.path.exists(Config().general["pd2_path"]):
        raise ValueError(f"Could not copy mod files because pd2_path {Config().general['pd2_path']} does not exist, please review your params.ini settings and set to your true PD2 installation directory")

    new_path = os.path.join(Config().general['pd2_path'], f"mods/{mod_name}")
    os.makedirs(new_path, exist_ok=True)
    try:
        # copy mod files to pd2 directory
        shutil.rmtree(new_path)
        shutil.copytree(old_path, new_path)
        os.rename(f"{new_path}/botpd.mpq", f"{new_path}/{mod_name}.mpq")

        # modify modinfo.json to use mod_name
        mod_info_path = f"{new_path}/{mod_name}.mpq/modinfo.json"
        with open(mod_info_path, "rb") as file:
            data=file.read()
            mod_info=json.loads(data)
        mod_info["name"] = mod_name
        with open(mod_info_path, 'w') as outfile:
            json.dump(mod_info, outfile, indent=4)

    except Exception as e:
        print(f"Error copying mod files: {e}")
        print(f"You might need to copy the mod files from {old_path} to {new_path} manually.")

def adjust_settings():
    close_down_d2()
    # find monitor res
    sct = mss()
    monitor_idx = 1
    if len(sct.monitors) == 1:
        print("How do you not have a monitor connected?!")
        os._exit(1)
    d2_saved_games = get_pd2_folder()
    # adjust settings
    if Config().advanced_options["launch_options"]:
        set_launch_settings(Config().advanced_options["launch_options"])
        copy_mod_files()
    f = open(d2_saved_games + "\\d2gl.json")
    curr_settings = json.load(f)
    f = open("assets/botpd_d2gl.json")
    new_settings = json.load(f)
    for key in new_settings:
        curr_settings[key] = new_settings[key]
    # In case monitor res is at 720p, force fullscreen
    if sct.monitors[monitor_idx]['width'] == 1280 and sct.monitors[monitor_idx]['height'] == 720:
        print(f"Detected 720p Monitor res. Forcing fullscreen mode.")
        curr_settings["Window Mode"] = 1
    # write back to d2gl.json
    with open(d2_saved_games + "\\d2gl.json", 'w') as outfile:
        json.dump(curr_settings, outfile)
    print("Adapted settings succesfully. You can now restart PD2.")

def check_settings() -> dict:
    d2_saved_games = get_pd2_folder()
    # adjust settings
    f = open(d2_saved_games + "\\d2gl.json")
    curr_settings = json.load(f)
    f = open("assets/botpd_d2gl.json")
    new_settings = json.load(f)
    diff_settings = {}
    for key in new_settings:
        if key != "Window Mode" and curr_settings[key] != new_settings[key]:
            diff_settings[key] = [curr_settings[key], new_settings[key]]
    return diff_settings

if __name__ == "__main__":
    copy_mod_files()
