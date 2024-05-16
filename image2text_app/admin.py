from django.contrib import admin
from .models import Image, Style, ImageAnalysis

class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'uploaded_at', 'user')
    list_filter = ('uploaded_at', 'user')
    search_fields = ('description',)

class StyleAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'tone')
    list_filter = ('type',)
    search_fields = ('type', 'tone')

class ImageAnalysisAdmin(admin.ModelAdmin):
    list_display = ('id', 'analyzed_at', 'image')
    list_filter = ('analyzed_at',)
    search_fields = ('image__description',)

admin.site.register(Image, ImageAdmin)
admin.site.register(Style, StyleAdmin)
admin.site.register(ImageAnalysis, ImageAnalysisAdmin)

