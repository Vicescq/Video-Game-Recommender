import { useEffect, useState } from "react"
import NavBar from "../Components/NavBar.jsx"
import Loading from "../Components/Loading"


export default function Home(){
    return(
        <>
        <NavBar/>
        <div className="container my-28">
          <Card/>

        </div>

        </>
    )
} 


function Card(){
    const [data, setData] = useState(null)
    
    useEffect(() => {
        fetch("http://127.0.0.1:5000/dev")
          .then(res => res.json())
          .then( data => setData(data))
          .catch((error) => console.log(error))
    }, [])
    return(
        <div>
            { 
            data ? 
            <>
            <img src={data.data[0]["img"]}/>
            {data.data[0]["name"]}
            </>
            : 
            <Loading/>
            }
        </div>
    )
}