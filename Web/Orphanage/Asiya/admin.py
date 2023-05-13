from django.contrib import admin


from .models import Node_Base,Node_Link_Base, NGCL, NG_Base

admin.site.register(Node_Base)
admin.site.register(Node_Link_Base)
admin.site.register(NGCL)
admin.site.register(NG_Base)
