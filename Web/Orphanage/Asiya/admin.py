from django.contrib import admin

from .models import Person_Memory,Ego
from .models import RelationType,Character_Tags,Emote_Reg
from .models import VM_Word, GOW, Sentence_Memory, Context_Table
from .models import Semantic_Memory, Constant_Expression
from .models import Episode_Memory,EM_Type
from .models import Identity,Motives,Postulates,Like_Dislike



admin.site.register(Person_Memory)
admin.site.register(Ego)

admin.site.register(RelationType)
admin.site.register(Character_Tags)

admin.site.register(Emote_Reg)

admin.site.register(VM_Word)
admin.site.register(GOW)

admin.site.register(Sentence_Memory)
admin.site.register(Context_Table)

admin.site.register(Semantic_Memory)
admin.site.register(Constant_Expression)

admin.site.register(Episode_Memory)
admin.site.register(EM_Type)

admin.site.register(Identity)
admin.site.register(Motives)
admin.site.register(Postulates)
admin.site.register(Like_Dislike)
