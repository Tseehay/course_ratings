from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Notification

def notifications(request):
    user = request.user
    notifications = Notification.objects.filter(user=user).order_by('-created_at')
    return render(request, 'notifications/notifications.html', {'notifications': notifications})

def mark_notification_as_read(request, notification_id):
    notification = Notification.objects.get(pk=notification_id)
    notification.is_read = True
    notification.save()
    return redirect('notifications')