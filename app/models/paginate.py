#!/usr/bin/env python


class Paginate():
    def __init__(self, PAGES_NUMBER_PER_PAGE, pages):
        "global pages"
        count=0
        self.list_page1 = []
        for page in pages:
            if count % PAGES_NUMBER_PER_PAGE == 0 :
                self.list_page1.append([])
            self.list_page1[int(count /PAGES_NUMBER_PER_PAGE )].append(page)
            count +=1

    def get_total_number(self):
        return len(self.list_page1)

    def get_number_pages(self, num):
        if num < 0 or num >= len(self.list_page1):
            return []
        return self.list_page1[num]
