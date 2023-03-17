import React from 'react'
import { useState } from 'react';
import {users} from "../staticData/users.js"

function LoginPage({setUser, user}) {

    const [currentInput, setCurrentInput] = useState(null);

    const updateUser = () =>{
        let userFilter = users.filter(user => user.name == currentInput );
        console.log(userFilter);
        if(userFilter.length > 0){
            setUser(currentInput);
            localStorage.setItem("currentUser", user);
            localStorage.setItem("currentCart", []);
        }
    }

  return (
    <div>
        <form onSubmit={updateUser}>
            <input type="text" placeholder="username" onChange={(e)=>setCurrentInput(e.target.value)} />
            <button type="submit">login</button>
        </form>
    </div>
  )
}

export default LoginPage