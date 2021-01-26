if __name__ == "__main__":
    """
    Entry Point 
    python -m ccmlutils
    """
    import sys

    from ccmlutils.framework.cli import cli

    if sys.argv[0].endswith("__main__.py"):
        sys.argv[0] = "python -m ccmlutils"
    cli()
