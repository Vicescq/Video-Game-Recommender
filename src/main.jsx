import React from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter, Routes, Route } from 'react-router'
import './index.css'
import Home from "./Pages/Home"
import GameProfile from './Pages/GameProfile'

const root = document.getElementById("root")


ReactDOM.createRoot(root).render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Home/>}/>
        <Route path='/gameprofile' element={<GameProfile/>}/>
      </Routes>
    </BrowserRouter>
    
  </React.StrictMode>,
)
