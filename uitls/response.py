from rest_framework.renderers import JSONRenderer
from rest_framework import status


class BaseResponse:

    def __init__(self):
        self.code = 10000
        self.data = None
        self.message = None

    @property
    def dict(self):
        return self.__dict__


class MyJsonRenderer(JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        res = BaseResponse()
        response = renderer_context.get("response")
        status_code = response.status_code

        if status.is_success(status_code):
            res.data = data
        elif status.is_server_error(status_code):
            res.message = "服务器错误，请联系管理员"
        else:
            msg = data['detail'] if 'detail' in data else data
            if isinstance(msg, dict):
                '''
                主要是解析ValidationError 
                '''
                msg = msg.values()
                res.message = ",".join([",".join(each) for each in msg])
            else:
                res.message = data['detail'] if 'detail' in data else data
            res.code = 10001
        renderer_context.get("response").status_code = 200
        return super().render(res.dict, accepted_media_type=accepted_media_type, renderer_context=renderer_context)
