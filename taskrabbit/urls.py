from django.conf.urls import patterns, url

from taskrabbit import views

urlpatterns = patterns('',
    # universal patterns
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.show_login, name='login'),
    url(r'^my_tasks/$', views.my_tasks, name='my_tasks'),
    url(r'^logout/$', views.log_out, name='log_out'),
    url(r'^search/$', views.search, name='search'),
    url(r'^active/$', views.all_tasks, name='all_tasks'),
    url(r'^active/(?P<page>\d+)/$', views.all_tasks, name='all_tasks'),

    # sort by teams page
    url(r'^team/$', views.teams, name='teams'),
    url(r'^team/(?P<team_id>[0-9]+)/$', views.teams, name='teams'),

    url(r'^status/$', views.statuses, name='statuses'),
    url(r'^status/(?P<status_id>[0-9]+)/$', views.statuses, name='statuses'),
    url(r'^status/(?P<status_id>[0-9]+)/(?P<page>[0-9]+)/$', views.statuses, name='statuses'),

    url(r'^claim/$', views.claim_task, name='claim_task'),


    url(r'^task/$', views.view_task, name='view_task'),
    url(r'^task/(?P<task_id>[0-9]+)/$', views.view_task, name='view_task'),
    url(r'^task/(?P<task_id>[0-9]+)/edit/$', views.edit_task, name='edit_task'),

    # user profile
    url(r'^user/(?P<user_id>[0-9]+)/$', views.user_profile, name='user_profile'),
    url(r'^user/(?P<user_id>[0-9]+)/status/(?P<status_id>[0-9]+)/$', views.user_status, name='user_status'),
    url(r'^user/(?P<user_id>[0-9]+)/email/$', views.email_user, name='email_user'),
    url(r'^user/(?P<user_id>[0-9]+)/text/$', views.text_user, name='text_user'),

    # time clock
    url(r'^in/$', views.clock_in_view, name='clock_in_view'),
    url(r'^out/$', views.clock_out_view, name='clock_out_view'),
    url(r'^times/$', views.time_history, name='time_history_page'),
    url(r'^times/(?P<page>\d+)/$', views.time_history,  name='time_history_page'),
    # hacky check-out-from-history thing
    url(r'^times/out/$', views.clock_out_view, name='clock_out_from_history'),

    # get things as json
    url(r'^json/statuses/$', views.get_statuses, name='get_statuses_as_json'),
    url(r'^json/users/$', views.get_users, name='get_users_as_json'),
    url(r'^json/carriers/$', views.get_carriers, name='get_carriers_as_json'),
    url(r'^json/themes/$', views.get_themes, name='get_themes_as_json'),


    # updates db objects
    url(r'^update/task/inline/$', views.update_task_inline, name='update_task_inline'),
    url(r'^update/task/form/$', views.update_task_form, name='update_task_form'),

    # add things
    url(r'^add/task/$', views.add_task, name='add_task'),
    url(r'^add/note/$', views.add_note, name='add_note'),

    # send things to user
    url(r'send/email/$', views.email_task_owner, name='email_task_owner'),
    url(r'send/text/$', views.send_text_to_owner, name='text_task_owner'),

    # user preferences
    url(r'profile/$', views.update_user_profile, name='update_user_profile'),
    url(r'profile/password/$', views.update_user_password, name='update_user_password'),

    # account things
    url(r'create/(?P<creation_id>\w+)/$', views.create_account, name='create_account'),

    url(r'forgot/$', views.forgot_password, name='forgot_password'),
    url(r'forgot/(?P<password_id>\w+)/$', views.forgot_password, name='forgot_password')

)


