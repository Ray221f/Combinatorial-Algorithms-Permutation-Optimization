# Combinatorial Algorithms (Spring 2025)
## Assignment 2 (v1.4)

**Authors:**  
- Hao Guo
- Zirui Fang

**Date:** June 2025  
**Course:** Combinatorial Algorithms  
**Instructor:** Prof. Pablo Ezequiel Terlisky
---

## 📘 Overview

This repository contains our solutions for **Assignment 2 (v1.4)** of the *Combinatorial Algorithms* course.  
The assignment includes **two main problems** involving **shortest path algorithms** and **vertex cover problems**.  
Each problem has **two parts**, leading to four Python implementations in total.

| Exercise | File | Description |
|-----------|------|-------------|
| 1(a) | `assignment_1_1.py` | Shortest *walk* from `s` to `t` using **exactly one special edge** |
| 1(b) | `assignment_1_2.py` | Shortest *path* from `s` to `t` using **at most two special edges** |
| 2(a) | `assignment_2_1.py` | **Exact** minimum vertex cover using **backtracking + pruning** |
| 2(b) | `assignment_2_2.py` | **2-approximation** vertex cover using a **greedy linear algorithm** |

All programs read from **standard input**, print to **standard output**, and are fully self-contained in Python 3.

---

## 🧩 Exercise 1 — Shortest Paths with Special Edges

### Problem Description
Given a **directed weighted graph** \( G = (V, E) \) with some edges marked as *special*,  
find the shortest walk or path from a source vertex \( s \) to a target vertex \( t \)  
subject to different constraints on the number of special edges used.

Each edge is defined as:
