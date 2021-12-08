'''User admin classes'''

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Models
from users.models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    '''Profile admin.'''

    # List of thing that is going to show on the admin app
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    # List of thing that are going to have a hiperlink
    list_display_links = ('pk', 'user')
    # list of things that are going to be editable from the admin page
    list_editable = ('phone_number', 'website','picture')
    # List of fields the search its going to look
    search_fields = ('user__username',
                     'user__email',
                     'user__first_name',
                     'user__last_name',
                     'phone_number')
    # filter on admin page
    list_filter = ('created',
                   'modified',
                   'user__is_active',
                   'user__is_staff')

    # To personalize the content inside a profile
    fieldsets = (
        ('Profile', {
            'fields': (
                ('user', 'picture'),),
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            )
        }),
        ('Metadata', {
            'fields': (('created', 'modified'),),
        })
    )

    # fields that can not be modified. In the case on naturally not modificates fields
    # 'created' we have to put it in here if we want to put it on the
    # fieldset (up)
    readonly_fields = ('created', 'modified')



# To create profile fields next to user admin page
class ProfileInline(admin.StackedInline):
    '''Profile in-line admin for users.'''

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    '''Add profile admin to base user admin'''

    inlines = (ProfileInline, )
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)





