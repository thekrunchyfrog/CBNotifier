import mechanize
import cookielib
from bs4 import BeautifulSoup


class GatherData:

    baseURL = "https://chaturbate.com"
    loginURL = baseURL + "/auth/login/"
    followedCamsURL = baseURL + "/followed-cams/"

    def getOnlineFollowedModels(self, username, password):

        br = mechanize.Browser()

        br.set_handle_equiv(True)
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

        online = []

        r = br.open(self.followedCamsURL)
        soup = BeautifulSoup(r.read(), 'html.parser')

        pageCount = self.getPageCount(soup)

        for page in range(1, pageCount + 1):
            r = br.open(self.followedCamsURL + "/?page=" + str(page))

            soup = BeautifulSoup(r.read(), 'html.parser')
            response = soup.find_all('li', class_='cams')

            for res in response:
                if res.text != "offline":
                    name = res.parent.parent.parent.img.get('alt', '')[:-12]
                    modelURL = self.baseURL + "/" + name
                    thumbnail = res.parent.parent.parent.img.get('src')
                    timeOnline = res.text[:res.text.find(",")]
                    girl = {'name': name, 'timeOnline': timeOnline, 'url': modelURL, 'thumbnail': thumbnail}
                    online.append(girl)
                else:
                    followed_cams = {'online': online}
                    return followed_cams

        followed_cams = {'online': online}

        r.close()

        return followed_cams

    def getAllFollowedModels(self, username, password):

        br = mechanize.Browser()

        br.set_handle_equiv(True)
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

        followed = []

        r = br.open(self.followedCamsURL)
        soup = BeautifulSoup(r.read(), 'html.parser')

        pageCount = self.getPageCount(soup)

        for page in range(1, pageCount + 1):
            r = br.open(self.followedCamsURL + "/?page=" + str(page))

            soup = BeautifulSoup(r.read(), 'html.parser')
            response = soup.find_all('li', class_='cams')

            for res in response:
                name = res.parent.parent.parent.img.get('alt', '')[:-12]
                modelURL = self.baseURL + "/" + name
                thumbnail = res.parent.parent.parent.img.get('src')
                timeOnline = res.text[:res.text.find(",")]
                if res.text == "offline":
                    timeOnline = "offline"
                girl = {'name': name, 'timeOnline': timeOnline, 'url': modelURL, 'thumbnail': thumbnail}
                followed.append(girl)

        followed_cams = {'followed': followed}

        r.close()

        return followed_cams

    def getFeatured(self):

        br = mechanize.Browser()

        br.set_handle_equiv(True)
        br.set_handle_redirect(True)
        br.set_handle_referer(True)
        br.set_handle_robots(False)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

        featured = []

        r = br.open(self.baseURL)
        soup = BeautifulSoup(r.read(), 'html.parser')

        pageCount = self.getPageCount(soup)

        for page in range(1, pageCount + 1):
            r = br.open(self.followedCamsURL + "/?page=" + str(page))

            soup = BeautifulSoup(r.read(), 'html.parser')
            response = soup.find_all('li', class_='cams')

            for res in response:
                name = res.parent.parent.parent.img.get('alt', '')[:-12]
                modelURL = self.baseURL + "/" + name
                thumbnail = res.parent.parent.parent.img.get('src')
                timeOnline = res.text[:res.text.find(",")]
                if res.text == "offline":
                    timeOnline = "offline"
                girl = {'name': name, 'timeOnline': timeOnline, 'url': modelURL, 'thumbnail': thumbnail}
                featured.append(girl)

        print len(featured)
        featured_cams = {'featured': featured}

        r.close()

        return featured_cams

    def getModelInfo(self, modelName):

        br = mechanize.Browser()

        br.set_handle_equiv(True)
        br.set_handle_redirect(True)
        br.set_handle_referer(True)
        br.set_handle_robots(False)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

        modelURL = self.baseURL + "/" + modelName

        r = br.open(modelURL)
        soup = BeautifulSoup(r.read(), 'html.parser')

        bioKeys = soup.select('div.bio dt', limit=12)
        bioValues = soup.select('div.bio dd', limit=12)

        r.close()

        info = {}

        i = 0
        for bioKey in bioKeys:
            if self.elementToFormattedString(bioKey, 4) == "Followers:":
                x = 5
            else:
                x = 4

            info[self.elementToFormattedString(bioKey, 4)[:-1]] = self.elementToFormattedString(bioValues[i], x)
            i += 1

        return info

    def getPageCount(self, soupObj):

        response = soupObj.find_all('a', class_='endless_page_link')

        pages = []
        for res in response:
            if res.text != "next":
                pages.append(int(res.text))

        return max(pages)

    def elementToFormattedString(self, element, tagSize):
        return str(element)[tagSize:- (tagSize + 1)]
