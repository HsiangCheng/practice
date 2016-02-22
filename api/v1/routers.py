# --coding: utf-8--

from rest_framework.routers import Route, DynamicDetailRoute, SimpleRouter

class  SingleRouter(SimpleRouter):
    routes = [
        # Detail route.
        Route(
            url=r'^{prefix}{trailing_slash}$',
            mapping={
                'get': 'retrieve',
                'post': 'create',
                'put': 'update',
                'patch': 'partial_update',
                'delete': 'destroy'
            },
            name='{basename}-detail',
            initkwargs={'suffix': 'Instance'}
        ),
        # Dynamically generated detail routes.
        # Generated using @detail_route decorator on methods of the viewset.
        DynamicDetailRoute(
            url=r'^{prefix}/{lookup}/{methodname}{trailing_slash}$',
            name='{basename}-{methodnamehyphen}',
            initkwargs={}
        ),
    ]
