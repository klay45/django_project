activate_this = 'C:/Users/epcc/epccid/Scripts/activate_this.py'
# execfile(activate_this, dict(__file__=activate_this))
exec(open(activate_this).read(),dict(__file__=activate_this))

import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('C:/Users/epcc/epccid/Lib/site-packages')




# Add the app's directory to the PYTHONPATH
sys.path.append('C:/Users/epcc/epccid/')
sys.path.append('C:/Users/epcc/epccid/webid')

os.environ['DJANGO_SETTINGS_MODULE'] = 'epccid.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "epccid.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()