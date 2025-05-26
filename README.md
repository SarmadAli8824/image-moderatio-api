# 🛡️ Image Moderation API

A FastAPI-based microservice that uses an external moderation API to detect inappropriate (NSFW) images by analyzing their URLs and storing the results in MongoDB Atlas.

---

## 📦 Features

- 🔍 Accepts image URLs and checks them for adult/inappropriate content.
- 🧠 Uses [ModerateContent API](https://www.moderatecontent.com/) for image moderation.
- ☁️ Stores results in MongoDB Atlas.
- 🧪 Postman(swagger ui for checking) for testing.
- 🐳 Dockerized for easy deployment.

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/image-moderation-api.git
cd image-moderation-api
