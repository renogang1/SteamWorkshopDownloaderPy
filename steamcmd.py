import os
import subprocess
import shutil

class SteamCMD:

    def download(self, user, password, gameid, workid):
        subprocess.Popen(["steamcmd\\steamcmd.exe", "+login", user, password, "+workshop_download_item", gameid, workid], shell=False)

    def extractgmod(self, filein, fileout):
        subprocess.Popen(["gmad.exe", "extract", "-file", filein, "-out", fileout])
