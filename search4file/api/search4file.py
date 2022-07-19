from search4file.core.SearchByContent import SearchByContent
from search4file.lib.decorator.except_dec import except_dec

sbc = SearchByContent()


# @except_dec()
def search_by_content(search_path, content):
    search_result_dict = sbc.search_files(search_path, content)
    print(search_result_dict)
    return search_result_dict
