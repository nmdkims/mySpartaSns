from django.shortcuts import render, redirect
from .models import TweetModel
from .models import TweetComment
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/tweet')
    else:
        return redirect('/sign-in')


@login_required
def tweet(request):
    if request.method == 'GET':  # 요청하는 방식이 GET 방식인지 확인하기
        all_tweet = TweetModel.objects.all().order_by('-created_at')
        return render(request, 'tweet/home.html', {'tweet': all_tweet})
    elif request.method == 'POST':  # 요청 방식이 POST 일때
        user = request.user  # 현재 로그인 한 사용자를 불러오기
        content = request.POST.get('my-content', '')  # 글 작성이 되지 않았다면 빈칸으로

        if content == '':  # 글이 빈칸이면 기존 tweet과 에러를 같이 출력
            all_tweet = TweetModel.objects.all().order_by('-created_at')
            return render(request, 'tweet/home.html', {'error': '글은 공백일 수 없습니다', 'tweet': all_tweet})
        else:
            my_tweet = TweetModel.objects.create(author=user, content=content)  # 글 저장을 한번에!
            my_tweet.save()
            return redirect('/tweet')


@login_required
def delete_tweet(request, id):
    my_tweet = TweetModel.objects.get(id=id)
    my_tweet.delete()
    return redirect('/tweet')


@login_required
def detail_tweet(request, id):
    my_tweet = TweetModel.objects.get(id=id)
    tweet_comment = TweetComment.objects.filter(tweet_id=id).order_by('-created_at')
    return render(request, 'tweet/tweet_detail.html', {'tweet': my_tweet, 'comment': tweet_comment})


@login_required
def write_comment(request, id):
    if request.method == 'POST':
        comment = request.POST.get("comment", "")
        current_tweet = TweetModel.objects.get(id=id)

        TC = TweetComment()
        TC.comment = comment
        TC.author = request.user
        TC.tweet = current_tweet
        TC.save()

        return redirect('/tweet/' + str(id))


@login_required
def delete_comment(request, id):
    comment = TweetComment.objects.get(id=id)
    current_tweet = comment.tweet.id
    comment.delete()
    return redirect('/tweet/' + str(current_tweet))
