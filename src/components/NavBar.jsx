import controller from "../Assets/controller.svg"
import search from "../Assets/search.svg"
import { Link } from "react-router"

export default function NavBar(){


    return(
        <>
        <nav className="bg-slate-800 py-2 px-5 flex">
            <ul className="flex">
                <li><img src={controller} className="min-w-8 hover:cursor-pointer"/> <a href="/page"></a></li>
                

            </ul>

            <ul className="flex ml-auto">
                <li>
                    <img src={search} className="min-w-8 hover:cursor-pointer"/>
                    <Link to="/gameprofile"></Link>
                </li> 

            </ul>
        </nav>
        
        </>
    )
        
    
}