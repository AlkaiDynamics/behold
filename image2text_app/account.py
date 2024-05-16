# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib import messages

from .models import GeneratedText


@login_required
def account(request):
    try:
        # Fetch all texts related to the logged-in user's images
        texts_query = GeneratedText.objects.filter(image__user=request.user)
        
        # Implement pagination to handle large datasets
        paginator = Paginator(texts_query, 10)  # Show 10 texts per page
        page_number = request.GET.get('page')
        texts = paginator.get_page(page_number)

    except GeneratedText.DoesNotExist:
        messages.error(request, "No texts found.")
        return redirect('home')

    except Exception as e:
        messages.error(request, f"Error retrieving user texts: {str(e)}")
        return redirect('home')

    context = {
        'texts': texts
    }

    return render(request, 'account.html', context)
