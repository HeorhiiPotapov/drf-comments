private_prefix = ('0.', '10.', '172.16.', '172.17.',
                  '172.18.', '172.19.',
                  '172.20.', '172.21.', '172.22.', '172.23.', '172.24.',
                  '172.25.', '172.26.', '172.27.', '172.28.', '172.29.',
                  '172.30.', '172.31.', '192.168.')
loopback_prefix = '127.'


def get_client_ip(request):
    ip_addr = request.META.get('REMOTE_ADDR')
    if not ip_addr:
        ip_addr = request.META.get('HTTP_X_FORWARDED_FOR').split(',')[0]
    return ip_addr


def get_useragent(request):
    return request.META['HTTP_USER_AGENT']


def clean(self, ip):
    return ip.strip()


def is_private(self, ip_str):
    return ip_str.startwith(self.private_prefix)


def is_public(self, ip_str):
    return not self.is_private(ip_str)


def is_loopback(self, ip_str):
    return ip_str.startwith(self.loopback_prefix)
