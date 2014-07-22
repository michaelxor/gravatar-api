import requests
import hashlib
import json

class Gravatar:
    url_base = "http://www.gravatar.com"
    email = ""
    profile = None
    avatar = {}

    def __init__(self, email):
        self.email = self.gravatize(email)


    def gravatize(self, email):
        return hashlib.md5(str.lower(str.strip(email))).hexdigest()


    def getProfileUrl(self, response_format="json"):
        return "{0}/{1}.{2}".format(self.url_base, self.email, response_format)


    def getProfile(self, response_format="json"):
        if self.profile is None:
            r = requests.get(self.getProfileUrl(response_format))

            if not r.ok:
                return None

            # parse, if json
            if response_format == "json":
                self.profile = json.loads(r.text)['entry'][0]
            else:
                self.profile = r.text

        return self.profile


    def getUsername(self):
        return self.getProfile()['preferredUsername']


    def getFullname(self):
        return self.getProfile()['name']['formatted']


    def getAboutMe(self):
        return self.getProfile()['aboutMe']


    def getBio(self):
        return self.getAboutMe()


    def getAvatarUrl(self, image_size=None):
        payload = {
            's' : image_size
        }
        req = requests.Request("GET",
            "{0}/avatar/{1}.jpg".format(self.url_base, self.email),
            params=payload
        )
        prepped = req.prepare()

        return prepped.url


    def getAvatar(self, image_size=None):
        if image_size not in self.avatar.keys():
            request_url = self.getAvatarUrl(image_size)
            r = requests.get(request_url, stream=True)

            if not r.ok:
                return None

            avatar = ""
            for block in r.iter_content(1024):
                if not block:
                    break

                avatar += block

            self.avatar[image_size] = avatar

        return self.avatar[image_size]


    def saveAvatar(self, filename, image_size=None):
        with open(filename, 'wb') as handle:
            handle.write(self.getAvatar(image_size))


    def getAvatarTag(self, image_size=None):
        return '<img src="{0}"{1}>'.format(self.getAvatarUrl(image_size), ' width="{0}" height="{0}"'.format(image_size) if image_size is not None else '')

