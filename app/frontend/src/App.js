import {Routes, Route, Link, Navigate} from "react-router-dom";
import MainPage from "./pages/MainPage";
import CartPage from "./pages/CartPage";
import LoginPage from "./pages/LoginPage";
import { useState } from "react";

function App() {
  const [user, setUser] = useState(localStorage.getItem("currentUser"));
  const [cart, setCart] = useState(localStorage.getItem("currentCart") ? JSON.parse(localStorage.getItem("currentCart")) : []);

  console.log(cart);
  return (
    <div className="App">
        <Routes>
          <Route path="/" element={ user == null ?
          <LoginPage setUser={setUser} user={user}/> 
          : <MainPage setCart={setCart} setUser={setUser}/>}/>
          <Route path="/cart" element={<CartPage cart={cart}/>}/>
        </Routes>
    </div>
  );
}

export default App;
