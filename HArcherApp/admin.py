from django.contrib import admin
from .models import Training

# admin.site.register(Training)


@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    exclude = ['title']
    list_display = ['title', 'date', 'horse','result_general', 'result_front',  'result_side', 'result_back']
    list_filter = ['title', 'horse']
    search_fields = ['horse', 'description']

