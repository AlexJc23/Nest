<<<<<<< HEAD
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

=======
# Welcome to your Expo app 👋

This is an [Expo](https://expo.dev) project created with [`create-expo-app`](https://www.npmjs.com/package/create-expo-app).

## Get started

1. Install dependencies

   ```bash
   npm install
   ```

2. Start the app

   ```bash
   npx expo start
   ```

In the output, you'll find options to open the app in a

- [development build](https://docs.expo.dev/develop/development-builds/introduction/)
- [Android emulator](https://docs.expo.dev/workflow/android-studio-emulator/)
- [iOS simulator](https://docs.expo.dev/workflow/ios-simulator/)
- [Expo Go](https://expo.dev/go), a limited sandbox for trying out app development with Expo

You can start developing by editing the files inside the **app** directory. This project uses [file-based routing](https://docs.expo.dev/router/introduction).

## Get a fresh project

When you're ready, run:

```bash
npm run reset-project
```

This command will move the starter code to the **app-example** directory and create a blank **app** directory where you can start developing.

## Learn more

To learn more about developing your project with Expo, look at the following resources:

- [Expo documentation](https://docs.expo.dev/): Learn fundamentals, or go into advanced topics with our [guides](https://docs.expo.dev/guides).
- [Learn Expo tutorial](https://docs.expo.dev/tutorial/introduction/): Follow a step-by-step tutorial where you'll create a project that runs on Android, iOS, and the web.

## Join the community

Join our community of developers creating universal apps.

- [Expo on GitHub](https://github.com/expo/expo): View our open source platform and contribute.
- [Discord community](https://chat.expo.dev): Chat with Expo users and ask questions.
>>>>>>> d194292 (startup)
