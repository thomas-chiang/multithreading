# Question 1: Multithreading

## Problem Statement:
Write a Python program that simulates a producer-consumer scenario using multithreading. The producer thread should generate random integers and place them into a shared queue. The consumer thread should read integers from the queue and print them. Use a threading lock to ensure thread-safe access to the queue.


### Requirements:


* Use the threading module.
* Implement a shared queue with a maximum size of 10.
* The producer should produce a new integer every 0.1 seconds. 
* The consumer should consume an integer every 0.15 seconds. 
* The program should run for 10 seconds before terminating.

## Run
```
docker-compose up --build
```
and run below for cleanout
```
docker-compose down --rmi all
```
