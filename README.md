# Nest by Hawx

## Overview

Nest by Hawx is an internal, work-focused social media **mobile application** built exclusively for **Hawx Pest Control employees**. It provides a centralized platform for communication, collaboration, and company updates—without the distractions of traditional social media.

The application intentionally avoids personal social features (such as friends, direct messages, or private profiles) to maintain a professional, work-first environment.

---

## Features

### Company Announcements
- Organization-wide announcements and important updates

### Main Social Feed
- Centralized feed for work-related posts and engagement
- Support for image-based posts

### Teams & Groups
- Branch-based or manager-created teams
- Collaboration spaces for departments or initiatives

### Events & RSVPs
- Company or team events
- Built-in RSVP tracking

### Media Uploads
- Secure photo uploads for posts and events
- Images stored and served via AWS infrastructure

### External Messaging
- Google Chat deep links for real-time communication
- No internal chat system

---

## Design Principles

- Professional and work-focused
- No personal social networking features
- Role-based access and permissions
- Scalable across branches and teams
- Mobile-first user experience

---

## Tech Stack

### Frontend (Mobile)
- React Native
- Redux Toolkit
- React Navigation

### Backend
- Python
- FastAPI
- SQLAlchemy
- PostgreSQL

### Authentication
- JWT-based authentication

### Media Storage
- AWS S3 for image storage
- Pre-signed URLs for secure uploads and access

### Messaging Integration
- Google Chat (deep links only)

---

## Project Status

Nest by Hawx is actively under development and intended for internal use only.

