import { useSelect } from "@/app/hooks/useSelect"
import styles from "./Searchbox.module.css"
import { CustomSelect } from "../CustomSelect/CustomSelect"
import { SearchButtons } from "../SearchButtons/SearchButtons"

export function Searchbox(){

    const {handleOrigin, handleDestination} = useSelect()

    return(
        <div className={styles.filtersContainer}>
            <CustomSelect
            className={styles.select}
            onChange={handleOrigin} label="Origen" />
            <CustomSelect
            className={styles.select}
            onChange={handleDestination} label="Destino" />
            <SearchButtons />
        </div>
    )
}