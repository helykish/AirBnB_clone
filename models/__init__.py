#!/usr/bin/python3
"""models dir __init__ some files"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
