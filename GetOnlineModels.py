import mechanize
import cookielib
from bs4 import BeautifulSoup


class GetOnlineModels:

    baseURL = "https://chaturbate.com"
    loginURL = baseURL + "/auth/login/"
    followedCamsURL = baseURL + "/followed-cams/"

    def myModels(self, username, password):
        # Browser
        br = mechanize.Browser()

        # Cookie Jar
        cj = cookielib.LWPCookieJar()
        br.set_cookiejar(cj)

        # Browser options
        br.set_handle_equiv(True)
        br.set_handle_gzip(True)
        br.set_handle_redirect(True)
        br.set_handle_referer(True)
        br.set_handle_robots(False)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

        r = br.open(self.loginURL)

        br.form = list(br.forms())[0]
        br["username"] = username
        br["password"] = password

        response = br.submit()

        r = br.open(self.followedCamsURL)

        soup = BeautifulSoup(r.read(), 'html.parser')
        response = soup.find_all('li', class_='cams')

        online = []

        for res in response:
            if res.text != "offline":
                name = res.parent.parent.parent.img.get('alt', '')[:-12]
                modelURL = self.baseURL + "/" + name
                thumbnail = res.parent.parent.parent.img.get('src')
                timeOnline = res.text[:res.text.find(",")]
                girl = {'name': name, 'timeOnline': timeOnline, 'url': modelURL, 'thumbnail': thumbnail}
                online.append(girl)
            else:
                break

        followed_cams = {'online': online}

        return followed_cams
