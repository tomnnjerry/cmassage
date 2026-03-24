from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    context = {

    }
    return render(request, 'index.html', context)


def about(request):
    context = {

    }
    return render(request, 'about.html', context)


# --- Service Pages ---

def deep_tissue(request):
    return render(request, 'services/deep_tissue.html')

def lymphatic_protocol(request):
    return render(request, 'services/lymphatic.html')

def swedish_relaxation(request):
    return render(request, 'services/swedish.html')

def reflexology_stretching(request):
    return render(request, 'services/reflexology.html')

def cupping_treatments(request):
    return render(request, 'services/cupping.html')

def prenatal_wellness(request):
    return render(request, 'services/prenatal.html')

def kinetic_protocol_view(request):
    """Integrated View: Massage + Cupping"""
    context = {
        'protocol_name': 'The Kinetic Protocol',
        'service_slug': 'massage-with-cupping',
        'clinical_focus': 'Decompression & Myofascial Release',
        'intensity': 'LVL 04',
        'duration': '60/90/120 Min',
        'meta_description': 'A clinical integration of deep tissue massage and medical-grade cupping therapy in Bay Harbor.'
    }
    return render(request, 'services/kinetic.html', context)

def structural_protocol_view(request):
    """Integrated View: Massage + Stretching"""
    context = {
        'protocol_name': 'The Structural Protocol',
        'service_slug': 'massage-with-stretching',
        'clinical_focus': 'Biomechanical Reset & ROM Enhancement',
        'intensity': 'LVL 03',
        'duration': '45/75/105 Min',
        'meta_description': 'Advanced assisted stretching combined with targeted massage to restore joint mobility.'
    }
    return render(request, 'services/structural.html', context)

# --- Main Nav Pages ---

def faq(request):
    return render(request, 'faq.html')

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    return render(request, 'contact.html')

def book_appointment(request):
    return render(request, 'booking.html')
    
def terms_view(request):
    """Renders the Terms and Conditions page"""
    return render(request, 'terms.html')

def privacy_view(request):
    """Renders the Privacy Policy page"""
    return render(request, 'privacy.html')

def refund_view(request):
    """Renders the Refund & Cancellation Policy page"""
    return render(request, 'refund.html')