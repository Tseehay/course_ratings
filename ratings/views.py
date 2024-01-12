from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Course, Rating


@login_required
def rate_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    user = request.user

    if request.method == 'POST':
        score = int(request.POST.get('score'))
        review = request.POST.get('review')

        rating, created = Rating.objects.get_or_create(course=course, user=user)
        rating.score = score
        rating.review = review
        rating.save()

        return redirect('course_detail', course_id=course_id)

    return render(request, 'ratings/rate_course.html', {'course': course})


def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    ratings = course.ratings.all()
    return render(request, 'ratings/course_detail.html', {'course': course, 'ratings': ratings})