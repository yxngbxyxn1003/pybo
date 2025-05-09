from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']  # ✅ 검색 대상 필드 지정

admin.site.register(Question, QuestionAdmin)
