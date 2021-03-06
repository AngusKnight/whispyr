# -*- coding: utf-8 -*-

"""Top-level package for whispyr."""

__author__ = """Grigory Starinkin"""
__email__ = 'starinkin@gmail.com'
__version__ = '0.3.1'

from .whispyr import Whispir, WhispirRetry

from .whispyr import Message, MessageStatus, MessageResponse, Template, \
    Workspace, ResponseRule, Contact, App, Callback

from .whispyr import WhispirError, ClientError, ServerError, JSONDecodeError

__all__ = [
    # Client
    'Whispir', 'WhispirRetry',
    # Resources
    'Message', 'MessageStatus', 'MessageResponse', 'Template', 'Workspace',
    'ResponseRule', 'Contact', 'App', 'Callback'
    # Errors
    'WhispirError', 'ClientError', 'ServerError', 'JSONDecodeError'
]
