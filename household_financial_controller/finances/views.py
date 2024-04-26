from django.shortcuts import render


def dashboard_view(request):
    """
    :param request:
    :return: This function returns the login view.
    """
    return render(request, 'finances/dashboard.html')

