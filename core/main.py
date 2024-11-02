#!/usr/bin/env python3
# -*- coding: utf-8 -*-"
"""
[pArAnoIA_Browser] by /psy (https://browser.03c8.net/)/ - 2020/2024

You should have received a copy of the GNU General Public License along
with pArAnoIA-Browser; if not, write to the Free Software Foundation, Inc., 51
Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""
import os, sys, re, random, socket, requests, time, urllib.parse, urllib.request, urllib.error

try:
    import gi
except:
    print("\nError importing: gi lib. \n\n To install it on Debian based systems:\n\n $ 'sudo apt-get install python3-gi' or 'pip3 install PyGObject'\n")
    sys.exit(2)

try:
    import pygeoip
except:
    print("\n[Error] [AI] Cannot import lib: pygeoip. \n\n To install it try:\n\n $ 'sudo apt-get install python3-geoip' or 'pip3 install pygeoip'\n")
    sys.exit(2)

from uuid import getnode

gi.require_version('Gtk', '3.0')
gi.require_version('WebKit', '3.0')

from gi.repository import Gtk, WebKit
from gi.repository import Gdk
Gdk.threads_init()

class Browser(object):
    def __init__(self):
        self.check_ip_service1 = 'https://checkip.org/' # set external check ip service-backup 1 [OK! 01/11/2024]
        self.home_website = "https://check.torproject.org" # Home website
        self.https_strict = "ON" # HTTPS(strict)
        self.navigation_mode = "EXPLORER" # Navigation mode
        self.logs_mode = "OFF" # logging mode
        self.tor_mode = "OFF" # TOR mode
        self.dns_prefetching = "ON" # DNS Prefetching
        self.javascript = "ON" # Javascript(flag) = No-Javascript [*]
        self.java = "ON" # Java*
        self.flash = "ON" # Flash*
        self.webaudio = "ON" # WebAudio*
        self.webgl = "ON" # WebGL/WebVideo*
        self.xss = "ON" # XSS audit
        self.cache = "ON" # Cache*
        self.styles = "ON" # Styles/Fonts*
        self.logs = [] # logged urls
        self.logo = "core/images/paranoia.jpeg" # set source path for logo img
        self.agents_file = "core/user-agents.txt" # set source path to retrieve user-agents
        self.geodb = "core/geo/GeoLiteCity.dat" # set source for geoip-DB
        self.agents = [] # generating available user-agents
        f = open(self.agents_file)
        agents = f.readlines()
        f.close()
        for agent in agents:
            self.agents.append(agent)
        self.builder = Gtk.Builder() 
        self.builder.add_from_file("core/browser.glade")
        self.builder.connect_signals(self)
        self.toolbar1 = self.builder.get_object("toolbar1")
        self.back = self.builder.get_object("back")
        self.forward = self.builder.get_object("forward")
        self.refresh = self.builder.get_object("refresh")
        self.stop = self.builder.get_object("stop")
        self.url = self.builder.get_object("url")
        self.spinner = self.builder.get_object("spinner")
        self.progressbar = self. builder.get_object("progressbar")
        self.scrolledwindow = self.builder.get_object("scrolledwindow")
        self.scrolledwindowinspector = self.builder.get_object("scrolledwindowinspector")
        self.scrolledwindowlogs = self.builder.get_object("scrolledwindowlogs")
        self.navigation_mode_img = self.builder.get_object("navigation_mode_img")
        self.navigation_mode_button = self.builder.get_object("navigation_mode_button")
        self.source_code_img = self.builder.get_object("source_code_img")
        self.source_code_button = self.builder.get_object("source_code_button")
        self.logs_img = self.builder.get_object("logs_img")
        self.logs_button = self.builder.get_object("logs_button")
        self.logs_view_buffer = self.builder.get_object("logs_view_buffer")
        self.top_panel = self.builder.get_object("top_panel")
        self.top_domain = self.builder.get_object("top_domain")
        self.hide_top_panel_img = self.builder.get_object("hide_top_panel_img")
        self.hide_top_panel_button = self.builder.get_object("hide_top_panel_button")
        self.toolbar = self.builder.get_object("toolbar")
        self.fullscreen_img = self.builder.get_object("fullscreen_img")
        self.fullscreen_button = self.builder.get_object("fullscreen_button")
        self.max_screen_img = self.builder.get_object("max_screen_img")
        self.max_screen_button = self.builder.get_object("max_screen_button")
        self.source_code_view_buffer = self.builder.get_object("source_code_view_buffer")
        self.source_code_text_view = self.builder.get_object("source_code_text_view")
        self.main_view_box_top = self.builder.get_object("main_view_box_top")
        self.main_view_box_foot = self.builder.get_object("main_view_box_foot")
        self.main_view_box_left = self.builder.get_object("main_view_box_left")
        self.https_mode_img = self.builder.get_object("https_mode_img")
        self.https_mode_button = self.builder.get_object("https_mode_button")
        self.tor_mode_img = self.builder.get_object("tor_mode_img")
        self.dns_img = self.builder.get_object("dns_img")
        self.dns_button = self.builder.get_object("dns_button")
        self.javascript_img = self.builder.get_object("javascript_img")
        self.javascript_button = self.builder.get_object("javascript_button")
        self.java_img = self.builder.get_object("java_img")
        self.java_button = self.builder.get_object("java_button")
        self.webaudio_img = self.builder.get_object("webaudio_img")
        self.webaudio_button = self.builder.get_object("webaudio_button")
        self.webgl_img = self.builder.get_object("webgl_img")
        self.webgl_button = self.builder.get_object("webgl_button")
        self.xss_img = self.builder.get_object("xss_img")
        self.xss_button = self.builder.get_object("xss_button")
        self.cache_img = self.builder.get_object("cache_img")
        self.cache_button = self.builder.get_object("cache_button")
        self.styles_img = self.builder.get_object("styles_img")
        self.styles_button = self.builder.get_object("styles_button")
        self.mac = self.builder.get_object("mac")
        self.ip_internal = self.builder.get_object("ip_internal")
        self.ip_external = self.builder.get_object("ip_external")
        self.ip_location = self.builder.get_object("ip_location")
        self.domain_name = self.builder.get_object("domain_name")
        self.domain_location = self.builder.get_object("domain_location")
        self.domain_lat = self.builder.get_object("domain_lat")
        self.domain_long = self.builder.get_object("domain_long")
        self.domain_code = self.builder.get_object("domain_code")
        self.useragent = self.builder.get_object("useragent")
        self.referer = self.builder.get_object("referer")
        self.windowsize = self.builder.get_object("windowsize")
        self.window = self.builder.get_object("window1")
        self.window.connect('destroy', lambda w: Gtk.main_quit())
        self.window.show_all()
        self.webview = WebKit.WebView()
        self.set_useragent()
        self.set_referer()
        self.set_navigation_settings()
        self.set_browser_settings()
        self.scrolledwindow.add(self.webview)
        self.webview.connect('title-changed', self.change_title)
        self.webview.connect('load-committed', self.change_url)
        self.webview.connect('load-committed', self.spinner_on)
        self.webview.connect('load_finished',self.spinner_off)
        self.webview.show() # start the whole show! ;-)
        self.get_mac() # get/set our MAC
        self.get_ip_internal() # get/set our IP(internal)
        self.get_ip_external() # get/set our IP(external)
        self.get_windowsize() # get/set our Window(size)
        self.main_view_box_top.show() # Websites (main view)
        self.main_view_box_foot.hide() # Shell
        self.main_view_box_left.hide() # Logs
        self.check_requests_tor() # at init and via urllib2

    def run(self, opts=None):
        Gtk.main()

    def set_navigation_settings(self):
        settings = WebKit.WebSettings()
        settings.set_property('user-agent', self.useragent.get_text()) # set User-agent
        self.webview.set_settings(settings)
        self.refresh_website()

    def set_browser_settings(self):
        settings = WebKit.WebSettings()         
        settings.set_property('enable-frame-flattening', 'False')
        settings.set_property('enable-fullscreen', 'False')
        settings.set_property('enable-html5-database', 'False')
        settings.set_property('enable-html5-local-storage', 'False')
        settings.set_property('enable-hyperlink-auditing', 'False')
        settings.set_property('media-playback-allows-inline', 'False')
        settings.set_property('media-playback-requires-user-gesture', 'False')
        settings.set_property('auto-load-images', 'False')
        settings.set_property('enable-caret-browsing', 'False')
        settings.set_property('enable-site-specific-quirks', 'False')
        settings.set_property('enable-smooth-scrolling', 'False')
        settings.set_property('print-backgrounds', 'False')
        settings.set_property('enable-dns-prefetching', 'True')
        settings.set_property('enable-scripts', 'False') # javascript
        settings.set_property('javascript-can-access-clipboard', 'False')
        settings.set_property('javascript-can-open-windows-automatically', 'False')
        settings.set_property("enable-java-applet", 'False')
        settings.set_property('enable-offline-web-application-cache', 'False')
        settings.set_property('enable-page-cache', 'False')
        settings.set_property('enable-private-browsing', 'True')
        settings.set_property('enable-webaudio', 'False')
        settings.set_property('enable-webgl', 'False')
        settings.set_property('enable-xss-auditor', 'True')
        settings.set_property('enable-page-cache', 'False')
        settings.set_property('enable-offline-web-application-cache', 'False')
        settings.set_property("enable-file-access-from-file-uris", "False") # hack.it! >;-)
        #settings.set_property('allow-modal-dialogs', 'False')
        #settings.set_property('enable-write-console-messages-to-stdout', 'False')
        #settings.set_property('draw-compositing-indicators', 'False')
        #settings.set_property('enable-accelerated-2d-canvas', 'False')
        #settings.set_property('enable-resizable-text-areas', 'False')
        #settings.set_property('enable-tabs-to-links', 'False')
        #settings.set_property('load-icons-ignoring-image-load-setting', 'False')
        self.webview.set_settings(settings)
        self.ipData = pygeoip.GeoIP(self.geodb) # load geodb

    def on_url_backspace(self, widget):
        url = widget.get_text()
        self.url.set_text("") # remove text from url-bar when focus-in-event

    def on_url_activate(self, widget):
        url = widget.get_text()
        url = self.check_url_spelling(url) # check for 'hints' when spelling at url bar
        self.url.set_text(url) # set url to bar
        self.set_domain_name(url) # set url to domain_name
        self.set_useragent() # set user-agent
        self.set_navigation_settings() # set navigation settings
        self.webview.open(url) # visit website
        self.check_geoip_visited_website(url) # set geoip (visited link)
        if self.home_website in url: # Home website
            self.on_visit_home_website()
        if self.logs_mode == "ON": # when logging mode in ON
            self.main_view_box_left.show() # be sure that logs view is also ON
            if url not in self.logs:
                self.logs.append(url) # add to logs list
                self.refresh_log() # refresh logs
        self.get_mac() # get/set our MAC
        self.get_ip_internal() # get/set our IP(internal)
        self.get_ip_external() # get/set our IP(external)
        self.set_useragent() # we want to change our HTTP User-Agent used to visit a site, on each request... and randomnly!
        self.get_windowsize() # get/set our window size
        html = self.get_html(url) # get source code from visited website

    def set_domain_name(self, url):
        domain_url = '.'.join(urllib.parse.urlparse(url).netloc.split('.')[-2:])
        self.domain_name.set_text("["+domain_url+"]")

    def check_url_spelling(self, url): # [rev: 26/06/2019]
        if self.home_website in url: # Home website
            url = self.home_website
        elif "!0" in url: # !0 = 03c8.net(author) / just link!
            url = 'https://03c8.net' # ;-) 
        elif "!deep" in url: # !deep = Torch(content) / just link!
            url = 'http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/'
        elif "!start" in url: # !start = StartPage(tems)
            url = str(url.split(' ',1)[1])
            url = 'https://www.startpage.com/do/search?limit=10&lang=english&format=html&query=' + url
        elif "!s" in url: # !s = DuckDuckGo(terms)
            if self.tor_mode == "OFF":
                url = str(url.split(' ',1)[1])
                url = "https://duckduckgo.com/?q=" + url
            else:
                url = "https://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion/" # duckduckGO (via TOR)
        elif "!dict" in url: # !dict = Cambridge Dictionary(words)
            url = str(url.split(' ',1)[1]) 
            url = 'https://dictionary.cambridge.org/dictionary/english/' + url
        elif "!map" in url: # !map = OpenStreetMaps(locations)
            url = str(url.split(' ',1)[1]) 
            url = 'https://www.openstreetmap.org/search?query=' + url
        elif "!w" in url: # !w = Wikipedia(terms)
            url = str(url.split(' ',1)[1]) 
            url = 'https://en.wikipedia.org/wiki/' + url
        elif "!video" in url: # !video = PeerTube(videos)
            url = str(url.split(' ',1)[1]) 
            url = 'https://video.hardlimit.com/search?search=' + url
        elif "!image" in url: # !image = DevianARt(images)
            url = str(url.split(' ',1)[1]) 
            url = 'https://www.deviantart.com/search?q=' + url
        elif "!nasa" in url: # !nasa = NASA(images)
            url = str(url.split(' ',1)[1]) 
            url = 'https://images.nasa.gov/search-results?q=' + url
        elif "!porn" in url: # !porn = PornHub(adult content)
            url = str(url.split(' ',1)[1]) 
            url = 'https://www.pornhub.com/video/search?search=' + url
        else:
            if url.startswith('https://'):
                url = url
            else:
                if url.startswith('http://'):
                    if self.https_strict == "ON":
                        url = url.replace('http://', "")
                        url = 'https://' + url
                        self.url.set_icon_from_stock(0, "gtk-dialog-authentication")
                    else:
                        url = url
                        self.url.set_icon_from_stock(0, "gtk-dialog-warning")
                else:
                    if self.https_strict == "ON":
                        url = 'https://' + url
                        self.url.set_icon_from_stock(0, "gtk-dialog-authentication")
                    else:
                        url = self.home_website # when non-supported go to Home 
        return url 

    def on_hide_top_panel_button_clicked(self, widget):
        hide_top_panel_img = self.hide_top_panel_img.get_stock()
        if hide_top_panel_img.stock_id == "gtk-remove":
            self.hide_top_panel_img.set_from_stock("gtk-add", 4)
            self.top_panel.hide()
            self.top_domain.hide()
        else:
            self.hide_top_panel_img.set_from_stock("gtk-remove", 4)
            self.top_panel.show()
            self.top_domain.show()

    def on_fullscreen_button_clicked(self, widget):
        fullscreen_img = self.fullscreen_img.get_stock()
        if fullscreen_img.stock_id == "gtk-zoom-fit":
            self.fullscreen_img.set_from_stock("gtk-leave-fullscreen", 4)
            self.top_panel.hide()
            self.top_domain.hide()
            self.toolbar.hide()
        else:
            self.fullscreen_img.set_from_stock("gtk-zoom-fit", 4)
            self.top_panel.show()
            self.top_domain.show()
            self.toolbar.show()
        self.get_windowsize() # get/set our window size

    def on_max_screen_button_toggled(self, widget):
        max_screen_img = self.max_screen_img.get_stock()
        if max_screen_img.stock_id == "gtk-fullscreen":
            self.max_screen_img.set_from_stock("gtk-leave-fullscreen", 4)
            self.window.fullscreen()
            self.get_warning_fixed_window() # get warning when maximized(fixed) size for Window
        else:
            self.max_screen_img.set_from_stock("gtk-fullscreen", 4)
            self.window.unfullscreen()
        self.get_windowsize() # get/set our window size

    def get_warning_fixed_window(self):
        msg = ("\n\nWait... ;-)\n\npArAnoIA is trying to evade screen/monitor tracking techniques.\n\nFullscreen mode will disable related contrameasures...\n\nAre you sure about keeping a fixed size?")
        dlg_img = Gtk.Image()
        dlg_img.set_from_file(os.path.join(self.logo))
        dlg_img.show()
        dlg = Gtk.MessageDialog(message_format=msg, image=dlg_img, parent=self.window)
        dlg.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        dlg.add_button(Gtk.STOCK_OK, Gtk.ResponseType.OK)
        dlg.set_default_response(Gtk.ResponseType.OK)
        dlg.set_title('Warning: Setting a fixed size for Window...')
        dlg.run()
        dlg.destroy()

    def get_html(self, website):
        self.webview.execute_script('oldtitle=document.title;document.title=document.documentElement.innerHTML;') 
        html = self.webview.get_main_frame().get_title() 
        self.webview.execute_script('document.title=oldtitle;') 
        return html 

    def get_mac(self):
        current_mac = self.mac.get_text() # we want to be sure about our MAC at init
        if current_mac == "255.255.255.255": # set by default at GUI level
            self.set_mac()

    def set_mac(self):
        mac = getnode() # to get physical address
        hex_mac = str(":".join(re.findall('..', '%012x' % mac)))
        self.mac.set_text(hex_mac)

    def get_ip_internal(self):
        current_ip_internal = self.ip_internal.get_text() # we want to be sure about our private IP (for internal LAN)
        if current_ip_internal == "127.0.0.1": # set by default at GUI level
            self.set_ip_internal()

    def set_ip_internal(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(("1.1.1.1", 1)) # black magic! /23-06-2019/ [UFONet+LoVe] ;-)
        except:
            print("\n[Info] Network is unaccesible: Aborting!\n")
            sys.exit(2)
        private_ip = s.getsockname()[0]
        s.close()
        self.ip_internal.set_text(private_ip)

    def get_ip_external(self):
        current_ip_external = self.ip_external.get_text() # we want to be sure about our public IP (for the Internet)
        if current_ip_external == "127.0.0.1": # set by default at GUI level
            self.set_ip_external()

    def set_ip_external(self):
        try:
            public_ip = self.external_ip # method 1: extracted from Home website
        except:
            try:
                public_ip = requests.get(self.check_ip_service1).text # method 2: direct request to third-party services
            except:
                public_ip = "127.0.0.1"
        if public_ip != "127.0.0.1": # check for geolocation
            self.check_geoip_ip_external(public_ip)
        self.ip_external.set_text(public_ip)
 
    def check_geoip_ip_external(self, ip):
        try:
            record = self.ipData.record_by_addr(ip)
            self.ip_location.set_text("["+str(record['country_name'])+"]")
        except:
            self.ip_location.set_text('[Unknown]')

    def check_geoip_visited_website(self, ip):
        domain_url = '.'.join(urllib.parse.urlparse(ip).netloc.split('.')[-2:])
        try:
            record = self.ipData.record_by_name(domain_url)
            self.domain_location.set_text("["+str(record['country_name'])+"]")
            self.domain_lat.set_text("(Lat: "+str(record['latitude'])+")")
            self.domain_long.set_text("(Long: "+str(record['longitude'])+")")
            self.domain_code.set_text("["+str(record['country_code'])+"]")
        except:
            self.domain_location.set_text('[Unknown]')
            self.domain_lat.set_text("(Lat: ?)")
            self.domain_long.set_text("(Long: ?)")
            self.domain_code.set_text("[?]")

    def set_useragent(self):
        user_agent = random.choice(self.agents).strip()  
        self.useragent.set_text(user_agent)

    def get_windowsize(self):
        windowsize = self.window.get_size()
        w, h = windowsize
        windowsize = str(w)+"x"+str(h)
        self.windowsize.set_text(windowsize) # set to 1024x768 by default

    def on_refresh_clicked(self, widget):
        self.webview.reload()

    def on_back_clicked(self, widget):
        self.webview.go_back()

    def on_forward_clicked(self, widget):
        self.webview.go_forward()

    def on_stop_clicked(self, widget):
        self.webview.stop_loading()

    def change_title(self, widget, frame, title):
        self.window.set_title('/pArAnoIA Browser/     |     ' + title)

    def change_url(self, widget, frame):
        uri = frame.get_uri()
        self.url.set_text(uri)
        self.back.set_sensitive(self.webview.can_go_back() )
        self.forward.set_sensitive(self.webview.can_go_forward() )

    def on_navigation_mode_button_toggled(self, widget):
        self.on_navigation_mode_img_button_press_event(self)

    def on_navigation_mode_img_button_press_event(self, widget):
        navigation_img = self.navigation_mode_img.get_stock()
        if navigation_img.stock_id == "gtk-orientation-landscape":
            self.navigation_mode_img.set_from_stock("gtk-find-and-replace", 4)
            self.navigation_mode = "INSPECTOR" # set navigation mode to: INSPECTOR
            self.start_inspector()
        else:
            self.navigation_mode_img.set_from_stock("gtk-orientation-landscape", 4)
            self.navigation_mode = "EXPLORER" # set navigation mode to: EXPLORER
            settings = WebKit.WebSettings()   
            settings.set_property('enable-developer-extras', False)
            self.webview.set_settings(settings)
            self.main_view_box_foot.hide()
        self.set_referer() # set referer according to Navigation mode

    def start_inspector(self):
        view = self.webview
        self.webview = WebKit.WebView()
        settings = WebKit.WebSettings()   
        settings.set_property('enable-developer-extras', True)
        view.set_settings(settings)
        self.inspector = view.get_inspector()
        self.inspector.connect("inspect-web-view", self.inspect)
        self.webview = WebKit.WebView()
        self.scrolledwindowinspector.add(self.webview)
        self.scrolledwindowinspector.show()
        self.source_code_text_view.hide()
        self.main_view_box_foot.show()
        
    def inspect(self, inspector, view):
        self.scrolledwindowinspector.show_all()
        self.webview.show()
        return self.webview
        
    def on_logs_button_toggled(self, widget):
        self.on_logs_img_button_press_event(self)

    def on_logs_img_button_press_event(self, widget):
        settings = WebKit.WebSettings()
        logs_img = self.logs_img.get_stock()
        if logs_img.stock_id == "gtk-no":
            self.logs_img.set_from_stock("gtk-yes", 4)
            self.logs_mode = "OFF" # set logging mode to: OFF
            settings.set_property('enable-private-browsing', 'True')
            self.main_view_box_left.hide()
        else:
            self.logs_img.set_from_stock("gtk-no", 4)
            self.logs_mode = "ON" # set logging mode to: ON
            settings.set_property('enable-private-browsing', 'False')
            self.main_view_box_left.show()
        self.webview.set_settings(settings)

    def refresh_log(self):
        self.logs_view_buffer.set_text("")
        for log in self.logs:
            iter = self.logs_view_buffer.get_end_iter()
            self.logs_view_buffer.insert(iter, log + "\n")

    def show_source_code(self, url):
        self.webviewsource = WebKit.WebView()
        self.webviewsource.open(url)
        def get_source(webobj, frame):
            source = self.webviewsource.get_main_frame().get_data_source().get_data()
            code_buffer = str(self.source_code_view_buffer.set_text(source.str))
        self.webviewsource.connect("load-finished", get_source)
        browser_settings = self.webviewsource.get_settings()
        browser_settings.set_property('enable-default-context-menu', True)
        browser_settings.set_property('enable-accelerated-compositing', True)
        browser_settings.set_property('enable-file-access-from-file-uris', True)
        self.webviewsource.set_settings(browser_settings)
        self.set_source_code_on_url_icon() # set source_code at url bar
        self.scrolledwindowinspector.hide()
        self.source_code_text_view.show()
        self.main_view_box_foot.show()

    def set_referer(self):
        referer = self.referer.get_text()
        if self.navigation_mode == "INSPECTOR":
            self.referer.set_text("127.0.0.1") # turn referer into INSPECTOR mode
        else:
            self.referer.set_text("-") # turn referer into EXPLORER mode

    def refresh_website(self):
        url = self.url.get_text()
        self.webview.open(url)

    def on_styles_button_toggled(self, widget):
        self.on_styles_button_press_event(self)

    def on_styles_button_press_event(self, widget):
        settings = WebKit.WebSettings()
        styles_img = self.styles_img.get_stock()
        if styles_img.stock_id == "gtk-yes":
            self.styles_img.set_from_stock("gtk-no", 4)
            self.styles = "OFF"
            settings.set_property('enable-frame-flattening', 'True')
            settings.set_property('enable-fullscreen', 'True')
            settings.set_property('enable-html5-database', 'True')
            settings.set_property('enable-html5-local-storage', 'True')
            settings.set_property('enable-hyperlink-auditing', 'True')
            settings.set_property('media-playback-allows-inline', 'True')
            settings.set_property('media-playback-requires-user-gesture', 'True')
            settings.set_property('auto-load-images', 'True')
            settings.set_property('enable-caret-browsing', 'True')
            settings.set_property('enable-site-specific-quirks', 'True')
            settings.set_property('enable-smooth-scrolling', 'True')
        else:
            self.styles_img.set_from_stock("gtk-yes", 4)
            self.styles = "ON"
            settings.set_property('enable-frame-flattening', 'False')
            settings.set_property('enable-fullscreen', 'False')
            settings.set_property('enable-html5-database', 'False')
            settings.set_property('enable-html5-local-storage', 'False')
            settings.set_property('enable-hyperlink-auditing', 'False')
            settings.set_property('media-playback-allows-inline', 'False')
            settings.set_property('media-playback-requires-user-gesture', 'False')
            settings.set_property('auto-load-images', 'False')
            settings.set_property('enable-caret-browsing', 'False')
            settings.set_property('enable-site-specific-quirks', 'False')
            settings.set_property('enable-smooth-scrolling', 'False')
        self.webview.set_settings(settings)
        self.refresh_website()

    def on_cache_button_toggled(self, widget):
        self.on_cache_button_press_event(self)

    def on_cache_button_press_event(self, widget):
        settings = WebKit.WebSettings()
        cache_img = self.cache_img.get_stock()
        if cache_img.stock_id == "gtk-yes":
            self.cache_img.set_from_stock("gtk-no", 4)
            self.cache = "OFF"

            settings.set_property('enable-page-cache', 'True')
            settings.set_property('enable-offline-web-application-cache', 'True')

        else:
            self.cache_img.set_from_stock("gtk-yes", 4)
            self.cache = "ON"
            settings.set_property('enable-page-cache', 'False')
            settings.set_property('enable-offline-web-application-cache', 'False')
        self.webview.set_settings(settings)
        self.refresh_website()

    def on_xss_button_toggled(self, widget):
        self.on_xss_button_press_event(self)

    def on_xss_button_press_event(self, widget):
        settings = WebKit.WebSettings()
        xss_img = self.xss_img.get_stock()
        if xss_img.stock_id == "gtk-yes":
            self.xss_img.set_from_stock("gtk-no", 4)
            self.xss = "OFF"
            settings.set_property('enable-xss-auditor', 'False')

        else:
            self.xss_img.set_from_stock("gtk-yes", 4)
            self.xss = "ON"
            settings.set_property('enable-xss-auditor', 'True')
        self.webview.set_settings(settings)
        self.refresh_website()

    def on_webgl_button_toggled(self, widget):
        self.on_webgl_button_press_event(self)

    def on_webgl_button_press_event(self, widget):
        settings = WebKit.WebSettings()
        webgl_img = self.webgl_img.get_stock()
        if webgl_img.stock_id == "gtk-yes":
            self.webgl_img.set_from_stock("gtk-no", 4)
            self.webgl = "OFF"
            settings.set_property("enable-webgl", 'False')
        else:
            self.webgl_img.set_from_stock("gtk-yes", 4)
            self.webgl = "ON"
            settings.set_property("enable-webgl", 'True')
        self.webview.set_settings(settings)
        self.refresh_website()

    def on_webaudio_button_toggled(self, widget):
        self.on_webaudio_button_press_event(self)

    def on_webaudio_button_press_event(self, widget):
        settings = WebKit.WebSettings()
        webaudio_img = self.webaudio_img.get_stock()
        if webaudio_img.stock_id == "gtk-yes":
            self.webaudio_img.set_from_stock("gtk-no", 4)
            self.webaudio = "OFF"
            settings.set_property("enable-webaudio", 'False')
        else:
            self.webaudio_img.set_from_stock("gtk-yes", 4)
            self.webaudio = "ON"
            settings.set_property("enable-webaudio", 'True')
        self.webview.set_settings(settings)
        self.refresh_website()

    def on_java_button_toggled(self, widget):
        self.on_java_button_press_event(self)

    def on_java_button_press_event(self, widget):
        settings = WebKit.WebSettings()
        java_img = self.java_img.get_stock()
        if java_img.stock_id == "gtk-yes":
            self.java_img.set_from_stock("gtk-no", 4)
            self.java = "OFF"
            self.flash = "OFF"
            settings.set_property("enable-java-applet", 'False')
        else:
            self.java_img.set_from_stock("gtk-yes", 4)
            self.java = "ON"
            self.flash = "ON"
            settings.set_property("enable-java-applet", 'True')
        self.webview.set_settings(settings)
        self.refresh_website()

    def on_javascript_button_toggled(self, widget):
        self.on_javascript_button_press_event(self)

    def on_javascript_button_press_event(self, widget):
        settings = WebKit.WebSettings()
        javascript_img = self.javascript_img.get_stock()
        if javascript_img.stock_id == "gtk-yes":
            self.javascript_img.set_from_stock("gtk-no", 4)
            self.javascript = "OFF"
            settings.set_property('enable-scripts', 'False')
            settings.set_property('javascript-can-access-clipboard', 'False')
            settings.set_property('javascript-can-open-windows-automatically', 'False')
        else:
            self.javascript_img.set_from_stock("gtk-yes", 4)
            self.javascript = "ON"
            settings.set_property('enable-scripts', 'True')
            settings.set_property('javascript-can-access-clipboard', 'False')
            settings.set_property('javascript-can-open-windows-automatically', 'True')
        self.webview.set_settings(settings)
        self.refresh_website()

    def on_dns_button_toggled(self, widget):
        self.on_dns_button_press_event(self)

    def on_dns_button_press_event(self, widget):
        settings = WebKit.WebSettings()
        dns_img = self.dns_img.get_stock()
        if dns_img.stock_id == "gtk-yes":
            self.dns_img.set_from_stock("gtk-no", 4)
            self.dns_prefetching = "OFF"
            settings.set_property('enable-dns-prefetching', 'False')
        else:
            self.dns_img.set_from_stock("gtk-yes", 4)
            self.dns_prefetching = "ON"
            settings.set_property('enable-dns-prefetching', 'True')
        self.webview.set_settings(settings)

    def on_https_mode_button_toggled(self, widget):
        self.on_https_mode_img_button_press_event(self)

    def on_https_mode_img_button_press_event(self, widget):
        https_img = self.https_mode_img.get_stock()
        if https_img.stock_id == "gtk-yes":
            self.https_mode_img.set_from_stock("gtk-no", 4)
            self.https_strict = "OFF"
        else:
            self.https_mode_img.set_from_stock("gtk-yes", 4)
            self.https_strict = "ON"
        self.set_warning_on_url_icon() # set warning at url bar
        self.refresh_website()

    def on_source_code_button_toggled(self, widget):
        self.on_source_code_img_button_press_event(self)

    def on_source_code_img_button_press_event(self, widget):
        url = self.url.get_text()
        if url.startswith("http") or url.startswith("source-code"):
            self.show_source_code(url)

    def set_source_code_on_url_icon(self):
        uri = self.url.get_text()
        url_primary_icon_name = self.url.get_icon_stock(0)
        if url_primary_icon_name == "gtk-dialog-authentication" or url_primary_icon_name == "gtk-home" or url_primary_icon_name == "gtk-warning":
            self.url.set_icon_from_stock(0, "gtk-properties")
            if uri.startswith("http://"):
                uri = uri.replace("http://", "")
            elif uri.startswith("https://"):
                uri = uri.replace("https://", "")
            url = "source-code: " + uri
            if "/" in url:
                url = url.replace("/", "")
            self.url.set_text(url)
            self.main_view_box_top.hide()
            self.main_view_box_foot.show()
        else:
            if "source-code" in uri:
                uri = uri.replace("source-code: ", "")
                check_default = "https://" + uri
                if check_default == self.home_website: # Home site detected! ;-)
                    self.url.set_icon_from_stock(0, "gtk-home")
                    uri = 'https://' + uri
                else:
                    if self.https_strict == "ON":
                        self.url.set_icon_from_stock(0, "gtk-dialog-authentication")
                        uri = 'https://' + uri
                    else:
                        self.url.set_icon_from_stock(0, "gtk-dialog-warning")
                        uri = 'http://' + uri
                self.url.set_text(uri)
                self.main_view_box_top.show()
                self.main_view_box_foot.hide()
                self.set_useragent()
                self.set_navigation_settings()
                self.webview.open(uri) # re-visit website after review source code

    def set_warning_on_url_icon(self):
        url_primary_icon_name = self.url.get_icon_stock(0)
        if url_primary_icon_name == "gtk-dialog-authentication" or url_primary_icon_name == "gtk-home" or url_primary_icon_name == "gtk-properties":
            self.url.set_icon_from_stock(0, "gtk-dialog-warning")
        else:
            self.url.set_icon_from_stock(0, "gtk-dialog-authentication")

    def on_visit_home_website(self):
        url_primary_icon_name = self.url.get_icon_stock(0)
        self.url.set_icon_from_stock(0, "gtk-home") # sweet home-lab ;-)
        html = self.get_html(self.home_website)
        self.check_html_tor(html) # check TOR via html
        self.extract_ip_external_from_home_website(html) # extract public IP from Home website
        self.check_geoip_visited_website(self.home_website) # set geoip (Home)

    def check_requests_tor(self): # check for TOR via direct request
        tor_reply = urllib.request.urlopen(self.home_website).read() # check if TOR is enabled
        if not tor_reply or 'Congratulations'.encode('utf-8') not in tor_reply:
            self.tor_mode = "OFF"
            self.tor_mode_img.set_from_stock("gtk-no", 4)
        else:
            self.tor_mode = "ON"
            self.tor_mode_img.set_from_stock("gtk-yes", 4)
        self.set_useragent()
        self.set_navigation_settings()
        self.set_domain_name(self.home_website) # set url to domain_name
        self.webview.open(self.home_website) # open Home website by default
        self.check_geoip_visited_website(self.home_website) # set geoip (Home)
        url_primary_icon_name = self.url.get_icon_stock(0)
        self.url.set_icon_from_stock(0, "gtk-home") # sweet home-lab ;-)

    def check_html_tor(self, html):
        tor_mode_img = self.tor_mode_img.get_stock() # check for TOR 'network circuit'
        if 'Congratulations' not in html:
            self.tor_mode = "OFF"
            self.tor_mode_img.set_from_stock("gtk-no", 4)
        else:
            self.tor_mode = "ON"
            self.tor_mode_img.set_from_stock("gtk-yes", 4)

    def extract_ip_external_from_home_website(self, html):
        try:
            self.external_ip = html.split('<span style="color: #5d9bD3;">')[1].split('</span>')[0].strip()
        except:
            pass # other methods supported... ;-)

    def spinner_on(self,widget,frame):
        self.spinner.start()

    def spinner_off(self, widget,frame):
        self.spinner.stop()

if __name__ == "__main__":
    app = Browser()
    app.run()
