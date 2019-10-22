import socket

import geocoder

from django.apps import apps
from django.conf import settings
from django.http import HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin


class CountryGateAccess(MiddlewareMixin):
    WHITE_LIST = [item.lower() for item in settings.GATE_WHITELIST_COUNTRIES]

    def process_request(self, request):
        ip = self._visitor_ip_address(request)
        if not self._check_ip(ip):
            return HttpResponseForbidden()

        model = apps.get_model("gate.report")
        country, blocked = self._check_is_blacklisted(ip, CountryGateAccess.WHITE_LIST)
        if blocked:
            model.objects.create(ip=ip, origin=country or "")
            return HttpResponseForbidden()

    def _visitor_ip_address(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def _check_ip(self, ip):
        try:
            socket.inet_aton(ip)
            return True
        except socket.error:
            return False

    def _check_is_blacklisted(self, ip, whitelist):
        if not whitelist:
            return None, False

        # noinspection PyBroadException
        try:
            geo = geocoder.ip(ip)
        except Exception:
            if settings.GATE_STRICT_MODE:
                return None, True
            return None, False

        if geo.country is None:
            if settings.GATE_STRICT_MODE:
                return geo.country, True
            return geo.country, False

        return geo.country, (geo.country.lower() not in whitelist)
