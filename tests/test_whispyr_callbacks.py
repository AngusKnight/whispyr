# -*- coding: utf-8 -*-

"""Tests for `whispyr` callbacks"""

from whispyr import Callback


def test_create_callback(cassette, whispir, rand_name):
    callback = whispir.callbacks.create(projectName=rand_name, status='A')
    assert isinstance(callback, Callback)
    assert 'id' in callback


def test_list_callbacks(cassette, whispir):
    callbacks = whispir.callbacks.list()
    callbacks = list(callbacks)
    assert len(callbacks) > 0
    for callback in callbacks:
        _check_callback(callback)


def test_show_callback(whispir, callback, cassette):
    callback = whispir.callbacks.show(callback['id'])
    _check_callback(callback)


def _check_callback(callback):
    assert isinstance(callback, Callback)
    assert 'id' in callback
    assert 'link' in callback
    assert 'name' in callback
    assert 'url' in callback
