"""
Recipe Manager - Main module.
"""
import sys

VERSION = "0.2.0"

def run(args):
    """Main entry point."""
    print(f"Recipe Manager v{VERSION}")
    if args:
        print(f"Processing: {', '.join(args)}")
        process(args)
    else:
        print("Usage: python recipe.py [arguments]")
        print("Try: python recipe.py --help")

def process(args):
    """Process input arguments."""
    entries = []
    for arg in args:
        result = arg.strip()
        if result:
            entries.append(result)
            print(f"  Processed: {result}")
    print(f"\nTotal: {len(entries)} items processed")
    return entries

def main():
    run(sys.argv[1:])

if __name__ == "__main__":
    main()
