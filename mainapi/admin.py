from django.contrib import admin
from .models import Recipe, Category, SFC, Users
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin

@admin.register(Recipe)
class recipes(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True
    pass

@admin.register(Category)
class categories(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True
    pass

@admin.register(SFC)
class calories(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True
    pass

@admin.register(Users)
class user(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True
    pass