from .models import Get_Ip_Address

class IpSaveMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        try:
            ip_address = Get_Ip_Address.objects.get(put_ip_user=ip)
        except Get_Ip_Address.DoesNotExist:
            ip_address = Get_Ip_Address(put_ip_user=ip)
            ip_address.save()
            request.user.ip_address = ip_address

        response = self.get_response(request)
        return response