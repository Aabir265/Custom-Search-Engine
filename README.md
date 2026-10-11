# 🔎 Custom Search Engine

A web-based search application that helps users discover relevant content across multiple social media platforms through a single search query, powered by the **Exa Search API**.

## 📌 About the Project

The Custom Search Engine is a personal web development project built to explore API integration, frontend-backend communication, and search functionality.

Instead of searching each platform separately, users can enter a topic or keyword and retrieve relevant web results from supported platforms such as YouTube, Instagram, and X.

The project is a work in progress, with ongoing improvements to search relevance and platform diversity.

## ✨ Features

- 🔍 Search for topics using a simple interface.
- 🌐 Retrieve web results through the Exa Search API.
- 🔗 Display result titles and clickable URLs.
- ⚡ Connect the frontend and backend using HTTP requests and JSON.
- 🐍 Process search requests using a Python Flask backend.
- 🔐 Store API credentials in an environment file rather than hardcoding them.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| HTML5 | Frontend structure |
| CSS3 | UI styling and layout |
| JavaScript | Form handling, API requests, and rendering results |
| Python | Backend logic |
| Flask | Web framework and API endpoints |
| Exa Search API | Web search and content retrieval |
| python-dotenv | Environment variable management |
| Figma & Figma AI | UI design and initial frontend code generation |

## 🏗️ How It Works

1. The user enters a search query in the frontend.
2. JavaScript captures the query and sends it to the Flask backend as a JSON request.
3. Flask passes the query to the Exa Search API.
4. Exa retrieves relevant web results from the configured domains.
5. Flask returns the results as JSON.
6. JavaScript processes the response and displays the result titles and links.

## 📂 Project Structure

```text
custom-search-engine/
│
├── app.py              # Exa API integration and search logic
├── web.py              # Flask application and routes
├── index.html          # Main search page
├── results.html        # Results template, if used
├── script.js           # Frontend search functionality
├── style.css           # Styling
├── .env                # API credentials (not committed)
├── .gitignore          # Files excluded from Git
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

*Note: Adjust the filenames to match your actual repository. If `results.html` isn't used by the current application, you can omit it.*

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd custom-search-engine
```

Replace the placeholder with your actual GitHub repository URL.

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install flask exa-py python-dotenv
```

### 4. Configure your API key

Create a `.env` file in the project root:

```env
EXA_API_KEY=your_exa_api_key_here
```

Replace the placeholder with your own Exa API key. Never publish your actual API key or commit the `.env` file to GitHub.

### 5. Run the application

If your Flask entry point is `web.py`, run:

```bash
python web.py
```

Open the local address displayed in your terminal, usually:

```text
http://127.0.0.1:5000/
```

## 🔑 Environment Variables

| Variable | Description |
|---|---|
| `EXA_API_KEY` | API key used to authenticate requests to Exa |

## 🧠 Development Workflow & AI Assistance

- **UI Design:** Used Figma to design the frontend interface.
- **AI-Assisted Development:** Used Figma AI to generate the initial HTML and CSS.
- **Frontend Integration:** Worked with JavaScript to handle search submissions, send requests, and render results.
- **Backend Integration:** Connected the frontend to a Flask backend and integrated the Exa Search API.
- **Debugging:** Tested and refined the request-response flow and search configuration.

AI-assisted tools were part of the development workflow. This project is also a learning exercise in understanding API integration, debugging, and building a complete web application.

## 🚧 Current Limitations

- Search relevance can vary depending on the query and available indexed content.
- Some platforms may return more results than others.
- Results depend on what the search API can retrieve and index.
- Platform diversity and result ranking are areas for further improvement.

## 🔮 Future Improvements

- [ ] Improve result relevance and ranking.
- [ ] Improve distribution of results across supported platforms.
- [ ] Display platform labels for each result.
- [ ] Add loading indicators and more detailed error messages.
- [ ] Add filters for individual platforms.
- [ ] Improve the responsive design for mobile devices.
- [ ] Add automated tests for backend search functionality.

## 🎯 What I Learned

Through this project, I explored:

- Frontend-backend communication.
- HTTP `POST` requests and JSON responses.
- Integrating third-party APIs with Python.
- Building routes and endpoints with Flask.
- Handling environment variables and API credentials.
- Debugging and improving a web application's search flow.
- Using AI-assisted tools as part of a development workflow.

## 👨‍💻 Author

**Aabir Sharma**

Connect with me on [LinkedIn](<https://www.linkedin.com/in/aabir-sharma-2296b3375/L>) or explore my other projects on [GitHub](<https://github.com/Aabir265>).

---

⭐ If you find this project interesting, feel free to explore the repository and share feedback!
