import controller from "../Assets/controller.svg"
import searchbar from "../Assets/searchbar.svg"

export default function NavBar(){


    return(
        <>
        <nav className="bg-slate-800 py-1 flex">
            <ul className="flex">
                <img src={controller} className="max-w-12"/>
                <img src={controller} className="max-w-12"/>
                <img src={controller} className="max-w-12"/>
                <img src={controller} className="max-w-12"/>
            </ul>

            <ul className="flex ml-auto">
                <img src={searchbar} className="max-w-12"/>
                <img src={controller} className="max-w-12"/>
            </ul>
        </nav>
        
        </>
    )
        
    
}