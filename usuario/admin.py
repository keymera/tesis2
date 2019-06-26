from django.contrib import admin
from usuario.models import Usuario
from usuario.models import Area
from usuario.models import Tipo
# Register your models here.


admin.site.register(Usuario)
admin.site.register(Area)
admin.site.register(Tipo)