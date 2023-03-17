import React from 'react'

function Product({name, price, quantity, setCart, version}) {

    const addToCart = () => {
        let cart = localStorage.getItem("currentCart") ? JSON.parse(localStorage.getItem("currentCart")) : [];
        if(cart.length > 0){
            cart.push({name: name, price: price})
        }
        else{
            cart = [{name: name, price: price}]
        }
        localStorage.setItem("currentCart", JSON.stringify(cart))
        setCart(cart);
    }

    const makeProduct = () => {
        if(version == "mainview"){
            return(
                <div>
        <h2>{name}</h2>
        <h3>{price}</h3>
        <button onClick={addToCart}>Add to cart</button>
    </div>
            )

        }else if(version == "cartview"){
            return(
                <div>
        <h2>{name}</h2>
        <h3>{price}</h3>
    </div>
            )
        }else{
            return "No content"
        }
    }

  return (
    <div>
        {makeProduct()}
    </div>
  )
}

export default Product