#!/usr/bin/env python3

def raise_exception():
    try:
        raise TypeError  
    except TypeError:
        return None
