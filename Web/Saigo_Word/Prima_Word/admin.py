from django.contrib import admin

from .models import VM_Alph, VM_Word, Context_Table, Sentence_Memory, GOW



admin.site.register(VM_Alph)
admin.site.register(VM_Word)
admin.site.register(GOW)

admin.site.register(Sentence_Memory)
admin.site.register(Context_Table)
