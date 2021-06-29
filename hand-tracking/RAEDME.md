# Chapter 1 - Hand tracking

# Objectives

In this chapter I will be learning how to use computer vision to carry out hand tracking using python.

I will:

- Write code to learn how to carry out hand tracking.
- Learn how to convert it into a module so we don't have to rewrite the code over and over again.

# Frameworks in use

- Media pipe - created by google that allows us to get started with some of the most fundamental AI problems, such as facial detection, facial landmarks, hand tracking etc.

- I will be using the <strong> hand tracking module </strong> which uses the palm detection module and landmarks modules.

- The hand tracking module, uses a full image and creates a cropped image of the palm,

- From there the hand landmark module will find 21 different landmarks which then generates about 21 different landmarks/points on the palm. This module was manually trained to recognise the 21 different points of a palm from 30,000 images.
