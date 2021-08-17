# -*- coding: utf-8 -*-

# Copyright (C) 2020 Botir Ziyatov <botirziyatov@gmail.com>
# This program is free software: you can redistribute it and/or modify

from typing import Dict, List
import requests

class sqbCurrency(object):
    url = ""

    def __init__(self, url="https://sqb.uz/uz/exchange-rate/json/"):
        self.url = url

    def _request(self, endpoint, params=None):
        if params is None:
            params = {}
        response = requests.get(self.url + endpoint, {**params})
        response.raise_for_status()
        if response:
            return response.json()
        else:
            return False

    def getCurrency(self) -> List[Dict[str, int]]:
        """
        :return: The latest amount of total confirmed cases, deaths, and recoveries.
        """
        data = self._request("")
        return data