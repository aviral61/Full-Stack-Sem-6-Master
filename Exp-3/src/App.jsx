import React from "react";
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import Home from "./components/home.jsx";
import About from "./components/About.jsx";
import SinglePageApp from "./components/Spa.jsx";

const App = () => {
  return (
    <>
      <SinglePageApp/>
    </>
  );
};
export default App;