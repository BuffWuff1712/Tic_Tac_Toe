import React, { useState, useEffect } from "react";
import axios from "axios";
import "./App.css";

const API_URL = process.env.REACT_APP_API_URL || "http://localhost:5000";

const EMPTY_BOARD = [
  ["", "", ""],
  ["", "", ""],
  ["", "", ""],
];

function App() {
  const [board, setBoard] = useState(EMPTY_BOARD);
  const [currentPlayer, setCurrentPlayer] = useState("X");
  const [aiPlayer, setAiPlayer] = useState("O");
  const [humanPlayer, setHumanPlayer] = useState("X");
  const [difficulty, setDifficulty] = useState("medium");
  const [gameOver, setGameOver] = useState(false);

  const checkWinner = (b) => {
    const lines = [
      // Rows & columns
      ...b,
      [b[0][0], b[1][0], b[2][0]],
      [b[0][1], b[1][1], b[2][1]],
      [b[0][2], b[1][2], b[2][2]],
      // Diagonals
      [b[0][0], b[1][1], b[2][2]],
      [b[0][2], b[1][1], b[2][0]],
    ];
    for (let line of lines) {
      if (line.every((cell) => cell === "X")) return "X";
      if (line.every((cell) => cell === "O")) return "O";
    }
    return b.flat().every(cell => cell !== "") ? "draw" : null;
  };

  const handleClick = async (row, col) => {
    if (board[row][col] !== "" || gameOver || currentPlayer !== humanPlayer) return;
  
    // Make a copy of the board and update it
    const newBoard = board.map((r) => [...r]);
    newBoard[row][col] = humanPlayer;
    setBoard(newBoard);
    setCurrentPlayer(aiPlayer);
  
    // Check if human won
    const result = checkWinner(newBoard);
    if (result) {
      setGameOver(true);
      setTimeout(() => alert(result === "draw" ? "It's a draw!" : `${result} wins!`), 200);
      return;
    }
  
    // AI move (delay for effect)
    setTimeout(async () => {
      try {
        const res = await axios.post(`${API_URL}/ai-move`, {
          board: newBoard,
          ai: aiPlayer,
          human: humanPlayer,
          difficulty,
        });
  
        const aiMove = res.data.move;
        if (aiMove) {
          const updatedBoard = newBoard.map((r) => [...r]);
          updatedBoard[aiMove[0]][aiMove[1]] = aiPlayer;
          setBoard(updatedBoard);
          setCurrentPlayer(humanPlayer);
  
          // Check AI win condition
          const newResult = checkWinner(updatedBoard);
          if (newResult) {
            setGameOver(true);
            setTimeout(() => alert(newResult === "draw" ? "It's a draw!" : `${newResult} wins!`), 200);
          }
        }
      } catch (error) {
        console.error("AI move error:", error);
      }
    }, 500); // Small delay for better UI experience
  };
  

  const resetGame = () => {
    setBoard(EMPTY_BOARD);
    setCurrentPlayer(humanPlayer);
    setGameOver(false);
  };

  return (
    <div className="App">
      <h1>Tic-Tac-Toe vs AI</h1>
      <div>
        <label>Difficulty: </label>
        <select value={difficulty} onChange={(e) => setDifficulty(e.target.value)}>
          <option value="easy">Easy</option>
          <option value="medium">Medium</option>
          <option value="hard">Hard</option>
        </select>
      </div>
      <div className="board">
        {board.map((row, r) =>
          row.map((cell, c) => (
            <button key={`${r}-${c}`} className="cell" onClick={() => handleClick(r, c)}>
              {cell}
            </button>
          ))
        )}
      </div>
      <button onClick={resetGame}>Reset</button>
    </div>
  );
}

export default App;
