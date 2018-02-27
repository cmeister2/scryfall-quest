#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test version information."""

import scryfall_quest


def test_version():
    """Test that the version string is present."""
    assert scryfall_quest.__version__ is not None
