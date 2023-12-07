import subprocess
import os
def runcmd(cmd, verbose = False, *args, **kwargs):

    process = subprocess.Popen(
        cmd,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        text = True,
        shell = True
    )
    std_out, std_err = process.communicate()
    if verbose:
        print(std_out.strip(), std_err)
    pass

def downloadScratchRemoverModel():
    curDir = os.getcwd()
    command_str = "wget https://www.dropbox.com/s/5jencqq4h59fbtb/FT_Epoch_latest.pt" + " -P " + curDir +"/extensions/arifScratchRemoverWebUIExtention/"
    runcmd(command_str, verbose=True)


#runcmd("apt-get update && apt-get install libgl1", verbose = True)

