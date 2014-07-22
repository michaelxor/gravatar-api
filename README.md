gravatar-api
============

A Python wrapper for the [Gravatar API](https://en.gravatar.com/site/implement/).

## Requirements

The `gravatar` module has been tested with Python 2.7.  The module makes
use of the Python [requests](http://docs.python-requests.org/en/latest/)
module to communicate with the Gravatar API. This can be installed easily
via [pip](https://pypi.python.org/pypi/pip):

```bash
pip install requests
```

## Usage

The `gravatar` module provides some dead-simple functions for interacting
with Gravatar's API.

The only thing required to start fetching data is
an email address.

```python
import gravatar

g = Gravatar("email@example.com")  # must be the main email for the account
```

There are some helper functions for fetching common profile info, but
it's also possible to fetch a user's full profile and grab whatever you
need.

```python
# fetch some information from user profile
username = g.getUsername()
bio = g.getBio()

# or just get the whole profile, as a dict
profile = g.getProfile()
print profile['name']['formatted']
```

You can fetch the avatar URL, a formatted HTML img tag, or the raw
avatar image data itself.  It's also possible to save the avatar
locally.

```python
avatar_url = g.getAvatarUrl()
avatar_tag = g.getAvatarTag(image_size=256)  # 80px is Gravatar default
avatar_raw = g.getAvatar()  # raw image data
g.saveAvatar("avatar.jpg", image_size=64) # save locally
```

## Contributing

Anyone and everyone is welcome to contribute.

## License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
