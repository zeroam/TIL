from django.http.response import HttpResponse
from django.views.generic.base import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import QueryDict

from .views_auth import logged_in_or_basicauth


class HomeView(TemplateView):
    template_name = 'home.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        print("HomeView.get()...")
        print(request.GET.get('language', 'RUBY'))
        print(request.GET.get('framework', 'RAILS'))
        print(request.GET.get('name', '홍길동'))
        print(request.GET.get('email', 'hong@gmail.com'))
        print(request.GET.get('url', 'http://google.co.kr'))
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print("HomeView.post()...")
        print(request.POST.get('language', 'RUBY'))
        print(request.POST.get('framework', 'RAILS'))
        print(request.POST.get('name', '홍길동'))
        print(request.POST.get('email', 'hong@gmail.com'))
        print(request.POST.get('url', 'http://google.co.kr'))
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        print("HomeView.put()...")
        put_params = QueryDict(request.body)
        print(put_params.get('language', 'RUBY'))
        print(put_params.get('framework', 'RAILS'))
        print(put_params.get('name', '홍길동'))
        print(put_params.get('email', 'hong@gmail.com'))
        print(put_params.get('url', 'http://google.co.kr'))
        return super().get(request, *args, **kwargs)


@logged_in_or_basicauth(realm='ksh')
def auth_view(request):
    print("auth_view()...")
    print(request.GET.get('language', 'JAVA'))
    return HttpResponse('This is Basic Auth Success Response.')


# def cookie_view(request):
#     print("cookie_view()...")
#     request.session.set_test_cookie()
#     return HttpResponse('This is set_test_cookie() Response.')


@csrf_exempt
def cookie_view_post(request):
    print("cookie_view_post()...")
    print("request.COOKIES:", request.COOKIES)

    if request.method == 'POST':
        if request.session.test_cookie_worked():
            print("Cookies:", request.session.items())
            request.session.delete_test_cookie()
            return HttpResponse("POST Request&Response... OK. Cookie received.")
        else:
            return HttpResponse("POST Request&Response... NOK. Please enable Cookie and try again.")
    request.session.set_test_cookie()

    # return HttpResponse('This is cookie_view_post RESPONSE')
    return HttpResponse('GET Request&Response... This is set_test_cookie() Response.')
