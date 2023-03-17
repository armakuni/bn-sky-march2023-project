import React from 'react'
import Product from './Product'

function ProductList({setCart, products, version}) {
  return (
    <div>{
        products.map(product =>{
            return <Product 
            name={product.name} 
            price={product.price} 
            quantity={product.quantity}
            setCart={setCart}
            version={version}
            />
        })
    }</div>
  )
}

export default ProductList