from django.conf.urls import url
from django.conf.urls import patterns
from django.views.generic import TemplateView


view = TemplateView.as_view(template_name='dummy.html')

urlpatterns = patterns('',
    url(r'^nl/foo/', view, name='not-translated'),
)
