import os


bind = '{0}:{1}'.format(os.getenv('bind_ip'), os.getenv('bind_port'))
capture_output = True  # have gunicorn capture what the app is sending to stdout and stderr
