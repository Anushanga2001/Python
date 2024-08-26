import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Test from "./pages/Test"; 
import Test1 from "./pages/Test1";

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route exact path="/" element={<Test />} />
          <Route exact path="/Test1" element={<Test1 />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
