
# 🎬 Movie Recommender System

A content-based movie recommendation system built with Python and Streamlit that recommends movies similar to a user's selected movie. The application uses a precomputed similarity matrix to generate recommendations and the TMDB API to fetch movie posters.

---

## 🚀 Live Demo

👉 **[Try the Movie Recommender](https://movie-recommender-system-lyyv6mkiaothvjz6ligxnc.streamlit.app/)**

---

## 📌 Overview

The Movie Recommender System helps users discover movies based on their preferences.

Users can select a movie from the application, and the system analyzes the similarity between movies to recommend the most relevant titles. Each recommendation is displayed along with its movie poster, fetched dynamically using the TMDB API.

The application provides a simple and interactive interface through Streamlit.

---

## ✨ Features

- 🎥 Content-based movie recommendations
- 🔍 Search and select movies interactively
- 🤝 Recommends movies based on similarity
- 🖼️ Dynamically fetches movie posters using the TMDB API
- ⚡ Fast recommendations using a precomputed similarity matrix
- 🌐 Interactive Streamlit web application
- 📱 Clean and simple user interface

---

## 🧠 Recommendation Workflow

The recommendation process follows these steps:

1. The user selects a movie.
2. The system identifies the selected movie from the movie dataset.
3. The corresponding movie index is retrieved.
4. The precomputed similarity matrix is used to find similar movies.
5. The movies with the highest similarity scores are selected.
6. Movie IDs are used to request poster information from the TMDB API.
7. The recommended movie titles and posters are displayed in the Streamlit application.

### Workflow

```text
                    User
                     │
                     ▼
              Select a Movie
                     │
                     ▼
              Movie Dataset
                     │
                     ▼
          Find Selected Movie Index
                     │
                     ▼
        Precomputed Similarity Matrix
                     │
                     ▼
          Find Similar Movies
                     │
                     ▼
          Top Movie Recommendations
                     │
                     ▼
               TMDB API
                     │
                     ▼
             Movie Posters
                     │
                     ▼
              Streamlit UI
````

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Data Processing & Machine Learning

* Pandas
* NumPy
* Scikit-learn

### Web Application

* Streamlit

### API

* TMDB API

### Data & Model Storage

* Pickle
* Git LFS

### HTTP Requests

* Requests

---

## 📂 Project Structure

```text
movie-recommender-system/
│
├── app.py
├── movies.pkl
├── movies_dict.pkl
├── similarity.pkl
├── requirements.txt
├── README.md
└── ...
```

### Important Files

| File               | Description                               |
| ------------------ | ----------------------------------------- |
| `app.py`           | Main Streamlit application                |
| `movies.pkl`       | Processed movie data                      |
| `movies_dict.pkl`  | Movie information used by the application |
| `similarity.pkl`   | Precomputed movie similarity matrix       |
| `requirements.txt` | Python dependencies                       |

---

## 🤖 Recommendation System

This project uses a **content-based recommendation approach**.

Instead of relying on ratings from other users, the system recommends movies based on the similarity between movies in the dataset.

A precomputed similarity matrix is used to efficiently retrieve movies that are most similar to the movie selected by the user.

When a movie is selected, the system finds its corresponding index and uses the similarity scores to identify the top similar movies.

---

## 🖼️ Movie Posters

The application uses the **TMDB API** to dynamically retrieve movie posters.

When a recommendation is generated:

```text
Recommended Movie
       ↓
TMDB Movie ID
       ↓
TMDB API
       ↓
Poster URL
       ↓
Streamlit
       ↓
Movie Poster
```

The poster is then displayed alongside the recommended movie title.

---

## 🔑 TMDB API Configuration

The application uses the TMDB API to retrieve movie poster information.

You will need a TMDB API key to use the poster-fetching functionality.

For security, API keys should be stored securely and should **not be committed directly to GitHub**.

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate into the project:

```bash
cd movie-recommender-system
```

### 2. Install the required dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📦 Requirements

The project uses the following major Python libraries:

```text
streamlit
pandas
numpy
scikit-learn
requests
```

---

## 💾 Git LFS

The `similarity.pkl` file is relatively large and exceeds GitHub's standard file-size limit.

To handle the large files, **Git Large File Storage (Git LFS)** was used.

The following files are tracked using Git LFS:

```text
movies.pkl
movies_dict.pkl
similarity.pkl
```

This allows the required model/data files to be stored with the project without exceeding GitHub's normal file-size restrictions.

---

## 🚀 Deployment

The application can be deployed using **Streamlit Community Cloud**.

After connecting the GitHub repository, configure the application to run:

```bash
streamlit run app.py
```

Once deployed, the application can be accessed through a public URL.

---

## 🔮 Future Improvements

* 🎯 Improve recommendation accuracy
* 🔎 Add advanced movie search and filtering
* 🎭 Add genre-based filtering
* ⭐ Include movie ratings and reviews
* 📊 Add additional movie information
* 👤 Add personalized user preferences
* 🌐 Improve the overall UI/UX
* 📱 Improve mobile responsiveness
* 🤖 Experiment with more advanced recommendation techniques

---

## 🎯 Project Highlights

* Built a complete movie recommendation web application using Python.
* Implemented a content-based recommendation approach.
* Used a precomputed similarity matrix for efficient recommendations.
* Integrated the TMDB API for dynamically retrieving movie posters.
* Built an interactive user interface using Streamlit.
* Used Git LFS to manage large `.pkl` files.

---

## 👨‍💻 Author

### Mohammed Yaassin

**Computer Science & Engineering**

GitHub: [YaassinMD]([YOUR_GITHUB_PROFILE_URL](https://github.com/YaassinMD))


⭐ If you found this project interesting, consider giving the repository a star!





