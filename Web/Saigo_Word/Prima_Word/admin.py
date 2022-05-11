from django.contrib import admin

from .models import VM_Alph, VM_Word, Context_Table, Correct_Answers, GOS



admin.site.register(VM_Alph)
admin.site.register(VM_Word)
admin.site.register(GOS)

admin.site.register(Correct_Answers)
admin.site.register(Context_Table)
