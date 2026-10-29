# Change the URL segment for pages in MkDocs to hide the "/pages" prefix, so that pages inside the
# "pages" directory are served directly at the root URL.
# This runs on all files before any page is rendered, so that links between pages resolve to the
# new URLs regardless of the order in which pages are built.
def on_files(files, *, config):
    for file in files:
        if file.url.startswith("pages/"):
            # Remove "pages/" prefix from the URL
            file.url = file.url.removeprefix("pages/")
            file.dest_uri = file.dest_uri.removeprefix("pages/")
            file.abs_dest_path = file.abs_dest_path.replace("/pages/", "/", 1)
    return files
