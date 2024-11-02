#!/usr/bin/env python3
# -*- coding: utf-8 -*-"
"""
[pArAnoIA_Browser] by /psy (https://browser.03c8.net/)/ - 2020/2024

You should have received a copy of the GNU General Public License along
with pArAnoIA-Browser; if not, write to the Free Software Foundation, Inc., 51
Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""
import sys, time

if sys.version_info[0] != 3:
    sys.exit("Sorry, pArAnoIA-Browser requires Python >= 3")

libs = ("GeoIP", "python-geoip", "pygeoip", "requests", "pgi", "PyGObject")
    
import subprocess, os

def checkeuid():
    try:
        euid = os.geteuid()
    except:
        sys.exit(2) # return
    return euid

def install(package):
    subprocess.run(["python3", "-m", "pip", "install", "--upgrade", "pip", "--no-warn-script-location", "--root-user-action=ignore"])
    subprocess.run(["python3", "-m", "pip", "install", "pycurl", "--upgrade", "--no-warn-script-location", "--root-user-action=ignore"])
    for lib in libs:
        subprocess.run(["python3", "-m", "pip", "install", lib, "--no-warn-script-location", "--ignore-installed", "--root-user-action=ignore"])

if __name__ == '__main__':
    euid = checkeuid()
    if euid != 0:
        try:
            args = ['sudo', sys.executable] + sys.argv + [os.environ]
            os.execlpe('sudo', *args)
        except: 
            sys.exit()
        sys.exit()
    os.system("sudo apt-get install -y --no-install-recommends python3-geoip python3-requests libgeoip1 libgeoip-dev python3-gi libcairo2-dev libgirepository1.0-dev gir1.2-webkit-3.0")
    install(libs)
    print("\n[pArAnoIA] Setup has been completed!. You can now try to run: python3 pArAnoIA.py\n")
