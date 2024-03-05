from src.hh_api import HH_API

hh = HH_API
assert 'response_letter_required' in hh.page
assert 'response_url' in hh.page
assert 'responsibility' in hh.page
assert 'accept_temporary' in hh.page
