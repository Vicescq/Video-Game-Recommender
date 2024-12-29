import { useEffect, useState } from "react"
import NavBar from "../Components/NavBar.jsx"
import Loading from "../Components/Loading"

export default function Home(){
    
    const [data, setData] = useState(null)
    
    useEffect(() => {
        fetch("http://127.0.0.1:5000/dev")
          .then(res => res.json())
          .then( data => setData(data))
          .catch((error) => console.log(error))
    }, [])

    

    
    return(
        <>
        <NavBar/>
        <div className="container my-28">
            <table className="sm:border-2 border-solid m-auto min-w-96">
                <thead>
                    <th>Portrait</th>
                    <th>Name</th>
                    <th>Status</th>
                    <th>Rating</th>
                </thead>
                <tbody>
                  <th>
                    {data ? (
                      <img src={data.data[0].img}/>
                    ) : (
                      <Loading/>
                    )}
                </th>
                    <th>1</th>
                    <th>1</th>
                    <th>1</th>
                    <th>1</th>
                    <th>1</th>
                </tbody>
            </table>

        </div>

        </>
    )
} 