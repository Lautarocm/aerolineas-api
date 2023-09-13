"use client"

import { useSearch } from "@/app/hooks/useSearch"
import { Spinner } from "@nextui-org/react"
import { Offers } from "../Offers/Offers"
import styles from "./OffersContainer.module.css"

export function OffersContainer(){

    const {loading} = useSearch()


    return(
        <div className={styles.offersContainer}>
            {
            loading ? 
            <Spinner />: 
            <Offers />
            }
        </div>
    )
}