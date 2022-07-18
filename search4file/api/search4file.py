from search4file.core.SearchByContent import SearchByContent

sbc = SearchByContent()


def search_by_content(search_path, content):
    sbc.search_files(search_path, content)
