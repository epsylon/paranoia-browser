
----------

  pArAnoIA - is a toolkit designed to navigate/surf the Internet.

 + Web:  https://browser.03c8.net

  ![pArAnoIA](https://browser.03c8.net/paranoia/paranoia-welcome_small.png "pArAnoIA Welcome")

  Main features are:

       - AutoSpoofing: User-Agent, Referer, Window(size)...
       - TOR (proxy support)
       - DNS (prefetching)
       - XSS Audit
       - Cache evasion
       - HTTPS/SSL strict only
       - PrivateBrowsing mode (no logs!)
       - LiveInspector (extra developers tools)
       - Source Code viewer
       - Geolocation (domains visited, user IP...)
       - NoStyles: CSS, images, fonts, etc...
       - NoScripts: Javascript, Java, WebGL, WebAudio, etc..
       - Spelling "hints" to: Wikipedia, NASA, Cambridge Dictionary, OpenStreetmaps, PornHub...
       - Different "privacy based" search engines supported: DuckDuckGo, StartPage
       - DarkWeb search engine supported: Torch!
       - [...]

  Current version (v0.2) is on "beta" development.

  ![pArAnoIA](https://browser.03c8.net/paranoia/paranoia-main_small.png "pArAnoIA Main")

----------

#### Installing:

  pArAnoIA runs on many platforms. It requires Python (3.x) and the following libraries:

       python3-gi - Python 3 bindings for gobject-introspection libraries
       python3-geoip - Python3 bindings for the GeoIP IP-to-country resolver library
       python3-requests - elegant and simple HTTP library for Python3, built for human beings
       libgirepository1.0-dev - Library for handling GObject introspection data (development files)

  You can automatically get all required libraries using (as root):

       sudo python setup.py install

  For manual installation, on Debian-based systems (ex: Ubuntu), run: 

       sudo apt-get install python3-gi python3-geoip python3-requests libgirepository1.0-dev

  On other systems such as: Kali, Ubuntu, ArchLinux, ParrotSec, Fedora, etc... also run:

       pip3 install requests
       pip3 install PyGObject
       pip3 install pygeoip

----------

####  License:

  pArAnoIA is released under the GPLv3. You can find the full license text
in the [LICENSE](./docs/LICENSE) file.

----------

####  Screenshots (current version!):

  ![pArAnoIA](https://browser.03c8.net/paranoia/paranoia1_small.png "pArAnoIA Example1")

  ![pArAnoIA](https://browser.03c8.net/paranoia/paranoia2_small.png "pArAnoIA Example2")

  ![pArAnoIA](https://browser.03c8.net/paranoia/paranoia3_small.png "pArAnoIA Example3")


