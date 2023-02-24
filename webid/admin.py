from django.contrib import admin

from .models import Employee
from .models import ID
from .models import Forclaim
from .models import Idcode
from .models import DeptandDesignation
from .models import Idapplication

admin.site.register(Employee)
admin.site.register(ID)
admin.site.register(Forclaim)
admin.site.register(Idcode)
admin.site.register(DeptandDesignation)
admin.site.register(Idapplication)
# Register your models here.
