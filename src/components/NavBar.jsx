import controller from "../Assets/controller.svg"
import search from "../Assets/search.svg"
import { Link } from "react-router"
export default function NavBar(){


    return(
        <>
        <nav className="bg-slate-800 py-2 px-5 flex">
            <ul className="flex">
                <Link to="/"><img src={controller} className="min-w-8 cursor-pointer"/> </Link>
            </ul>

            <ul className="flex ml-auto">
                <Link to="/gameprofile"><img src={search} className="min-w-8 cursor-pointer"/></Link>
            </ul>
        </nav>
        </>
    )
        
    
}