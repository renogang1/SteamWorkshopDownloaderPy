import pathlib
import time
from steamcmd import SteamCMD

steam = SteamCMD()
print("Welcome to SteamWorkhopDownloaderPy!")
print("")

# user = input("Username:")
gameid = input("Game ID:")
workshopid = input("Workshop item ID:")
try:
    if gameid == "4000":
        pathh = "steamcmd\\steamapps\\workshop\\content\\" + str(gameid) + "\\" + str(workshopid) + "\\"
        steam.download("anonymous", "", gameid, workshopid)
        time.sleep(20)
        for path in pathlib.Path("steamcmd\\steamapps\\workshop\\content\\" + str(gameid) + "\\" + str(workshopid) + "\\").iterdir():
            if path.is_file():
                old_name = path.stem
                old_extension = path.suffix
                directory = path.parent

                new_name = str(workshopid) + old_extension

                path.rename(pathlib.Path(directory, new_name))
        time.sleep(5)
        steam.extractgmod(pathh + workshopid + ".gma", "files\\" + workshopid + "\\")
    else:
        steam.download("anonymous", "", gameid, workshopid)
except Exception as e:
    print(str(e))
