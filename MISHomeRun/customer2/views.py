#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.views import generic
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from machina.core.db.models import get_model
from machina.conf import settings as machina_settings

from customer2.models import RealNote, FakeNote
from main.models import User
from betting.models import Betting
from customer2.forms import RealNoteForm, PurchaseForm
from customer2.models import PurchaseRecord, SystemGiveRecord
from main.mixins import PageTitleMixin

Forum = get_model('forum', 'Forum')
ForumProfile = get_model('forum_member', 'ForumProfile')
Post = get_model('forum_conversation', 'Post')
Topic = get_model('forum_conversation', 'Topic')

class ProfileView(PageTitleMixin, generic.TemplateView):
    template_name = 'customer2/profile.html'
    page_title = '個人資料'
    active_tab = 'profile'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProfileView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(ProfileView, self).get_context_data(**kwargs)
        ctx['user'] = User.objects.get(username=kwargs.get('username'))
        profile, dummy = ForumProfile.objects.get_or_create(user=ctx['user'])
        ctx['profile'] = profile
        return ctx

class RealNoteView(PageTitleMixin, FormView):
    template_name = 'customer2/real.html'
    page_title = '真實投注筆記'
    active_tab = 'real'
    form_class = RealNoteForm

    def get_success_url(self):
        return reverse_lazy('customer2:real', 
                            kwargs={'username': self.request.user.username, })

    def form_valid(self, form):
        betting =  Betting.objects.get(id=self.request.POST.get('betting'))
        if not RealNote.objects.filter(user=self.request.user, betting=betting):
            messages.success(self.request, "成功新增了一筆筆記")
            
            realNote = form.save(commit=False)
            realNote.user = self.request.user
            realNote.betting = betting
            realNote.save()

        else:
            messages.warning(self.request, "您已新增過此賽事投注筆記")
        return super(RealNoteView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(RealNoteView, self).get_context_data(**kwargs)
        ctx['notes'] = RealNote.objects.filter(user=self.request.user)
        return ctx

class RealNoteUpdateView(PageTitleMixin, UpdateView):
    model = RealNote
    template_name = 'customer2/realu.html'
    page_title = '編輯真實筆記'
    fields = [
            'lp_home_team', 
            'lp_away_team', 
            'nlp_home_team', 
            'nlp_away_team',
            'big',
            'small',
        ]

    def get_success_url(self):
        return reverse_lazy('customer2:real', 
                            kwargs={'username': self.request.user.username, })

    def form_valid(self, form):
        messages.success(self.request, "編輯成功")
        return super(RealNoteUpdateView, self).form_valid(form)

class RealNoteDeleteView(PageTitleMixin, DeleteView):
    model = RealNote
    template_name = 'customer2/reald.html'
    page_title = '刪除真實筆記'

    def get_success_url(self):
        return reverse_lazy('customer2:real', 
                            kwargs={'username': self.request.user.username, })
    
    def form_valid(self, form):
        messages.success(self.request, "刪除成功")
        return super(RealNoteUpdateView, self).form_valid(form)
        

class FakeNoteView(PageTitleMixin, generic.TemplateView):
    template_name = 'customer2/fake.html'
    page_title = '虛擬投注記錄'
    active_tab = 'fake'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FakeNoteView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(FakeNoteView, self).get_context_data(**kwargs)
        username = kwargs.get('username')
        ctx['user'] = User.objects.get(username=username)
        ctx['notes'] = FakeNote.objects.filter(
            user= ctx['user']).order_by('-betting__game__date')
        
        return ctx  

class PurchaseView(FormView):
    form_class = PurchaseForm

    def form_valid(self, form):
        buy_for = self.request.POST.get('buy_for')
        buy_note = int(self.request.POST.get('buy_note'))

        #FIXME: cost 之後別用form帶，直接用user的level在view裡計算
        cost = int(self.request.POST.get('cost'))

        note = FakeNote.objects.get(id=buy_note)
        self.username = note.user.username 

        if buy_for not in ['lp', 'nlp', 'bs', 'wdp',]:
            return self.form_invalid(form)

        if not PurchaseRecord.objects.filter(
            buyer=self.request.user, 
            buy_note=note,
            buy_for=buy_for):

            coin = self.request.user.coin
            if coin - cost >= 0:
                pr = PurchaseRecord(
                    buyer=self.request.user,
                    buy_note=note,
                    buy_for=buy_for,
                    cost=cost,
                )
                self.request.user.coin = coin - cost
                self.request.user.save()
                pr.save()
                note.user.coin = note.user.coin + cost
                note.user.save()
                messages.success(self.request, "成功購買了一筆虛擬投注記錄項目，花費%d枚金幣，剩餘%d枚金幣" % (cost, self.request.user.coin))
            else:
                messages.warning(self.request, "金幣不足，您只剩下%d枚金幣" % coin)
        else:
            messages.warning(self.request, "您已購買過此筆記錄項目")
        return super(PurchaseView, self).form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, "不成功")
        return super(PurchaseView, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('customer2:fake', args=(self.username,))

class CoinView(PageTitleMixin, generic.TemplateView):
    template_name = 'customer2/coin.html'
    page_title = '金幣花費資訊'
    active_tab = 'coin'

    def get_context_data(self, **kwargs):
        ctx = super(CoinView, self).get_context_data(**kwargs)
        username = kwargs.get('username')
        ctx['user'] = User.objects.get(username=username)

        # 投注支出
        ctx['fakenote'] = FakeNote.objects.filter(user=ctx['user']).order_by('-create_date')

        # 購買支出
        ctx['purchase'] = PurchaseRecord.objects.filter(buyer=ctx['user']).order_by('-create_date')

        # 收入
        ctx['income'] = PurchaseRecord.objects.filter(buy_note__user=ctx['user']).order_by('-create_date')

        # 系統發放
        ctx['system'] = SystemGiveRecord.objects.filter(receiver=ctx['user']).order_by('-create_date')
        
        return ctx  

class ForumView(PageTitleMixin, generic.TemplateView):
    template_name = 'customer2/forum.html'
    page_title = '發表文章'
    active_tab = 'forum'

    def get_context_data(self, **kwargs):
        ctx = super(ForumView, self).get_context_data(**kwargs)
        ctx['user'] = User.objects.get(username=kwargs.get('username'))
        profile, dummy = ForumProfile.objects.get_or_create(user=ctx['user'])
        ctx['profile'] = profile

        ctx['topics_count'] = Topic.objects.filter(
            approved=True, poster=profile.user).count()
        # Fetches the recent posts added by the considered user
        forums = self.request.forum_permission_handler.forum_list_filter(
            Forum.objects.all(), self.request.user)
        recent_posts = Post.approved_objects.filter(
            topic__forum__in=forums, poster=profile.user).order_by('-created')
        ctx['recent_posts'] = recent_posts[:machina_settings.PROFILE_RECENT_POSTS_NUMBER]

        return ctx
