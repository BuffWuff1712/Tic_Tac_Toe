# 🧠 Tic-Tac-Toe AI (React + Flask + Docker)

A full-stack Tic-Tac-Toe game where you play against an AI powered by the **Minimax algorithm**, a classical machine learning approach used in turn-based games. Built with **React** for the frontend and **Flask** for the backend, and containerised using **Docker Compose** for easy setup and deployment.

---

## 📦 Tech Stack

- **Frontend**: React
- **Backend**: Flask
- **AI Algorithm**: Minimax (Classical ML)
- **DevOps**: Docker, Docker Compose

---

## ✨ Features

- 🤖 AI opponent that uses the Minimax algorithm for optimal play
- 🎮 Simple and intuitive user interface
- ⚙️ REST API endpoint to interact with the AI logic
- 🔀 Supports difficulty adjustment (depth-limited Minimax)
- 🐳 Containerised with Docker for ease of use

---

## 🚀 Getting Started

### ✅ Prerequisites

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### 🛠️ Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/BuffWuff1712/Tic_Tac_Toe.git
   cd Tic_Tac_Toe
   ```

2. **Build and run the containers**

   Open your terminal and run the following command:

   ```bash
   docker-compose up --build
   ```
   This command will:
   - Build the Docker images for both frontend and backend
   - Start both containers
   - Connect them via Docker’s internal network
  
3. **Open the app in your browser**

   Once the containers are running, open:
   ```arduino
   http://localhost:3000
   ```
   You should see the Tic-Tac-Toe game interface. You can now play against the AI!

## 💡 Future Improvements

Here are some ideas for future enhancements to the project:

- 📊 Display a running scoreboard (wins, losses, draws)
- 🎨 Improve the UI/UX with animations or sound effects
- 🔄 Add a game history
- 📱 Make the interface mobile responsive
- 🌐 Deploy the app online (e.g., Render, Railway, or GitHub Pages + API host)
- 🧪 Add unit tests for the AI and backend logic
