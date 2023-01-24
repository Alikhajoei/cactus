# this file contains all the functions that i need them in my views and i write them myself
# sasha + utility => sutility
from doctest import TestResults


def get_client_ip(user_info):

	x_forwarded_for = user_info.META.get('HTTP_X_RORWARDED_FOR')

	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = user_info.META.get('REMOTE_ADDR')

	return ip


