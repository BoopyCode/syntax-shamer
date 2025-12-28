#!/usr/bin/env python3
"""Syntax Shamer - Because your editor is judging you silently."""

import ast
import sys
import os
from pathlib import Path

# Shame levels - because not all errors are created equal
SHAME_LEVELS = {
    'SyntaxError': "🔴 MORTAL SIN - Did you even look at the screen?",
    'IndentationError': "🟠 CARDINAL SIN - Python is not a free-form poem",
    'TabError': "🟡 HERESY - Tabs and spaces in unholy matrimony",
    'NameError': "🔵 OOPSIE - Calling ghosts that don't exist",
    'TypeError': "🟣 CONFUSION - Trying to add apples to oranges",
}

def shame_file(filepath):
    """Publicly shame a Python file for its syntax crimes."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # The ultimate syntax test - if ast can't parse it, you're guilty
        ast.parse(content)
        print(f"✅ {filepath} - Surprisingly competent! No shame today.")
        return True
        
    except SyntaxError as e:
        # Extract the shameful error type
        error_type = type(e).__name__
        shame_msg = SHAME_LEVELS.get(error_type, "⚫️ MYSTERY ERROR - Even Python is confused")
        
        print(f"\n🎭 SYNTAX SHAME ALERT! 🎭")
        print(f"File: {filepath}")
        print(f"Crime: {shame_msg}")
        print(f"Evidence: {e.msg}")
        print(f"Line {e.lineno}: {e.text or '??? (probably something terrible)'}")
        print(f"{'^' * (e.offset or 1)} Here's your crime scene!")
        return False
        
    except Exception as e:
        print(f"⚠️  {filepath} - Failed to read: {e}")
        return False

def main():
    """Judge all the files, let God sort them out."""
    if len(sys.argv) < 2:
        print("Usage: python syntax_shamer.py <file.py> [file2.py ...]", file=sys.stderr)
        print("Example: python syntax_shamer.py my_broken_code.py", file=sys.stderr)
        sys.exit(1)
    
    all_clean = True
    for filepath in sys.argv[1:]:
        if not Path(filepath).exists():
            print(f"❌ {filepath} - File not found (that's a different kind of error)")
            all_clean = False
            continue
            
        if not shame_file(filepath):
            all_clean = False
    
    if all_clean:
        print("\n🎉 All files are syntax-shaming-free! You may proceed.")
    else:
        print("\n💀 Some files need repentance. Fix them before they multiply.")
        sys.exit(1)

if __name__ == "__main__":
    main()
