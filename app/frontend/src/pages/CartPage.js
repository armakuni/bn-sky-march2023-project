import React from 'react'
import ProductList from '../components/ProductList'
import { Link } from 'react-router-dom'

function CartPage({cart}) {

    const sumItems = () => {
        let sum = 0;
        cart.forEach(item => {
            sum += item.price;
        });
        return sum;
    }

  return (
    <div>
        <button><Link to="/">Return to shopping</Link></button>
        <h3>ITEMS IN CART:</h3>
        <ProductList products={cart} version="cartview"/>
        <h1>TOTAL PRICE: {sumItems().toFixed(2)}</h1>
    </div>
  )
}

export default CartPage