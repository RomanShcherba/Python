from plwrght_pages.base_page import BasePage

class SearchResultPage(BasePage):
    search_result = "//h1[contains(.,'«рюкзак» в Україні')]"


    def __init__(self, page):
        super().__init__(page)

    def is_search_result_displayed(self, timeout: int = 5000):
        self.page.wait_for_selector(self.search_result, timeout=timeout)
        return self.page.is_visible(self.search_result)