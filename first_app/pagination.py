from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class ProductPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'p'
    page_size_query_param = 'size'
    max_page_size = 3


class ProductLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    limit_query_param = 'l'
    offset_query_param = 'of'


class ProductCursorPagination(CursorPagination):
    page_size = 3
    ordering = 'id'
