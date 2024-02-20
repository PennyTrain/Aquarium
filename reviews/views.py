from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import ReviewPost
from django.views.generic import DeleteView
from .forms import EditPost, CreatePost
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# View for running reviews
def ReviewPostDisplay(request):
    template_name = "reviews/reviews.html"
    reviews_all = ReviewPost.objects.all()
    context = {
        'reviews_all': reviews_all
    }
    return render(request, template_name, context)


def ReviewDetail(request, slug):
    review = get_object_or_404(ReviewPost, slug=slug)
    template_name = "reviews/reviews_details.html"
    context = {
        'review': review 
    }
    return render(request, template_name, context)


@login_required 
def CreateReview(request):
    """
    A view to create the reviews
    """
    form = CreatePost()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = CreatePost(request.POST, request.FILES)
        if form.is_valid():
            new_review = form.save(commit=False)
            print(request.user)
            # print(new_review)
            # print(new_review.author)
            new_review.author = request.user 
            print(new_review)
            new_review.save()
            # message here
            return redirect(reverse('reviews:ReviewPostDisplay'))
        else:
            # message is review fails to post
            return
    template_name = "reviews/create_review.html"
    return render(request, template_name, context)


@login_required
def UpdateReview(request, slug):
    """
    update
    """
    review = get_object_or_404(ReviewPost, slug=slug)
    review_form = EditPost(instance=review)
    if request.method == 'POST':
        review_form = EditPost(request.POST,
                             request.FILES,
                             instance=review)
        if review_form.is_valid():
            try:
                review_form.save()
                return redirect('reviews:ReviewPostDisplay')
            except:
                context = {
                    'form': review_form
                }
                return render(request,
                              'reviews/update_review.html', context)

    context = {
        'form': review_form
    }

    return render(request, 'reviews/update_review.html', context)





# class DeleteReview(DeleteView): 
#     model = ReviewPost
#     template_name = "reviews/delete_review.html"
#     success_url = reverse_lazy('reviews:ReviewPostDisplay')

class DeleteReview(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Class base view of deleting an original post
    """
    model = ReviewPost
    success_message = "Post Deleted"
    success_url = '/reviews/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    


    
