from rest_framework.exceptions import NotFound

class UrlParamMixin:
    param_name = None
    attr_name = None
    required = True
    cast = None  # opcional (ex: int, UUID)

    def dispatch(self, request, *args, **kwargs):
        if not self.param_name:
            raise NotFound()

        value = kwargs.get(self.param_name)

        if self.required and value is None:
            raise NotFound()

        if value is not None and self.cast:
            try:
                value = self.cast(value)
            except Exception:
                raise NotFound()

        setattr(self, self.attr_name or self.param_name, value)

        return super().dispatch(request, *args, **kwargs)