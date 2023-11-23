from __future__ import annotations

from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.schemas.openapi import AutoSchema
from rest_framework.viewsets import GenericViewSet


class ParameterSchema(AutoSchema):
    def __init__(self, **kwargs):
        self.parameters = kwargs.pop('parameters')
        super().__init__(**kwargs)

    def get_operation(self, path, method):
        op = super().get_operation(path, method)
        method_name = getattr(self.view, 'action', method.lower())
        action_parameters = self.parameters.get(method_name, [])
        for param in action_parameters:
            op['parameters'].append(param)
        return op


class CreateViewSet(mixins.CreateModelMixin, GenericViewSet):
    pass


class ListCreateViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, GenericViewSet):
    pass


class ListViewSet(mixins.ListModelMixin, GenericViewSet):
    pass


class FetchUpdateViewSets(viewsets.ReadOnlyModelViewSet, mixins.UpdateModelMixin, GenericViewSet):
    http_method_names = [
        'get', 'post', 'put',
        'delete', 'head', 'options', 'trace',
    ]


class DeleteViewSets(mixins.DestroyModelMixin, GenericViewSet):
    pass
