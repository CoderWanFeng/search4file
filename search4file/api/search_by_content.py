import asyncio

from search4file.core.SearchByContent import SearchByContent
from search4file.core.SpecialFunc import SpecialExcel
from search4file.lib.utils.except_utils import except_dec

sbc = SearchByContent()

se = SpecialExcel()


# @except_dec()
def search_by_content(search_path, search_content):
    search_result_dict = asyncio.run(sbc.search_files(search_path, search_content))
    print(search_result_dict)
    return search_result_dict


# @except_dec()
def find_excel_data(search_key, target_dir):
    se.find_excel_data(search_key, target_dir)
