#!/usr/bin/env python3
"""
Project root directory definition module.

Provides the ROOT_DIR constant that points to the application's root directory,
enabling relative path resolution throughout the application.
"""
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

