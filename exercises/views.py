# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.db.models import Count, F
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.contrib.auth import logout

import datetime
from itertools import chain

from exercises.models import Discipline, Exercise, ExoResult, ExoResultDetail
from django.contrib.auth.models import User

from exercises.obj_into_dic import obj_into_dic


@login_required
def ExerciseIndex(request):
    if request.user.is_staff:
        return redirect('/exercises/results')
    else:
        qr = Exercise.objects.filter(is_published=True)
        qr_dict = obj_into_dic(qr, 'discipline', 'exo_number')
        qr_results = []
        for disc, val in qr_dict.items():  # get the score for each exercise for the request.user
            for exo, val2 in val.items():
                qs = ExoResult.objects.filter(user=request.user.id,
                                              exo_number=exo,
                                              discipline_id=disc)
                if not qs:
                    qs = [None]
                val2.extend(qs)

        #import pdb; pdb.set_trace()
        return render(request, 'exercises/exercise_index.html', {'exercise_list': qr_dict})


@staff_member_required
def ExerciseResult(request):
    qr = Exercise.objects.all()
    qr_dict = obj_into_dic(qr, 'discipline', 'exo_number')
    #import pdb; pdb.set_trace()
    return render(request, 'exercises/exercise_result.html', {'exercise_list': qr_dict})


@staff_member_required
def ExerciseResultChoice(request):
    qs = []
    index_qs = 0
    user_list = User.objects.exclude(is_staff=True).values_list('username', flat=True)
    exo_choosen = []
    for user in user_list:
        qs.append([])
        for key in request.POST:
            if key == 'csrfmiddlewaretoken':
                continue
            for item in request.POST.getlist(key):  # each key is an exercise
                discipline, exo_number = item.split('/')
                if user == user_list[0]:
                    exo_choosen.append([discipline, exo_number])
                qr = ExoResult.objects.filter(discipline__name=discipline, exo_number=exo_number, user__username=user)
                if qr:
                    qr = [qr[0].result_to_letter()]
                else:
                    qr = ['None']
                qs[index_qs].extend(qr)
        index_qs += 1
    user_zip = zip(user_list, qs)
    #import pdb; pdb.set_trace()
    return render(request, 'exercises/result_choice.html', {'user_zip': user_zip, 'exo_choosen': exo_choosen})

@login_required
def ExerciseForm(request, discipline, exo_number):
    exo_list = Exercise.objects.filter(discipline__name=discipline, exo_number=exo_number, is_published=True)
    truth_mask = [True for x in range(len(exo_list))]
    new = True
    if request.method == 'POST':
        #import pdb; pdb.set_trace()
        forloop_nb = 1  # used for the forloop
        for exo in exo_list:
            posted_id = request.POST.get('user_answer_id'+str(forloop_nb))
            if posted_id:
                new = False  # it is being tried
                posted_answer = request.POST.getlist('user_answer_text'+str(forloop_nb))
                posted_answer = ''.join(posted_answer)
                currentexo = Exercise.objects.get(id=posted_id)
                if currentexo.answer == posted_answer:
                    truth_mask[forloop_nb-1] = True
                else:
                    truth_mask[forloop_nb-1] = False

                # put the user answer inside table exercises_exoresultdetail :
                d1, created = ExoResultDetail.objects.get_or_create(exo_number=exo_number,
                                                                    discipline_id=currentexo.discipline_id,
                                                                    user_id=request.user.id,
                                                                    exo_number_detail=forloop_nb,
                                                                    truth=truth_mask[forloop_nb-1])
                if not created:
                    d1.try_number = F('try_number') + 1
                    d1.truth = truth_mask[forloop_nb-1]
                # in all cases, update result and date
                d1.result_date = datetime.datetime.now()
                d1.save()
            forloop_nb += 1
        # calculate the score :
        score = round((sum(truth_mask)*100)/len(truth_mask))
        # put the user answer inside table exercises_exoresult :
        p1, created = ExoResult.objects.get_or_create(exo_number=exo_number,
                                                    discipline_id=currentexo.discipline_id,
                                                    user_id=request.user.id)
        if not created:
            p1.try_number = F('try_number') + 1
        # in all cases, update result and date
        p1.result = score
        p1.result_date = datetime.datetime.now()
        p1.save()

    # get the truth for the exercise
    k = 1
    for x in truth_mask:
        try:
            t1 = ExoResultDetail.objects.get(discipline__name=discipline,
                                             exo_number=exo_number,
                                             exo_number_detail=k,
                                             user_id=request.user.id)
            truth_mask[k-1] = t1.truth
            new = False  # it was already tried before (but on another session)
            #import pdb; pdb.set_trace()
        except:
            pass
        k += 1

    score = round((sum(truth_mask)*100)/len(truth_mask))
    if score < 50:    # translate score in number to letters
        score = 'C'
    elif score < 75:
        score = 'B'
    else:
        score = 'A'
    if score == 100:
        perfect = True
    else:
        perfect = False
    # export to the template
    truth = list(zip(exo_list, truth_mask))
    context = {'exo_list': exo_list, 'discipline': discipline, 'truth': truth, 'new': new, 'score': score, 'perfect': perfect}
    return render(request, 'exercises/exercise_form.html', context)


def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('/')



