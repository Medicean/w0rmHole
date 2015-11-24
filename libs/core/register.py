# coding:utf-8
from libs.core.config import PAYLOAD

def register(pocClass):
    PAYLOAD.poc = pocClass()
