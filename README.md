
# 🛡️ Image Moderation API

A FastAPI-based microservice that detects inappropriate (NSFW) images by analyzing image URLs using a third-party API and stores the moderation results in MongoDB Atlas.

---

## 📦 Features

- 🔍 Accepts image URLs via POST request.
- 🧠 Integrates with [ModerateContent API](https://www.moderatecontent.com/) for image content analysis.
- ☁️ Saves moderation results in MongoDB Atlas.
- 🧪 Easy testing using Swagger UI (`/docs`) or Postman.
- 🐳 Fully Dockerized for consistent and easy deployment.

---

## 📁 Project Structure

```
Image-Moderation-api/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── database.py
├── .env.example
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/SarmadAli8824/image-moderatio-api.git
cd image-moderatio-api
```

### 2. Create and Configure `.env` File
Create a `.env` file based on `.env.example` and add:

```env
MONGODB_URI=your_mongodb_atlas_connection_string
MODERATE_API_KEY=your_moderatecontent_api_key
```

---

## 🚀 Running the Application

### Option 1: Run Locally (Without Docker)

#### Step 1: Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate      # Windows
# OR
source venv/bin/activate   # Mac/Linux
```

#### Step 2: Install dependencies
```bash
pip install -r requirements.txt
```

#### Step 3: Run the server
```bash
uvicorn app.main:app --reload --port 7000
```

Visit: `http://localhost:7000/docs` to access the Swagger UI.

---

### Option 2: Run with Docker

Make sure Docker and Docker Compose are installed.

```bash
docker-compose up --build
```

Swagger UI: `http://localhost:7000/docs`

---

## 🧪 API Usage

### Endpoint: `POST /moderate/`

#### Sample Request:
```json
{
  "image_url": "https://moderatecontent.com/img/sample.jpg"
}
```

#### Sample Response:
```json
{
  "image_url": "https://moderatecontent.com/img/sample.jpg",
  "rating_label": "everyone",
  "rating_index": 1,
  "prediction": "safe",
  "probability": 0.95
}
```

---

## 🧰 Testing with Postman

1. Open Postman.
2. Create a **POST** request to:
   ```
   http://localhost:7000/moderate/
   ```
3. Go to **Body** → Select `raw` → `JSON`.
4. Paste:
   ```json
   {
     "image_url": "https://moderatecontent.com/img/sample.jpg"
   }
   ```
5. Click **Send** to see the moderation results.

---

## 🐙 GitHub Deployment

### Push to GitHub (if not already done):

```bash
git add .
git commit -m "Initial project commit"
git push origin main
```

---

## 🧾 .env.example

```env
# MongoDB connection string
MONGODB_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/dbname?retryWrites=true&w=majority

# ModerateContent API key
MODERATE_API_KEY=your_api_key_here
```

---

## 📄 License

This project is provided for educational/demo purposes only. Use responsibly.
