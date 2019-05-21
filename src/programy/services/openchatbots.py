"""
Copyright (c) 2016-2019 Keith Sterling http://www.keithsterling.com

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from programy.config.brain.openchatbots import BrainOpenChatBotsConfiguration


class OpenChatBot(object):

    def __init__(self, name, url, method, authorization, api_key):
        self._name = name
        self._url = url
        self._method = method
        self._authorization = authorization
        self._api_key = api_key

    @property
    def name(self):
        return self._name

    @property
    def url(self):
        return self._url

    @property
    def method(self):
        return self._method

    @property
    def authorization(self):
        return self._authorization

    @property
    def api_key(self):
        return self._api_key


class OpenChatBotCollection(object):

    def __init__(self):
        self._openchatbots = {}

    def load_from_configuration(self, configuration: BrainOpenChatBotsConfiguration):

        names = configuration.openchatbots()
        for name in names:
            openchatbot_config = configuration.openchatbot(name)
            self._openchatbots[name.upper()] = OpenChatBot(openchatbot_config.section_name,
                                                           openchatbot_config.url,
                                                           openchatbot_config.method,
                                                           openchatbot_config.authorization,
                                                           openchatbot_config.api_key)
        return True

    def exists(self, name):
        return bool(name.upper() in self._openchatbots)

    def openchatbot(self, name):
        if self.exists(name):
            return self._openchatbots[name.upper()]

        return None
