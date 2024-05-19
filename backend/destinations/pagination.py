from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response(
            {
                "currentPage": self.page.number,
                "totalPages": self.page.paginator.num_pages,
                "count": self.page.paginator.count,
                "results": data,
            }
        )
