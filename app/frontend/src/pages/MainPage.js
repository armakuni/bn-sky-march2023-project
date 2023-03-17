import React from 'react'
import ProductList from '../components/ProductList'
import { products } from '../staticData/products'
import {Link} from "react-router-dom";

function MainPage({setCart, setUser}) {

    const logout = () => {
        setUser(null)
    }

  return (
    <div>
        <button><Link to="/cart">Go to cart</Link></button>
        <button onClick={logout}>Logout</button>
        <h3>ITEMS FOR SALE:</h3>
        <ProductList setCart={setCart} products={products} version="mainview"/>
    </div>
  )
}

export default MainPage