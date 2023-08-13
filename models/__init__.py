#!/usr/bin/python3
"""__init__ magic method for models directory"""
from models.engine.file_storage import FileStorage
import models


storage = FileStorage()
storage.reload()
