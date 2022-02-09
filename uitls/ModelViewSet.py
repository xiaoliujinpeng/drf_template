from rest_framework.viewsets import ModelViewSet as MV


class ModelViewSet(MV):
    def get_object(self):
        if "__" in self.lookup_field:
            queryset = self.filter_queryset(self.get_queryset())
            lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
            filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
            obj = queryset.filter(**filter_kwargs).first()
            self.check_object_permissions(self.request, obj)
            return obj
        else:
            return super().get_object()
