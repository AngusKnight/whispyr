# -*- coding: utf-8 -*-

"""Tests for `whispyr` package"""

import base64
import httpretty
import pytest
import re

import whispyr

httpretty.HTTPretty.allow_net_connect = False


TEST_USERNAME = 'U53RN4M3'
TEST_PASSWORD = 'P4ZZW0RD'
TEST_API_KEY = 'V4L1D4P1K3Y'


@pytest.fixture
def whispir():
    return whispyr.Whispir(TEST_USERNAME, TEST_PASSWORD, TEST_API_KEY)


@httpretty.activate
def test_basic_auth(whispir):
    httpretty.register_uri(httpretty.GET, re.compile(r'.*', re.M), body='{}')
    whispir.request('get', 'workspaces')

    assert httpretty.has_request()
    request = httpretty.last_request()
    assert 'Authorization' in request.headers
    basic_auth = request.headers['Authorization']
    expected_basic = _basic_auth(TEST_USERNAME, TEST_PASSWORD)
    assert basic_auth == expected_basic


@httpretty.activate
def test_api_key_provided(whispir):
    httpretty.register_uri(httpretty.GET, re.compile(r'.*', re.M), body='{}')
    whispir.request('get', 'workspaces')

    assert httpretty.has_request()
    request = httpretty.last_request()
    assert 'apikey' in request.querystring
    api_key = request.querystring['apikey'][0]
    assert api_key == TEST_API_KEY


@httpretty.activate
def test_user_agent_is_set(whispir):
    httpretty.register_uri(httpretty.GET, re.compile(r'.*', re.M), body='{}')
    whispir.request('get', 'workspaces')

    assert httpretty.has_request()
    request = httpretty.last_request()
    assert 'User-Agent' in request.headers
    expexted_agent = 'whispyr/{}'.format(whispyr.__version__)
    assert request.headers['User-Agent'] == expexted_agent


def _basic_auth(username, password):
    username = username.encode('latin1')
    password = password.encode('latin1')
    b64auth = base64.b64encode(b':'.join((username, password)))
    return 'Basic {}'.format(b64auth.decode('utf-8'))
