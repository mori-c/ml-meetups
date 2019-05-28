# Goals

1. Individual app idea to follow along the series
2. Set up Firebase with Firestore
3. Choice of Framework (Angular, Vue, React)


## Idea

Create EEG Biosignal classifier with PyTorch/Tensorflow connected with Firebase

Classification feature ideas:

...

## Breakdown

| Process           | I / O | Method / Tools |
| ----------------- | ----- | -------------- |
| store/upload data | input | firestone      | clean eeg data | input | colab, numpy, pandas | graph, visualize data | output | colab, matplotlib | identify frequency channels | - | - | remove interfernce noise | input | firestone, csv | apply deep learning algorithms (FFT) | input | colab, algebra | display output of either image or wavelengths (tbd) | output | - | identify loss perhaps around less active channels by boosting (reinforce activity with auditory engagement, for example) | - | colab, generalization, loss, monte carlo / bayesian / regression |



## Firestone (database) → Firebase Setup

[Firestore Sub-Collections](https://howtofirebase.com/firestore-sub-collections-2e23c998540d)


## Framework

[Django](https://www.hackanons.com/2018/03/python-django-with-google-firebase.html)




---

## [Firebase Study Jam Series - Session 2](https://www.meetup.com/GDG-Toronto/events/261549807/)

> Monday, May 27, 2019

Our Firebase repo is also set up (https://github.com/gdg-toronto/firebase-study-jam-season-1). If anyone has not joined us, please let Solomon know. We will add you to the contributor list.

It is expected for everyone to have their own project ideas for this series. If you are determined and committed to be a part of the Firebase journey until the end, we are excited to have you!

Before next session, please make sure to have Firebase set up and make sure to choose Firestore for the database. Try and connect Firebase to the framework of your choice. We are primarily focusing on web related framework with Angular, React and Vue this time. However, if you have a framework you would like to use or if you are trying out through iOS or Android, please still feel free to be a part of us and share your experiences!

For more details on setup, Google’s Firebase guide will be a good place to get started (https://firebase.google.com/docs/guides/).

Location will be at Intersect.

In this series, we will take a journey into Firebase and what its capabilities are.

Throughout the series, we will be looking at the following topics:

- Firebase highlights and intro
- Setup/Read/Write
- Frameworks/Auth
- Fun with Frameworks

If you have always been interested in learning about Firebase or have an astonishing app idea that requires NoSQL database, this series will be a great fit for you!

Below is a quick glance of the schedule:

- 6:00pm - Doors Open
- 6:30pm - 8:00pm - Firechat by the Fire at a Firecamp about Firebase
- topics:
- discussion about how everybody's experiences have been so far setting up Firebase and exploring the Firestore capabilities
- opportunity for people to talk about their projects or show code samples
- opportunity for people to get help with anything they may be stuck on
- if there is not much discussion to be had, some time for people to work on their projects
- 8:00pm - 8:30pm - Wrap up and setting targets for session 3 (authentication)

Look forward to see everyone!

GDG Toronto

---

## Resources

[Angular](https://angular.io/)
[Firebase Documentation](https://firebase.google.com/docs/guides/)
[Tensorflow](https://www.tensorflow.org/tutorials/)