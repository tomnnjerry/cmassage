
from django.urls import path
from . import views
app_name='home'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # Services Dropdown Routes
    path('services/deep-tissue-mastery/', views.deep_tissue, name='deep_tissue'),
    path('services/purify-protocol-lymphatic/', views.lymphatic_protocol, name='lymphatic'),
    path('services/swedish-relaxation/', views.swedish_relaxation, name='swedish'),
    path('services/reflexology-stretching/', views.reflexology_stretching, name='reflexology'),
    path('services/cupping-treatments/', views.cupping_treatments, name='cupping'),
    path('services/prenatal-wellness/', views.prenatal_wellness, name='prenatal'),

    # Main Navigation Routes
    path('faq/', views.faq, name='faq'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('book-appointment/', views.book_appointment, name='book_appointment'),




    path('massage-with-cupping/', views.kinetic_protocol_view, name='kinetic_protocol'),
    
    # Integrated Modality 02: Massage + Stretching
    # URL: /protocols/massage-with-stretching/
    path('massage-with-stretching/', views.structural_protocol_view, name='structural_protocol'),



    # Legal & Compliance URLs
    path('terms/', views.terms_view, name='terms'),
    path('privacy-policy/', views.privacy_view, name='privacy'),
    path('refund-policy/', views.refund_view, name='refund'),
] 