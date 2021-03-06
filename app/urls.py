from django.conf.urls import patterns, url
from app import views,pdf

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^approvement/$', views.approvement, name='approvement'),
    url(r'^login/$', views.login , name='login'),
    url(r'^logout/$', views.logout , name='logout'),
    url(r'^setup/$', views.setup , name='setup'),
    url(r'^list/$',views.list , name='list'),
    url(r'^create/(?P<formtype_id>\d+)/$', views.create_form, name='form'),
    url(r'^modify/(?P<form_id>\d+)/$', views.modify_form, name='modify'),
    url(r'^extend/(?P<form_id>\d+)/$', views.extend_form, name='extend'),
    url(r'^substitute/(?P<form_id>\d+)/$', views.substitute_form, name='copy'),
    url(r'^form/(?P<form_id>\d+)/approve/$', views.approve_form, name='approve'),
    url(r'^form/(?P<form_id>\d+)/approve/approved/$', views.approved, name='approved'),
    url(r'^form/(?P<form_id>\d+)/approve/reject/$', views.reject, name='reject'),
    url(r'^form/(?P<form_id>\d+)/$', views.form_show, name='show'),
    url(r'^file/(?P<file_id>\d+)/$', views.showfile, name='file'),
    url(r'^yearreport/$',views.reportByYear , name='reportByYear'),
    url(r'^yearreport/report$',views.reportByYearResult , name='reportByYearResult'),
    url(r'^userreport/$',views.reportByUsername , name='reportByUsername'),
    url(r'^userreport/report$',views.reportByUsernameResult , name='reportByUsernameResult'),
    url(r'^approvement/(?P<user_id>\d+)/approve/$', views.user_approve, name='user_approve'),

    ########################## PDF STUFF ###########################
    #url(r'^form/(?P<form_id>\d+)/$', views.manage_form, name='submit_form'),
    url(r'^form/(?P<form_id>\d+)/pdf/$', pdf.pdf_export, name='pdf'),
    # url(r'^pdf/$',views.pdf_export , name='pdf'),
    url(r'^form/(?P<form_id>\d+)/pdf1/$',pdf.pdf_hold , name='pdf1'),
    url(r'^form/(?P<form_id>\d+)/pdf2/$',pdf.pdf_register , name='pdf2'),
    url(r'^form/(?P<form_id>\d+)/pdf3/$',pdf.pdf_sample_produce , name='pdf3'),
    url(r'^form/(?P<form_id>\d+)/pdf4/$',pdf.pdf_sample_import , name='pdf4'),
    url(r'^form/(?P<form_id>\d+)/pdf5/$',pdf.pdf_produce , name='pdf5'),
    url(r'^form/(?P<form_id>\d+)/pdf6/$',pdf.pdf_import , name='pdf6'),

    url(r'^form/(?P<form_id>\d+)/pdf7/$',pdf.pdf_hold_extend , name='pdf7'),
    url(r'^form/(?P<form_id>\d+)/pdf8/$',pdf.pdf_import_extend , name='pdf8'),
    url(r'^form/(?P<form_id>\d+)/pdf9/$',pdf.pdf_export_extend , name='pdf9'),
    url(r'^form/(?P<form_id>\d+)/pdf10/$',pdf.pdf_produce_extend , name='pdf10'),
    url(r'^form/(?P<form_id>\d+)/pdf11/$',pdf.pdf_register_extend , name='pdf11'),

    url(r'^form/(?P<form_id>\d+)/pdf12/$',pdf.pdf_hold_modify , name='pdf12'),
    url(r'^form/(?P<form_id>\d+)/pdf13/$',pdf.pdf_produce_modify , name='pdf13'),
    url(r'^form/(?P<form_id>\d+)/pdf14/$',pdf.pdf_import_modify , name='pdf14'),
    url(r'^form/(?P<form_id>\d+)/pdf15/$',pdf.pdf_export_modify , name='pdf15'),
    url(r'^form/(?P<form_id>\d+)/pdf16/$',pdf.pdf_register_modify , name='pdf16'),

    url(r'^pdf17/$',pdf.pdf_exportEND , name='pdf17'),
    url(r'^pdf18/$',pdf.pdf_importEND , name='pdf18'),
    url(r'^pdf19/$',pdf.pdf_produceEND , name='pdf19'),
    url(r'^pdf20/$',pdf.pdf_holdEND , name='pdf20'),
    
    url(r'^form/(?P<form_id>\d+)/pdf21/$',pdf.pdf_register_sub , name='pdf21'),   

)