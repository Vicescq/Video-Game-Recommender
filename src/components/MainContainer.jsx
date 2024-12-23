import styles from "./MainContainer.module.css"


function MainContainer({content}){
    return(
        <div className={styles.container}>

        {content}

        </div>
    )


}

export default MainContainer